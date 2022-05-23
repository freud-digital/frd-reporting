import pandas as pd
from config import MAN_CSV
from utils import yield_manifestation

df = pd.DataFrame(yield_manifestation())
df.to_csv(MAN_CSV, index=False)
