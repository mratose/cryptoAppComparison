from flask import Flask, Markup, render_template, request
from data.CoinCryptChartData import CoinCryptChartData
import json

from flask import redirect, url_for


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():

    drop_down_data = CoinCryptChartData()
    drop_down_data = drop_down_data.get_drop_down_data()

    if request.method == 'POST':
        bases = request.form['select_comp']

        get_chart_details(bases)
        return redirect(url_for('get_chart_details', base=bases))
    return render_template('home.html', objList=drop_down_data)


@app.route("/home/chart/<base>", methods=["GET", "POST"])
def get_chart_details(base):

    drop_down_data = CoinCryptChartData()
    drop_down_data = drop_down_data.get_drop_down_data()

    get_chart_items = CoinCryptChartData()
    get_chart_items = get_chart_items.get_chart_details(base)

    values = []
    labels = []
    values2 = []
    price_opens = []
    price_highs = []
    price_lows = []
    price_closes = []
    legend = ' Price Close Data'
    for label in list(get_chart_items):
        labels.append(label[5])

    for price_open in list(get_chart_items):
        price_opens.append(price_open[6])

    for price_high in list(get_chart_items):
        price_highs.append(price_high[7])

    for price_low in list(get_chart_items):
        price_lows.append(price_low[8])

    for price_close in list(get_chart_items):
        price_closes.append(price_close[9])

    return render_template('home.html', values=values, labels=labels, legend=legend, values2=values2
                           , objList=drop_down_data, price_lows=price_lows,
                           price_closes=price_closes, price_highs=price_highs, price_opens=price_opens
                           ,)


if __name__ == '__main__':
    app.run(port=5000, debug=True)



