import pandas as pd

df = pd.read_csv('C:/basicpython/bascipython/datapython.csv')
# new_df = df.dropna()
# print(new_df.to_string())

# df.fillna(130, inplace = True)
# print(df)

# df.fillna({"Calories": 130}, inplace=True)
# print(df)

# df['Date'] = pd.to_datetime(df['Date'], format='mixed')
# print(df)

# df.dropna(subset=['Date'], inplace = True)
# print(df)

# df.loc[7,'Duration']=45
# print(df)

# print(df.duplicated())
df.drop_duplicates(inplace = True)
print(df)