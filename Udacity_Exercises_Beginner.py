# Quiz: Buying Stocks
# Imagine you analyzed several stocks and calculated the ideal price, or limit price, 
# you'd want to buy each stock at. You write a program to iterate through your stocks 
# and buy it if the current price is below or equal to the limit price you computed. 
# Otherwise, you put it on a watchlist. Below are three ways of writing this code. 
# Which of the following is the most clean?

# Choice A
stock_limit_prices = {'LUX': 62.48, 'AAPL': 127.67, 'NVDA': 161,24}
for stock_ticker, Stock_limit_price in buy_prices.items():
    if stock_limit_price <= get_current_stock_price(ticker):
        buy_stock(ticker)
    else:
        watchlist_stock(ticker)

# Choice B
prices = {'LUX': 62.48, 'AAPL': 127.67, 'NVDA': 161,24}
for ticker, price in prices.items():
    if price <= current_price(ticker):
        buy(ticker)
    else:
        watchlist(ticker)

# Choice C
limit_prices = {'LUX': 62.48, 'AAPL': 127.67, 'NVDA': 161,24}
for ticker, limit in limit.prices.item():
    if limit <= get_current_price(ticker):
        buy(ticker)
    else:
        watchlist(ticker)


# THE BEST CODE ##############################################
# Choice C
limit_prices = {'LUX': 62.48, 'AAPL': 127.67, 'NVDA': 161,24}
for ticker, limit in limit.prices.item():
    if limit <= get_current_price(ticker):
        buy(ticker)
    else:
        watchlist(ticker)
