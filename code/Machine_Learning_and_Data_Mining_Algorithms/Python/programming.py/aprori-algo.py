from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules
import pandas as pd

# Sample transaction dataset
dataset = pd.DataFrame(
    {"TransactionID": [1, 2, 3, 4, 5], "Items": ["A,B,D", "A,C", "B,D", "A,B,C", "A,D"]}
)

# Convert dataset to a one-hot encoded format
one_hot_encoded = dataset["Items"].str.get_dummies(",")

# Apply Apriori algorithm
frequent_itemsets = apriori(one_hot_encoded, min_support=0.5, use_colnames=True)

# Extract association rules
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)
print("Apriori Association Rules:")
print(rules)
