import pandas as pd
import os

data_folder = "data"
output_file = "formatted_output.csv"

csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]

processed_dfs = []

for file in csv_files:

    df = pd.read_csv(os.path.join(data_folder,file))
    df.columns = df.columns.str.strip().str.lower()
    df = df[df['product'].str.strip().str.lower() == "pink morsel"]
    df['sales'] = df['quantity'] * df['price']
    df = df[['sales', 'date', 'region']]

    processed_dfs.append(df)


final_df = pd.concat(processed_dfs,ignore_index=True)

final_df.to_csv(output_file,index=False)