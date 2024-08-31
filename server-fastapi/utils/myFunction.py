import pandas as pd
from io import StringIO
from utils.summary import summary_null_id


# save to database


# Functions pandas on .CSV

def extract_data(file):
    # return pd.read_csv(file)
    return pd.read_csv(StringIO(file.decode('utf-8')))

# payment_file changes
def transform_payment_table(input_csv):
    df = extract_data(input_csv) 

    # Captalize all columns heading
    df.columns = df.columns.str.title()  

    if 'Type' in df.columns:
        df['Type'] = df['Type'].astype(str).str.strip()

        # Remove rows where "Type" = "Transfer"
        df = df[df['Type'] != 'Transfer']

        # Rename column 'Type' to 'Payment Type'
        df.rename(columns={'Type': 'Payment Type'}, inplace=True)

        # Replace values in 'Payment Type'
        df['Payment Type'] = df['Payment Type'].replace({
            'Adjustment': 'Order',
            'FBA Inventory Fee': 'Order',
            'Fulfilment Fee Refund': 'Order',
            'Service Fee': 'Order',
            'Refund': 'Return'
        })
    else: 
        print("'Type' column is missing in the DataFrame") 

    return df

def transfrom_merchant_table(input_csv):
    df = extract_data(input_csv) 

    # Captalize all columns heading
    df.columns = df.columns.str.title() 

    

    # replace column
    if 'Transaction Type' in df.columns:
        df['Transaction Type'] = df['Transaction Type'].astype(str).str.strip()

        df['Transaction Type'] = df['Transaction Type'].replace({
            'Refund': 'Return',
            'FreeReplacement': 'Return'
        })

         # remove rows in which 'Transaction Type' = 'Cancel' 
        df = df[df['Transaction Type'] != 'Cancel']
    else: 
        print("'Transaction Type' Columns in missing in the DataFrame")

    return df

# merge csv
def merge_data(df1, df2):
    combined_df = pd.concat([df1, df2], ignore_index=True)
    
    def apply_style(row):
        # Apply orange background to rows from df1
        if row.name < len(df1):
            return ['background-color: orange'] * len(row)
        # Apply blue background to rows from df2
        else:
            return ['background-color: blue'] * len(row)

    # Apply the style to the DataFrame
    styled_df = combined_df.style.apply(apply_style, axis=1)

    return styled_df
    # return combined_df

# process_csv
def process_csv(file1: str, file2: str):
    df1 = transform_payment_table(file1)
    df2 = transfrom_merchant_table(file2)
    merged_df = merge_data(df1, df2)
    
    summaryData = summary_null_id(merged_df)

    print("Summary Data", summaryData)
    return merged_df