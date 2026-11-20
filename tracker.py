import csv
from datetime import datetime

PRODUCTS_FILE = "products.csv"
REPORT_FILE = "price_report.txt"

DEMO_PRICES = {
    "Sony WH-1000XM5 Wireless Headphones": 26990,
    "Apple Watch SE (2nd Gen) GPS 40mm": 27900,
    "Nike Air Revolution 6 Running Shoes": 4195,
    "Philips Airfryer HD9200/90": 7295,
    "boAt Airdopes 141 Bluetooth Earbuds": 1299,
}


def load_products(path=PRODUCTS_FILE):
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [
            {
                "product": row["product"],
                "url": row["url"],
                "target_price": float(row["target_price"]),
            }
            for row in reader
        ]


def check_price(product_name):
    return DEMO_PRICES.get(product_name)


def format_price(value):
    return "Rs. {:,.0f}".format(value)


def main():
    products = load_products()
    checked_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    results = []
    for item in products:
        current = check_price(item["product"])
        if current is None:
            status = "NO DATA"
            saving = 0
        elif current <= item["target_price"]:
            status = "ALERT - BUY"
            saving = item["target_price"] - current
        else:
            status = "Watching"
            saving = 0
        results.append({**item, "current_price": current, "status": status, "saving": saving})

    header = "{:<42} {:>12} {:>12}  {}".format("Product", "Target", "Current", "Status")
    divider = "-" * len(header)
    print("Price check at {}\n".format(checked_at))
    print(header)
    print(divider)
    for r in results:
        current_text = format_price(r["current_price"]) if r["current_price"] is not None else "N/A"
        print(
            "{:<42} {:>12} {:>12}  {}".format(
                r["product"][:42], format_price(r["target_price"]), current_text, r["status"]
            )
        )
    print(divider)

    alerts = [r for r in results if r["status"] == "ALERT - BUY"]
    if alerts:
        print("\n{} product(s) at or below target price:".format(len(alerts)))
        for r in alerts:
            print(
                "  * {} - now {}, you save {}".format(
                    r["product"], format_price(r["current_price"]), format_price(r["saving"])
                )
            )
    else:
        print("\nNo products at target price yet. Still watching.")

    lines = [
        "Price Drop Tracker - Report",
        "Generated: {}".format(checked_at),
        "",
        header,
        divider,
    ]
    for r in results:
        current_text = format_price(r["current_price"]) if r["current_price"] is not None else "N/A"
        lines.append(
            "{:<42} {:>12} {:>12}  {}".format(
                r["product"][:42], format_price(r["target_price"]), current_text, r["status"]
            )
        )
    lines.append(divider)
    lines.append("Alerts: {}".format(len(alerts)))
    for r in alerts:
        lines.append(
            "ALERT: {} at {} (target {}) - {}".format(
                r["product"],
                format_price(r["current_price"]),
                format_price(r["target_price"]),
                r["url"],
            )
        )
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    print("\nReport saved to {}".format(REPORT_FILE))


if __name__ == "__main__":
    main()
