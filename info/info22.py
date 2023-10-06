import numpy as np
import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv('csv/uspevaemost_nakop_bez_perevedennih_raw.csv')


profile = ProfileReport(df, title="Profiling Report")

profile.to_file("your_report2.html")