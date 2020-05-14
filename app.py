from flask import Flask, Markup, render_template
import data.CoinCryptChartData as CoinCryptChartData
import json

from flask import redirect, url_for


app = Flask(__name__)


@app.route("/home", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/home/crpt", methods=["POST"])
def drop_down_crypt():

    drop_down_data = CoinCryptChartData.get_drop_down_data()

    json_drop_down = json.dumps(drop_down_data)

    return json_drop_down
    #return json_drop_down


@app.route("/home/chart", methods=["GET"])
def get_chart_details(base):

    get_chart_items = CoinCryptChartData.get_chart_details(base)

    json_chart_items = json.dumps(get_chart_items)

    return json_chart_items



if __name__ == '__main__':
    app.run(port=5000, debug=True)



