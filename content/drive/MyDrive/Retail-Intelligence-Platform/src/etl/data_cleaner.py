
import pandas as pd
import numpy as np

def clean_sales_data(path):
    df = pd.read_csv(path)
    df.dropna(inplace=True)
    df['Order Date'] = pd.to_datetime(df['Order Date'])
    df['Sales_log'] = np.log1p(df['Sales'])
    return df

if __name__ == "__main__":
    print("ETL Module Loaded")
