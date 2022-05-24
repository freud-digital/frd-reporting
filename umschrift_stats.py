import time
import pandas as pd
import json
from config import MAN_CSV, UMSCHRIFT_DATA, DIPL_UMSCHRIFT_MAPPING, ALL_MAN

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


works = df.groupby(['work_title'])

result = {
    "Keine Transkripte": 0,
    "Teilweise transkribiert": 0,
    "Fertig transkribiert": 0
}
for _, x in df.groupby(['work_title']):
    status = set()
    for i, row in x.iterrows():
        status.add(row['man_field_status_umschrift'])
    if len(status) > 1:
        result["Teilweise transkribiert"] += 1
    elif list(status)[0] == 0:
        result["Keine Transkripte"] += 1
    else:
        result["Fertig transkribiert"] += 1

data = [[key, value] for key, value in result.items()]

with open(f"{UMSCHRIFT_DATA.replace('umschrift.json', 'works_hc.json')}", 'w') as f:
    json.dump(data, f, ensure_ascii=True)

man_stat = dict(df.groupby('man_field_status_umschrift').size())
data = [
    [DIPL_UMSCHRIFT_MAPPING[key], int(value)] for key, value in man_stat.items()
]

with open(f"{UMSCHRIFT_DATA.replace('umschrift.json', 'manifestations_hc.json')}", 'w') as f:
    json.dump(data, f, ensure_ascii=True)

df = pd.read_csv(ALL_MAN)
man_stat = dict(df.groupby('fwf').size())
data = [
    ['FWF' if key else 'Nicht FWF', int(value)] for key, value in man_stat.items()
]

with open(f"{UMSCHRIFT_DATA.replace('umschrift.json', 'all_works_hc.json')}", 'w') as f:
    json.dump(data, f, ensure_ascii=True)
