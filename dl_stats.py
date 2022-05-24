import pandas as pd
from config import MAN_CSV, WORK_SIGNATURS, ALL_MAN
from utils import yield_manifestation, fwf_col


df = pd.DataFrame(yield_manifestation())
work_sig_df = pd.read_csv(WORK_SIGNATURS)
merged = pd.merge(df, work_sig_df, on='werk_signatur_id')
merged['man_full_sig'] = merged["werk_signatur"] + merged["man_sig"]
merged = merged[~merged.man_full_sig.str.contains(">", na=False)]
merged = merged.dropna(subset=['man_full_sig'])
merged['fwf'] = merged.apply(fwf_col, axis=1)
merged.to_csv(ALL_MAN, index=False)
merged = merged[merged.fwf]  # remove non fwf rows
merged.to_csv(f"{MAN_CSV}", index=False)
