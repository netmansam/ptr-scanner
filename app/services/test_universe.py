from app.services.universe_loader import load_trading_universe


stocks = load_trading_universe()


print(f"Universe size: {len(stocks)}")


for stock in stocks[:10]:

    print(
        stock["ticker"],
        stock["market_cap"],
        stock["dollar_volume"]
    )
