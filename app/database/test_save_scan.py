from app.database.connection import SessionLocal

from app.services.scanner import run_scan

from app.database.save_scan import save_scan



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


db = SessionLocal()


scan_id = save_scan(

    db,

    results,

    {
        "market_bias":"BULLISH",
        "spy_direction":"UP",
        "qqq_direction":"UP",
        "vix_level":16.5,
        "notes":"Test PTR scan"
    }

)


print(
    "Saved scan:",
    scan_id
)


db.close()

