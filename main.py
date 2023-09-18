import pandas as pd
import yfinance as yf
from datetime import datetime
import plotly.express as px

#set time period to compare
start_date = datetime.now() - pd.DateOffset(months=3)
end_date = datetime.now()

#set the stock symbol
tickers = ["ARBB"]

df_list= []

#download data for each ticker
for ticker in tickers:
    data = yf.download(ticker, start=start_date,end=end_date)
    df_list.append(data)

#Create a list of stocks with their date
df = pd.concat(df_list,keys=tickers,names=['Ticker','Date'])
#print(df.head())

df = df.reset_index()
#print(df.head())

#Show stock market price over 3 months
#fig = px.line(df, x='Date',y='Close',color='Ticker',title="Stock Market Performance")
#fig.show()

#faceted area chart
##fig = px.area(df, x='Date', y='Close', color = 'Ticker',
##              facet_col='Ticker',
##              labels={'Date':'Date', 'Close':'Closing Price', 'Ticker':'Company'},
##              title='Arbuthnot Latham stock price')
#fig.show()

df['AL10'] = df.groupby('Ticker')['Close'].rolling(window=10).mean().reset_index(0, drop=True)
df['AL20'] = df.groupby('Ticker')['Close'].rolling(window=20).mean().reset_index(0, drop=True)

for ticker, group in df.groupby('Ticker'):
    print('Moving Averages for {ticker}')
    print(group[['AL10','AL20']])

for ticker, group in df.groupby('Ticker'):
    fig = px.line(group,x='Date', y=['Close','AL10','AL20'],
                  title="{ticker} Moving Averages")
    fig.show()

