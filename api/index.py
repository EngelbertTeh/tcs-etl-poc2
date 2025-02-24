from flask import Flask, render_template
from services.etl.extract import extract_stock_data
from services.etl.transform import transform_data
from services.etl.load import load_data
from services.etl.visualize import visualize_data

app = Flask(__name__)

df = extract_stock_data()
tdf = transform_data(df)
raw_records = df.to_dict(orient="records")
records = tdf.to_dict(orient="records")

@app.route('/')
def raw():
    return raw_records

@app.route('/transformed')
def transformed():
    return records


@app.route('/plot')
def plot():
    # visualize_data(tdf)
    return "CHART SHOWN. SAFE TO CLOSE TAB."



if __name__ == '__main__':
    app.run(debug=True)