import time
import pandas as pd
import json
from config import MAN_CSV, UMSCHRIFT_DATA

df = pd.read_csv(MAN_CSV)

with open(UMSCHRIFT_DATA, 'r') as f:
    data = json.load(f)

umschrift = df.groupby(['man_field_status_umschrift'])
data[int(time.time() * 1000)] = {
    key: int(value) for key, value in dict(umschrift.size()).items()
}
with open(UMSCHRIFT_DATA, 'w') as f:
    json.dump(data, f, ensure_ascii=True)

with open(UMSCHRIFT_DATA, 'r') as f:
    data = json.load(f)

data_array = [
    [float(key), value['2']] for key, value in data.items()
]

with open(f"{UMSCHRIFT_DATA.replace('.json', '_hc.json')}", 'w') as f:
    json.dump(data_array, f, ensure_ascii=True)