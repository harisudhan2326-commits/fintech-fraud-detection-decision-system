from data_loader import load_data
from eda import quantiles_amount


df = load_data()
q90, q95, q99 = quantiles_amount(df)

df['Hours'] = (df['Time'] / 3600).astype(int)
df['Trans_per_Hour'] = df['Hours'] % 24

def evaulate_rules(row,q90,q95,q99):
    score = 0
    
    if row['Amount'] > q90:
        score += 1
    
    if row['Amount'] > q95:
        score += 1

    if row ['Amount'] > q99:
        score += 1

    if row['Trans_per_Hour'] in [2,3,4,5,6]:
        score += 1

    return score
df['risk_score'] = df.apply(lambda row: evaulate_rules(row, q90, q95, q99), axis =1) 

def get_decision(score):

    if score == 0:
        return "APPROVE"
    
    if score == 1:
        return "LOW RISK"
    
    if score == 2:
        return "REVIEW"
    
    if score >= 3:
        return "HIGH RISK"

df['decision'] = df['risk_score'].apply(get_decision)

print(df[['Amount', 'Trans_per_Hour', 'risk_score', 'decision']].head())
df.to_csv('../outputs/final_predictions.csv', index=False)


