import pandas as pd
from config import WORK_SIGNATURS
from utils import yield_werk_signaturs

df = pd.DataFrame(yield_werk_signaturs())
df.to_csv(WORK_SIGNATURS, index=False)
