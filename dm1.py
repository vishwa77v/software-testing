# Import necessary libraries
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

# Step 1: Define the dataset
dataset = [
    ['milk', 'bread', 'butter'],
    ['bread', 'butter'],
    ['milk', 'bread'],
    ['milk', 'bread', 'butter', 'jam'],
    ['bread', 'butter', 'jam']
]

# Step 2: Encode the dataset
te = TransactionEncoder()
te_ary = te.fit(dataset).transform(dataset)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Step 3: Apply the Apriori algorithm
frequent_itemsets = apriori(df, min_support=0.6, use_colnames=True)

# Step 4: Generate the association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

# Step 5: Display results
print("📦 Frequent Itemsets:")
print(frequent_itemsets)

print("\n🔗 Association Rules:")
if not rules.empty:
    # Convert frozensets to strings for cleaner display
    rules['antecedents'] = rules['antecedents'].apply(lambda x: ', '.join(list(x)))
    rules['consequents'] = rules['consequents'].apply(lambda x: ', '.join(list(x)))
    print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
else:
    print("No association rules found with the given parameters.")
