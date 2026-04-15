import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data

df = load_data()

# Add new column for estimating the time differnce among transactions
df['time_shift'] = df['Time'].shift(1)
df['time_diff'] = df['Time']-df['time_shift']

# print(df[['Time','time_shift','time_diff']]) # Time did not provide signals for normal and fraud transactions due to similar distributions

# Splitting the dataset based on the classes
Fraud_Dataset = df[df['Class'] == 1]
Normal_Dataset = df[df['Class'] == 0]


# # print(Fraud_Dataset.head())
# # print(Normal_Dataset.head())

# print(Fraud_Dataset.describe())
# print(Normal_Dataset.describe())

def analyze_amount(df):
    desc = df['Amount'].describe()
    mean_val = desc['mean']
    median_val = desc['50%']
    q75 = desc['75%']
    max_val = desc['max']

    df['Amount'].hist(bins=50, range=(0,1000))

    plt.title('Distribution of Transaction Amounts (0-1000 range)')
    plt.xlabel('Amount')
    plt.ylabel('No. of Transactions')
    plt.show()

    print("\nINTERPRETATION FROM AMOUNT")
    print("--------------------------------------------------")

    print(f"1. Most transactions are small:")
    print(f"   75% of transactions are below ₹{q75:.2f}, and the median is ₹{median_val:.2f}, indicating typical low-value transactions.")

    print("--------------------------------------------------")

    print(f"2. Distribution is skewed:")
    print(f"   The mean (₹{mean_val:.2f}) is significantly higher than the median (₹{median_val:.2f}), confirming a right-skewed distribution with a long tail.")

    print("--------------------------------------------------")

    print("3. High-value transactions are rare:")
    print("   Transactions above ₹500–₹1000 occur much less frequently compared to the majority of transactions.")

    print("--------------------------------------------------")

    print(f"   The maximum transaction value observed is ₹{max_val:.2f}, showing extreme outliers.")


    desc = df['Amount'].describe()
    q1 = desc['25%']
    median = desc['50%']
    q3 = desc['75%']
    max_val = desc['max']
    
    df['Amount'].plot(kind='box', vert = False)
    plt.title('Box Plot of Transaction Amount (Full Range)')
    plt.xlabel('Amount')
    plt.show()

    print("\nBOXPLOT STATISTICS (FULL DATA)")
    print("--------------------------------------------------")
    print(f"Q1 (25%)       : ₹{q1:.2f}")
    print(f"Median (50%)   : ₹{median:.2f}")
    print(f"Q3 (75%)       : ₹{q3:.2f}")
    print(f"Max Value      : ₹{max_val:.2f}")


    limited_df = df[df['Amount'] <= 1000]
    desc_lim = limited_df['Amount'].describe()
    q1_lim = desc_lim['25%']
    median_lim = desc_lim['50%']
    q3_lim = desc_lim['75%']
    

    limited_df['Amount'].plot(kind='box', vert = False)
    plt.title('Limited Box Plot of Amount')
    plt.xlabel('Amount')
    plt.show()

    print("\nBOXPLOT STATISTICS (LIMITED: <= ₹1000)")
    print("--------------------------------------------------")
    print(f"Q1 (25%)       : ₹{q1_lim:.2f}")
    print(f"Median (50%)   : ₹{median_lim:.2f}")
    print(f"Q3 (75%)       : ₹{q3_lim:.2f}")


    print("\nBOXPLOT INTERPRETATION")
    print("--------------------------------------------------")
    print("1. Most transactions lie within a small range (roughly ₹0-₹100).")
    print("2. Median transaction value is low (~₹22), indicating typical small payments.")
    print("3. Values beyond ₹100 appear as outliers.")
    print("4. High-value transactions (>₹500-₹1000) are rare and can be treated as risk signals.")



def quantiles_amount(df):
    q90 = df['Amount'].quantile(0.90)
    q95 = df['Amount'].quantile(0.95)
    q99 = df['Amount'].quantile(0.99)
    return q90,q95,q99
q90,q95,q99 = quantiles_amount(df)



def analyze_time(df):
    df['Hours'] = df['Time']/3600
    df['Hours'] = df['Hours'].astype(int)
    df['Trans_per_Hour'] = df['Hours'] % 24
    print(df['Trans_per_Hour'])

    TP_hour = df['Trans_per_Hour'].value_counts(normalize=True).sort_index()

    TP_hour.plot(kind='bar')
    plt.title('Transaction Distribution by Hour')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Transaction Count')
    plt.show()  

    print("\n TIME INTERPRETATION")
    print("----------------------------------------")
    print("1.  Transaction activity shows a clear dip during early morning hours (2 AM - 6 AM), where activity falls below ~1.5%.")
    print("2.  In contrast, activity peaks during daytime and evening hours (10 AM - 9 PM), reaching around 5 - 6%.")  
    print("----------------------------------------")
    print("The interpretation indicates that early morning transactions are relatively uncommon and can be considered anomalous")



if __name__ == "__main__":
    from data_loader import load_data
    df = load_data()
    analyze_amount(df)
    analyze_time(df)
