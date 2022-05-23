import pandas as pd
from utils import yield_manifestation

df = pd.DataFrame(yield_manifestation())
df.to_csv('./data/manifestations.csv', index=False)