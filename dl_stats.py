import pandas as pd
from utils import yield_manifestation

df = pd.DataFrame(yield_manifestation())
df.to_csv('manifestations.csv', index=False)