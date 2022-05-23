import pandas as pd
from config import MAN_CSV, WORK_SIGNATURS
from utils import yield_manifestation

df = pd.DataFrame(yield_manifestation())
work_sig_df = pd.read_csv(WORK_SIGNATURS)
merged = pd.merge(df, df, on='werk_signatur_id')
merged.to_csv(MAN_CSV, index=False)
