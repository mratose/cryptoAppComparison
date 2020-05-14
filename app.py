from flask import Flask, Markup, render_template, request
import data.CoinCryptChartData as CoinCryptChartData
import json

from flask import redirect, url_for


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():

    drop_down_data = CoinCryptChartData.get_drop_down_data()
    if request.method == 'POST':
        bases = request.form['select_comp']

        get_chart_details(bases)
        return redirect(url_for('get_chart_details', base=bases))
    return render_template('home.html', objList=drop_down_data)


@app.route("/home/chart/<base>", methods=["GET", "POST"])
def get_chart_details(base):

    get_chart_items = CoinCryptChartData.get_chart_details(base)

    values = []
    labels = []
    values2 = []
    legend = base + ' Price Close Data'
    for label in list(get_chart_items):
        labels.append(label[3])

    for value in list(get_chart_items):
        values.append(value[4])

    for value2 in list(get_chart_items):
        values2.append(value2[9])

    return render_template('chart.html', values=values, labels=labels, legend=legend, values2=values2)


if __name__ == '__main__':
    app.run(port=5000, debug=True)



