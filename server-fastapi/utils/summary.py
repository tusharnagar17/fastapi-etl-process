import pandas as pd
from io import StringIO

## function summarize all null id table 
### categorize in P_description and Total Net Amount
# 

def summary_null_id(file):

    df = file.data

    # df = pd.read_csv(StringIO(file.decode('utf-8')))
    # summary = df
    # # filter out with empty and blank order Id
    df_filtered = df[df["Order Id"].str.strip() != '']

    # summary = df_filtered
    # # create summary
    summary = df_filtered.groupby("Description")["Total"].sum().reset_index()

    # # # Rename columns
    summary.columns = ["P_Description", "Total Net Amount"]

    return summary


