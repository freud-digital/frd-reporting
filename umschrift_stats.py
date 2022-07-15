import time
import pandas as pd
import json
from collections import Counter
from config import MAN_CSV, UMSCHRIFT_DATA, DIPL_UMSCHRIFT_MAPPING, ALL_MAN, STOPWORDS, HAVE_TEI

df = pd.read_csv(MAN_CSV)

work_stat = []
for i, x in df.groupby('work_id'):
    status = set()
    for i, row in x.iterrows():
        status.add(row['man_field_status_umschrift'])
    if len(status) > 1:
        item = {
            'work_id': row['work_id'],
            'work_status': "Teilweise transkribiert"
        }
    elif list(status)[0] == 0:
        item = {
            'work_id': row['work_id'],
            'work_status': "Keine Transkripte"
        }
    else:
        item = {
            'work_id': row['work_id'],
            'work_status': "Fertig transkribiert"
        }
    work_stat.append(item)
work_stat_df = pd.DataFrame(work_stat)

df_have_tei = pd.read_csv(HAVE_TEI)

merged = pd.merge(df, work_stat_df, on='work_id')
merged_with_tei = pd.merge(df_have_tei, merged, on='man_id', how='right')
merged_with_tei.to_csv(MAN_CSV)
df = None
df = pd.read_csv(MAN_CSV)

hansi = df.to_json(orient='records')
data_table = {
    'data': json.loads(hansi)
}
with open(f"{MAN_CSV.replace('manifestations.csv', 'data_table_2.json', )}", 'w') as f:
    json.dump(data_table, f, ensure_ascii=False)

# with open(UMSCHRIFT_DATA, 'r') as f:
#     data = json.load(f)

# umschrift = df.groupby(['man_field_status_umschrift'])
# data[int(time.time() * 1000)] = {
#     key: int(value) for key, value in dict(umschrift.size()).items()
# }
# with open(UMSCHRIFT_DATA, 'w') as f:
#     json.dump(data, f, ensure_ascii=True)

# with open(UMSCHRIFT_DATA, 'r') as f:
#     data = json.load(f)

# data_array = [
#     [float(key), value['2']] for key, value in data.items()
# ]

# with open(f"{UMSCHRIFT_DATA.replace('.json', '_hc.json')}", 'w') as f:
#     json.dump(data_array, f, ensure_ascii=True)


# works = df.groupby(['work_title'])

# result = {
#     "Keine Transkripte": 0,
#     "Teilweise transkribiert": 0,
#     "Fertig transkribiert": 0
# }
# for _, x in df.groupby(['work_title']):
#     status = set()
#     for i, row in x.iterrows():
#         status.add(row['man_field_status_umschrift'])
#     if len(status) > 1:
#         result["Teilweise transkribiert"] += 1
#     elif list(status)[0] == 0:
#         result["Keine Transkripte"] += 1
#     else:
#         result["Fertig transkribiert"] += 1

# data = [[key, value] for key, value in result.items()]

# with open(f"{UMSCHRIFT_DATA.replace('umschrift.json', 'works_hc.json')}", 'w') as f:
#     json.dump(data, f, ensure_ascii=True)

# man_stat = dict(df.groupby('man_field_status_umschrift').size())
# data = [
#     [DIPL_UMSCHRIFT_MAPPING[key], int(value)] for key, value in man_stat.items()
# ]

# with open(f"{UMSCHRIFT_DATA.replace('umschrift.json', 'manifestations_hc.json')}", 'w') as f:
#     json.dump(data, f, ensure_ascii=True)

# df = pd.read_csv(ALL_MAN)
# with open(STOPWORDS, 'r') as f:
#     stopwords = f.read().split(',')
# text = " ".join([x.split(':')[-1].strip().lower() for x in list(set(df.work_title))]).split()
# text = [x for x in text if len(x) > 3]
# text = [x for x in text if not '[' in x]  # noqa: E713
# text = [x for x in text if not '›' in x]  # noqa: E713
# text = [x for x in text if not ']' in x]  # noqa: E713
# text = [x for x in text if not '‹' in x]  # noqa: E713
# token = [x.replace('.', '').replace(',', '') for x in text if not x in stopwords]  # noqa: E713
# hansi = Counter(token)
# data = [
#     {
#         "name": key,
#         "weight": value
#     } for key, value in Counter(token).items() if value > 1
# ]
# with open(f"{UMSCHRIFT_DATA.replace('umschrift.json', 'wordcloud_data.json')}", 'w') as f:
#     json.dump(data, f, ensure_ascii=True)

# man_stat = dict(df.groupby('fwf').size())
# data = [
#     ['FWF' if key else 'Nicht FWF', int(value)] for key, value in man_stat.items()
# ]

# with open(f"{UMSCHRIFT_DATA.replace('umschrift.json', 'all_maninfestations_hc.json')}", 'w') as f:
#     json.dump(data, f, ensure_ascii=True)

# tup = list()
# for key, stat in df.groupby(['work_id', 'fwf']):
#     tup.append(key)

# dct = dict(tup)
# count_fwf = 0
# count_nicht_fwf = 0
# for key, value in dct.items():
#     if value:
#         count_fwf += 1
#     else:
#         count_nicht_fwf += 1
# data = [['Nicht FWF', count_nicht_fwf], ['FWF', count_fwf]]

# with open(f"{UMSCHRIFT_DATA.replace('umschrift.json', 'all_works_hc.json')}", 'w') as f:
#     json.dump(data, f, ensure_ascii=True)

# frieda = df.to_json(orient='records')
# man_all = {
#     'data': json.loads(frieda)
# }

# with open(ALL_MAN.replace('.csv', '.json'), 'w') as f:
#     json.dump(man_all, f, ensure_ascii=False)
