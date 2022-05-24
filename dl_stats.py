import pandas as pd
from config import MAN_CSV, WORK_SIGNATURS
from utils import yield_manifestation

df = pd.DataFrame(yield_manifestation())
work_sig_df = pd.read_csv(WORK_SIGNATURS)
merged = pd.merge(df, work_sig_df, on='werk_signatur_id')
merged['man_full_sig'] = merged["werk_signatur"] + merged["man_sig"]
merged = merged[~merged.man_full_sig.str.contains(">", na=False)]
merged = merged.dropna(subset=['man_full_sig'])
merged.to_csv(MAN_CSV, index=False)
