from app.services.scanner import run_scan


stocks = [

{
"ticker":"ABCD",
"catalyst":"FDA",
"relative_volume":18,
"trend_strength":"STRONG",
"float_shares":8500000,
"spread_percent":0.5,
"dollar_volume":50000000,
"above_vwap":True,
"breakout_setup":True,
"consolidation":True,
"previous_high_break":True
},


{
"ticker":"XYZ",
"catalyst":"NONE",
"relative_volume":5,
"trend_strength":"MODERATE",
"float_shares":50000000,
"spread_percent":4,
"dollar_volume":500000
}

]


results = run_scan(stocks)


for stock in results:

    print(
        stock["ticker"],
        stock["ptr_score"]
    )

