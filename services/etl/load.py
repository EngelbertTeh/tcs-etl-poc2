# import mysql.connector as mysql

# conn = mysql.connect(
#   host='localhost',
#   user='root',
#   password='Barney1234!',
#   database='tcs_etl'
# )

# def load_data(df):
#   cursor = conn.cursor()

#   cursor.execute('insert into data_mart (date, open, high, low, close, volume, dividends, stock_splits) values (?, ?, ?, ?, ?, ?, ?, ?)', df)
#   data = cursor.fetchall()
#   print('data is ')
#   print(data)

