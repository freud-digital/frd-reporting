import time
import pandas as pd
import json
from config import MAN_CSV, UMSCHRIFT_DATA

df = pd.read_csv(MAN_CSV)

with open(UMSCHRIFT_DATA, 'r') as f:
    data = json.load(f)

umschrift = df.groupby(['man_field_status_umschrift'])
data[time.time()] = {
    key: int(value) for key, value in dict(umschrift.size()).items()
}
with open(UMSCHRIFT_DATA, 'w') as f:
    json.dump(data, f, ensure_ascii=True)
