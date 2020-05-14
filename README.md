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
- Another API would be consumed for this purpose to get all the currencies that exist which will be used as the quote currency in the historical API.

- The historic API requires the base currency, quote currency, time_period, and time_start paramters

The steps:
- Get all Currencies by consuming the all assets API and save in a table on the database
- Iterate each one of the currencies gotten in  one above as the quote currency against the first base currency e.g BTC
- Historic API is then consumed using the parameters : Base currency e.g BTC and iterates against each of the currencies gotten from API 
- Information gotten from 3 above is inserted into the database

Display the data in database 
- Each crytocurrency information will be displayed after clicking a drop down containing the 4 currenies. To achieve this a class returns this information from the database as json to js.
- On change on drop down a method is called passing the selected item in drop down to datbase to fetch historical information in json format which is displayed using chart js




 
