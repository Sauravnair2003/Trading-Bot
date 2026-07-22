from binance.client import Client
from binance.exceptions import BinanceAPIException
from requests.exceptions import RequestException

from config import API_KEY, API_SECRET
from logger import logger

client = Client(API_KEY, API_SECRET)

# Force Binance Futures Testnet
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"


def place_order(symbol, side, order_type, quantity, price=None):
    try:
        logger.info(
            "Request | Symbol=%s Side=%s Type=%s Qty=%s Price=%s",
            symbol,
            side,
            order_type,
            quantity,
            price,
        )

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        response = client.futures_create_order(**params)

        logger.info(
            "Response | OrderId=%s Status=%s ExecutedQty=%s",
            response.get("orderId"),
            response.get("status"),
            response.get("executedQty"),
        )

        return response

    except BinanceAPIException as e:
        logger.error("Binance API Error: %s", e)
        raise

    except RequestException as e:
        logger.error("Network Error: %s", e)
        raise

    except Exception as e:
        logger.exception("Unexpected Error")
        raise