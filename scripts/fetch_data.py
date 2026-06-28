# import packages
# ===============================
# import packages
# ===============================
import pandas as pd
import requests
from datetime import datetime as dt, timezone, timedelta
from pathlib import Path
import urllib3 as lib3

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
end_date = dt.now(timezone.utc)
time_lag = timedelta(days=7)
start_date = pd.Timestamp(end_date - time_lag).round('D').strftime('%Y-%m-%d %H:%M:%S')
end_date = pd.Timestamp(end_date).strftime('%Y-%m-%d %H:%M:%S')

params = {
    'startTime' : start_date,
    'endTime' : end_date
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

# ===============================
# 2 - NESO demand data
# ===============================
# API request - NESO demand data
url = 'https://api.neso.energy/api/3/action/datastore_search?resource_id=177f6fa4-ae49-4182-81ea-0c6b35f26ca6'

response = requests.get(url)

if response.status_code == 200:
    print('NESO demand API call successful!')
else:
    raise Exception(f"NESO demand API call not successful. Status code: {response.status_code}")

dmnd = response.json()

dmnd = dmnd['result']['records']

dmnd = pd.json_normalize(dmnd)

dmnd = pd.DataFrame(dmnd)