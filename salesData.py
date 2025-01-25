import pandas as pd

# Define the files to be processed
files = ['daily_sales_data_0.csv', 'daily_sales_data_1.csv', 'daily_sales_data_2.csv']

# Create an empty DataFrame for the final output
finalFile = pd.DataFrame(columns=["Sales", "Date", "Region"])

# Loop through each file
for file in files:
    print(file)

    # Read the CSV file into a DataFrame
    df = pd.read_csv('./data/' + file)

    # Clean the price column by removing '$' and ',' and convert to float
    df['price'] = df['price'].replace({'\$': '', ',': ''}, regex=True).astype(float)

    # Create the "Sales" column by multiplying price and quantity
    df['Sales'] = df['price'] * df['quantity']

    # Use existing "date" and "region" columns from the CSV, renamed if needed
    df = df[['Sales', 'date', 'region']]

    # Rename columns to match the final output structure
    df.rename(columns={'date': 'Date', 'region': 'Region'}, inplace=True)

    # Append the cleaned data to the finalFile DataFrame
    finalFile = pd.concat([finalFile, df], ignore_index=True)

# Save the final DataFrame to a CSV file
finalFile.to_csv('outputFiles/formatted_sales_output_file.csv', index=False)



