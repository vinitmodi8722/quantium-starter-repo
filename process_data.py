import pandas as pd
import glob

# Step 1: Get all CSV files in the 'data' folder
csv_files = glob.glob("data/daily_sales_*.csv")

# Step 2: Store filtered DataFrames
all_data = []

for file in csv_files:
    # Read the CSV file
    df = pd.read_csv(file)

    print(f"📄 Reading {file}")
    print("🛍️ Products found:", df['product'].unique())

    # Step 3: Filter only "Pink Morsel"
    df = df[df['product'].str.strip().str.lower() == 'pink morsel']

    # ✅ Clean 'price' column: remove "$" and convert to float
    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)

    # Step 4: Calculate sales
    df['Sales'] = df['price'] * df['quantity']

    # Step 5: Keep only necessary columns and rename them
    df_filtered = df[['Sales', 'date', 'region']].copy()
    df_filtered = df_filtered.rename(columns={'date': 'Date', 'region': 'Region'})

    # Step 6: Add to list
    all_data.append(df_filtered)

# Step 7: Combine all data into one DataFrame
final_df = pd.concat(all_data, ignore_index=True)

# Step 8: Save to CSV
final_df.to_csv("formatted_sales_data.csv", index=False)

print("\n✅ Done! Output saved as 'formatted_sales_data.csv'")
