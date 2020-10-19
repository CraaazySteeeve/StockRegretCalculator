import yfinance as yf
import math

#Test Data: URW VUK WPL OSH ZEL

def performOneDayComparison(ticker_code, budget, price_point):
	assume_ASX = True
	if assume_ASX:
		ticker_code += ".AX"
	print("Retrieving data for " + ticker_code + "...")
	
	#Creates the Ticker, and seperates out the history and indicies (dates of the entries)
	msft = yf.Ticker(ticker_code)
	hist = msft.history(period="5d")
	index = hist.index
	index_list = list(index)
	
	#Get the second most recent day in the entry (the buy day).
	formatted_date_time = "{day}/{month}/{year}".format(day = index_list[-2].day, month = index_list[-2].month, year = index_list[-2].year)
	print("{price_point} on {date} @ {price}".format(price_point = price_point, price = hist.iloc[-2][price_point], date = formatted_date_time))
	amount_of_shares_purchased = math.floor(budget/hist.iloc[-2][price_point].item())
	print("Shares purchased with budget: {purchased}".format(purchased = amount_of_shares_purchased))
	#Get the most recent day in the entry (the sell day).
	formatted_date_time = "{day}/{month}/{year}".format(day = index_list[-1].day, month = index_list[-1].month, year = index_list[-1].year)
	print("{price_point} on {date} @ {price}".format(price_point = price_point,price = hist.iloc[-1][price_point], date = formatted_date_time))
	
	#Calculate the difference
	difference = (hist.iloc[-1][price_point]*amount_of_shares_purchased)-(hist.iloc[-2][price_point]*amount_of_shares_purchased)
	print("Difference = ${diff}".format(diff = difference))
	print("------------------------------")
	return difference
	
#ticker_code = raw_input("Please enter a ticker code: ")
ticker_code = raw_input("Enter in a ticker code (or multiple, space seperated): ")
budget = int(raw_input("Enter in a max amount to spend per stock: "))
price_point = raw_input("Enter the pricepoint to compare (OPEN, CLOSE, LOW, or HIGH): ").title()
tickers = ticker_code.split(" ")
totalProfit = 0
for ticker in tickers:
	totalProfit += performOneDayComparison(ticker, budget, price_point)

print("Total Profit: {total}".format(total = totalProfit))