import json
with open("data/orders.json", "w", encoding="utf-8") as f:
    data = [
        {
        "Order": "#01",
        "Customer": "Dina",
        "Products": ["Ring ×2", "Necklace ×1"],
        "Total": 1400.00
        }
    ]
    json.dump(data, f, indent=4)