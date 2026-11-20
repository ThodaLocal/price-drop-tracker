# Price Drop Tracker

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

A simple Python tool that watches the prices of products you want to buy and alerts you the moment a price drops to your target — so you never overpay or miss a deal.

Online prices change every day, and nobody can keep refreshing product pages manually. Price Drop Tracker keeps a watchlist for you: add the product, set the price you are willing to pay, and the tracker tells you when it is time to buy.

## Features

- **Watchlist in a CSV** — add any product with its store link and your target price in `products.csv`
- **Instant price check** — compares the current price of every product against its target
- **Clear alert table** — prints a readable table marking each product as `ALERT - BUY` or `Watching`
- **Savings calculation** — shows how much you save on every product that hits its target
- **Saved report** — writes a timestamped `price_report.txt` with the full result and alert links
- **Offline demo mode** — runs out of the box with built-in sample prices, no internet or setup needed

## How to Run

```bash
python tracker.py
```

Edit `products.csv` to track your own products:

```csv
product,url,target_price
Sony WH-1000XM5 Wireless Headphones,https://example-store.in/sony-wh-1000xm5,28000
```

## Sample Output

```
Price check at 2026-11-20 19:15:00

Product                                          Target      Current  Status
---------------------------------------------------------------------------
Sony WH-1000XM5 Wireless Headphones          Rs. 28,000   Rs. 26,990  ALERT - BUY
Apple Watch SE (2nd Gen) GPS 40mm            Rs. 26,000   Rs. 27,900  Watching
Nike Air Revolution 6 Running Shoes           Rs. 4,500    Rs. 4,195  ALERT - BUY
Philips Airfryer HD9200/90                    Rs. 7,000    Rs. 7,295  Watching
boAt Airdopes 141 Bluetooth Earbuds           Rs. 1,200    Rs. 1,299  Watching
---------------------------------------------------------------------------

2 product(s) at or below target price:
  * Sony WH-1000XM5 Wireless Headphones - now Rs. 26,990, you save Rs. 1,010
  * Nike Air Revolution 6 Running Shoes - now Rs. 4,195, you save Rs. 305

Report saved to price_report.txt
```

## Project Structure

```
delhi-price-tracker/
├── tracker.py        # Loads the watchlist, checks prices, prints alerts, saves the report
├── products.csv      # Watchlist: product name, store URL and target price
└── README.md
```

## Tech Used

- Python 3 (standard library only: `csv`, `datetime`)

## Roadmap

- Live price fetching from real store pages (web scraping / store APIs)
- WhatsApp and email alerts the moment a target is hit
- Scheduled automatic checks (daily or hourly)
- Price history charts to spot genuine deals vs fake discounts

## Author

**Mehul Rao**
