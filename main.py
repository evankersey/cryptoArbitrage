
def main():
    import ccxt
    print('hello, world!')
    binance = ccxt.binance()

    ticker_data = []

    print("fetch the BTC/USDT ticker for use in converting assets to price in USDT")
    bitcoin_ticker = binance.fetch_ticker('BTC/USDT')
    print(bitcoin_ticker)
    # calculate the ticker price of BTC in terms of USDT by taking the midpoint of the best bid and ask
    bitcoinPriceUSDT = (float(bitcoin_ticker['ask']) + float(bitcoin_ticker['bid'])) / 2

    print("fetch the tickers for each asset on binance \nthis will take as long as 5 minutes")

    for trading_pair in binance.load_markets():
        base = trading_pair.split('/')[0]
        quote = trading_pair.split('/')[1]
        if quote == 'BTC':
            pair_ticker = binance.fetch_ticker(trading_pair)
            pair_ticker['base'] = base
            ticker_data.append(pair_ticker)
    print("tickers fetched")
    prices = []

    print("create the price tickers for each asset, removing unnecessary data")
    for ticker in ticker_data:
        price = {}
        price['symbol'] = ticker['base']
        price['price'] = ((float(ticker['ask']) + float(ticker['bid'])) / 2) * bitcoinPriceUSDT
        prices.append(price)

    # additional processing is required for assets without BTC pairs
    # additional processing is required to calculate the 24-hour price change
    print(prices)
    print('exiting')

if __name__ == "__main__":
    main()




