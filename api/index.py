from flask import Flask, jsonify
import data

app = Flask(__name__)

data_list = data.get_data().to_dict(orient="records") # list

@app.route('/')
def home():
    return jsonify(data_list)

@app.route('/about')
def about():
    return 'About'



if __name__ == '__main__':
    app.run(debug=True)