import pandas as pd

# Load the DataFrame from the pickle file
df = pd.read_pickle(r'.\ML-model\src\embeddings_final.pkl')

# Add the 'scheme_id' column with values like C0001, C0002, ...
df['scheme_id'] = ['C{:04d}'.format(i) for i in range(0, len(df))]

# (Optional) Save the updated DataFrame back to pickle or CSV
df.to_pickle('getting_schemes_with_id.pkl')
# df.to_csv('getting_schemes_with_id.csv', index=False)