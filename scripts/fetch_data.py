# import packages
# ===============================
# import packages
# ===============================
import pandas as pd
import requests
from datetime import datetime as dt, timezone, timedelta
from pathlib import Path

# ===============================
# system paths
# ===============================
script_dir = Path(__file__).resolve().parents[1]
output_dir = script_dir / "data"

output_dir.mkdir(parents=True, exist_ok=True)

# ===============================
# 1 - Elexon generation data
# ===============================
# API request - generation data
url = 'https://data.elexon.co.uk/bmrs/api/v1/generation/outturn/summary'
today = dt.now(timezone.utc)
time_lag = timedelta(days=7)
start_date = pd.Timestamp(today - time_lag).round('D').strftime('%Y-%m-%d %H:%M:%S')
today = pd.Timestamp(today).strftime('%Y-%m-%d %H:%M:%S')

params = {
    'startTime' : start_date,
    'endTime' : today
}

response = requests.get(url, params = params)

if response.status_code == 200:
    print('Elexon generation API call successful!')
else:
    raise Exception(f"Elexon generation API call not successful. Status code: {response.status_code}")

gen = response.json()

gen = pd.json_normalize(
    gen,
    record_path=['data'],
    meta=['startTime', 'settlementPeriod']
)

# Convert data types - generation data
gen['settlementPeriod'] = pd.to_numeric(gen['settlementPeriod'])
gen['startTime'] = pd.to_datetime(gen['startTime'], utc=True)

# Pivot - generation data
gen = gen.pivot_table(
    index=['startTime', 'settlementPeriod'],
    columns='fuelType',
    values='generation'
).reset_index().rename_axis(None, axis=1)


# ===============================
# 2 - NESO demand data
# ===============================
# API request - NESO demand data
url_start = 'https://api.neso.energy'
url_end = '/api/3/action/datastore_search?resource_id=8a4a771c-3929-4e56-93ad-cdf13219dea5'


today = dt.now(timezone.utc)
start_date = pd.to_datetime('2026-01-01', utc=True)

dmnd = []

i = 1

while start_date <= today:
    url = url_start + url_end

    response = requests.get(url)

    if response.status_code == 200:
        print('NESO demand API call successful!')
    else:
        raise Exception(f"NESO demand API call not successful. Status code: {response.status_code}")

    dmnd_resp = response.json()
    records = dmnd_resp['result']['records']
    
    if not records:
        print("Reached the end of available records. Stopping.")
        break

    dmnd.extend(records)

    start_date = pd.to_datetime(dmnd_resp['result']['records'][-1]['SETTLEMENT_DATE'], utc=True)
    url_end = dmnd_resp['result']['_links']['next']

    print(f'Loop run:{i} times. Collected data up to {start_date}.')

    i += 1

    print(url)

# No flattening required!
df_dmnd = pd.DataFrame(dmnd)

# View the result
print(df_dmnd.tail())

df_dmnd['SETTLEMENT_DATE'] = pd.to_datetime(df_dmnd['SETTLEMENT_DATE'], utc=True)



#     raise Exception(f"NESO demand API call not successful. Status code: {response.status_code}")



# dmnd = dmnd['result']['records']

# dmnd = pd.json_normalize(dmnd)

# dmnd = dmnd.loc[:, ['SETTLEMENT_DATE', 'SETTLEMENT_PERIOD', 'EMBEDDED_SOLAR_GENERATION', 'EMBEDDED_WIND_GENERATION']]
# # dmnd['SETTLEMENT_DATE']

# print(gen.dtypes)
# print(dmnd.dtypes)

# jn.display(gen)
# # print(list(dmnd.columns.values))