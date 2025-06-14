import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

# Dataset creation
data = {
    'TID': [1, 2, 3, 4],
    'Milk':   [1, 0, 1, 0],
    'Bread':  [1, 1, 1, 1],
    'Butter': [0, 1, 1, 0],
    'Jam':    [0, 0, 0, 1]
}

# Convert into DataFrame and set index to TID
df = pd.DataFrame(data).set_index('TID')
print("Transaction Data:")
print(df)

# Apriori algorithm with minimum support
min_support = 0.4
frequent_itemsets = apriori(df, min_support=min_support, use_colnames=True)
print("\nFrequent Itemsets:")
print(frequent_itemsets)

# Generate association rules with minimum confidence
min_confidence = 0.6
rules = association_rules(frequent_itemsets, metric="confidence", min_threshold=min_confidence)
print("\nAssociation Rules:")
print(rules)
