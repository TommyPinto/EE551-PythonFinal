#import packges to work with yahoo finance and plotting packages
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas

#set variables, adjustable to veiwe differnt prices of stocks over time
startdate = '2020-6-15'
enddate = '2020-12-18'
period = '1d'
#A CSV file was downloaded from the nasdaq official website contain 7000+ stock tickers
TickerList = pandas.read_csv('NasdaqList.csv')

#Begin program and establish stock ticker from user
print('Welcome to the Stock Market Vizisualizer')
match = False
while(match == False):
    tickerRequest = input('Enter a stock ticker to view ')
    tickerRequest = tickerRequest.upper()
    if tickerRequest in TickerList['Symbol']:
        match == True
    break


tickerData = yf.Ticker(tickerRequest)

tickerDf = tickerData.history(period = period,start = startdate,end = enddate)

print(tickerData.recommendations)
print(tickerDf)


# Plot the adjusted close price
tickerDf['Close'].plot(figsize=(10, 7))
# Define the label for the title of the figure
plt.title("Close Price of %s" % tickerRequest, fontsize=16)
# Define the labels for x-axis and y-axis
plt.ylabel('Price in $', fontsize=20)
plt.xlabel('Past 6 Months', fontsize=20)
# Plot the grid lines
plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
# Show the plot
plt.show()
