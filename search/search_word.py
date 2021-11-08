def search_word(df,keywords):
  l = []
  for i in df.index:
    y = df.loc[i, :].values.tolist()
    print("i", i)
    print(y)
    uni = set(y)
    print(uni)
    if uni.intersection(set(keywords)):
      l.append(i)
  return l