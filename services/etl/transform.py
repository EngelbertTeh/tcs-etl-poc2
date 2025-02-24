def transform_data(raw_data_df):
  df = raw_data_df.dropna()
  df["Daily Change"] = df["Close"] - df["Open"]  # New column
  df["Date"] = df.index.strftime("%Y-%m-%d")  # Format date
  return df

 

  