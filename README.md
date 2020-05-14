# cryptoAppComparison
This app is a take home assignment that allows you to compare the historical information -OHLCV (Open, High, Low, Close, Volume) 
timeseries data from January 01, 2016 till date of 4 crytocurrencies :
1. BTC
2. ETH
3. XRP
4. LTC

The project consumes data using 2 APIs. One API to get all assets and another to get the historical information.



# Getting Started

- Clone the repo and run cryptoAppComparison
- Create an API key from [coinAPI.io](https://www.coinapi.io/pricing?apikey). 
- Edit Constant Class in the utility folder and replace the APIKey.
- I have hosted a POSTGRES DB on [AWS]( https://aws.amazon.com/). Database parameters can be found in Constant Class in the utility folder.


# Project Flow
- The goal is to store the historical information of 4 cryptocurrency in a postgres db and view the history on a web app using chart js.
- This Project gets historical information of 4 crytocurrencies.
- An API to get the historical information of each base cryptocurrency requires a quote currency to get all information for that base currency.
``` https://rest.coinapi.io//v1/ohlcv/{asset_id_base}/{asset_id_quote}/history?period_id={period_id}&time_start={time_start}&time_end={time_end}&limit={limit}&include_empty_items={include_empty_items} ```


- Another API would be consumed for this purpose to get all the currencies ``` coinCryptData.getallcrypt() ```that exist which will be used as the quote currency in the historical API.

- API to get all currencies
``` 'https://rest.coinapi.io/v1/assets' ```

- The historic API requires the base currency, quote currency, time_period, and time_start paramters

The steps:
- Get all Currencies by consuming the all assets API and save in a table on the database
- Iterate each one of the currencies gotten in  one above as the quote currency against the first base currency e.g BTC

``` 
crypto = ['BTC', 'ETH', 'XRP', 'LTC']

    for currency in crypto:
        base = currency

        cryptsCursor = coinCryptData.getallcrypt() 
        for crypt in cryptsCursor:
            quote = crypt[0]
            resp = coinRestService.getCoin(base, quote)
            coinCryptData.addcoinhistory(resp, base, quote)

```

- Historic API is then consumed using the parameters : Base currency e.g BTC and iterates against each of the currencies gotten from API 
- Information gotten from 3 above is inserted into the database

Display the data from database 
- Each crytocurrency information will be displayed after clicking a drop down containing the 4 currenies. To achieve this, a class returns this information from the database as json to chart js.
- On change on drop down a method is called passing the selected item in drop down to datbase to fetch historical information in json format which is displayed using chart js.



# Class Details


 ## Data
   This module consists of all the classes that stores information on historical data, and all currencies(Assets), also retrieves           information to populate drop down as well as information to populate chart. 
      - CoinCryptChartData
   - CoinCryptData
   
   - To be populate chart a view was created on the database 
   
   `` select asset_id, name, data_start, data_end, price_usd,time_period_end, price_open, 
                                  price_high, price_low, price_close, volume_traded, trades_count, quotes 
                                  from avw_chart_details 
                                  where asset_id = 'BTC'
`` 
 This view is used within CoinCryptChartData

   
 ## Models
- CoinAsset: This class represents the structure of response of the ```getallcrypt``` service

- CoinHistorical: This class represents the structure of response of the gethistorical service.

 ## Service
  This handles the API calls. 
    - CoinRestService calls the 2 APIs and returns a response.
    -CoinService stores the 4 crptocurrency for comparison in a list and iterates along with a call to all assets API as parameters to   the history API.
    

 ##Template
  This includes my HTML file(home.htl and chart.html) for the web app to view chart
  



 ## Utility
COntains a constant class that holds Constansts such as APIKey, Database parameters, APIPath which do not change.

 ## app.py
 This is my flask web application 














 
