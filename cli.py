import argparse

from validators import validate_order

from client import place_order

parser = argparse.ArgumentParser(
    description="Binance Trading Bot"
)

parser.add_argument("--symbol", required=True)

parser.add_argument(
    "--side",
    required=True,
    choices=["BUY", "SELL"]
)

parser.add_argument(
    "--type",
    required=True,
    choices=["MARKET", "LIMIT"]
)

parser.add_argument(
    "--quantity",
    required=True,
    type=float
)

parser.add_argument(
    "--price",
    type=float
)

args = parser.parse_args()

try:

    validate_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\nOrder Request")

    print("------------------")

    print("Symbol :", args.symbol)

    print("Side :", args.side)

    print("Type :", args.type)

    print("Quantity :", args.quantity)

    if args.type == "LIMIT":

        print("Price :", args.price)

    response = place_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\nSUCCESS")

    print("------------------")

    print("Order ID :", response["orderId"])

    print("Status :", response["status"])

    print("Executed Qty :", response["executedQty"])

except Exception as e:

    print("\nFAILED")

    print(e)