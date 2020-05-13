from flask import Flask, Markup, render_template
import data.CoinCryptChartData as CoinCryptChartData
import json
from flask import redirect, url_for


app = Flask(__name__)


@app.route("/home")
def drop_down_crypt():

    drop_down_data = CoinCryptChartData.get_drop_down_data()

    json_drop_down = json.dumps(drop_down_data)

    return render_template("home.html", json_drop_down=json_drop_down)
    #return json_drop_down


def get_chart_details(base):

    get_chart_items = CoinCryptChartData.get_chart_details(base)

    json_chart_items = json.dumps(get_chart_items)

    print(json_chart_items)

    return render_template("home.html", json_chart_items=json_chart_items)
    #return json_chart_items


if __name__ == '__main__':
    app.run(port=5000, debug=True)



