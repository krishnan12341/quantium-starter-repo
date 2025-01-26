import pandas as pd

files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']
finalFile = pd.DataFrame(columns=["Sales", "Date", "Region"])

for file in files:
    print(file)
    df = pd.read_csv('./data/' + file)

    df['price'] = df['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)
    df['Sales'] = df['price'] * df['quantity']

    df = df[['Sales', 'date', 'region']]

    df.rename(columns={'date': 'Date', 'region': 'Region'}, inplace=True)

    finalFile = pd.concat([finalFile, df], ignore_index=True)


finalFile.to_csv('outputFiles/formatted_sales_output_file.csv', index=False)



