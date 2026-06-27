# import packages
# ===============================
# import packages
# ===============================
import pandas as pd
import requests
from datetime import datetime as dt, timezone, timedelta
import time
import json
from pathlib import Path

# ===============================
# system paths
# ===============================
script_dir = Path(__file__).resolve().parents[1]
output_dir = script_dir / "data"

output_dir.mkdir(parents=True, exist_ok=True)

# ===============================
# API request
# ===============================
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
    print('Call successful!')
else:
    raise Exception(f"Non-success status code: {response.status_code}")