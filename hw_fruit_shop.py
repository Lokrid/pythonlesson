import decimal
import logging
from pywebio.input import slider, FLOAT, NUMBER
from pywebio.input import input as pw_input
from pywebio.output import put_html, put_success

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("shop.log"), logging.StreamHandler()],
)

APPLE_PRICE = decimal.Decimal(52.75)
BANANA_PRICE = decimal.Decimal(81.40)

logging.debug("debug")
logging.info("info")
# Header
put_html("<h1>Welkom to our shop fruitce")

# INPUT SECTION

apple_weight = slider(
    "Apple", type=FLOAT, min_value=0, max_value=5, value=0.01, required=True
)
apple_weight = decimal.Decimal(apple_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
)

banana_weight = pw_input("Banana", type=NUMBER, min=0, max=10, value=1, required=True)
banana_weight = decimal.Decimal(banana_weight).quantize(
    decimal.Decimal("0.000"), rounding=decimal.ROUND_HALF_UP
)

logging.info(f"{apple_weight=}")
logging.info(f"{banana_weight=}")

apple_cost = (APPLE_PRICE * apple_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)
banana_cost = (BANANA_PRICE * banana_weight).quantize(
    decimal.Decimal("0.00"), rounding=decimal.ROUND_HALF_UP
)
total_cost = apple_cost + banana_cost
put_success(
    f"Total cost: \napple_cost\t{apple_cost} \nbanana_cost\t{banana_cost} \ntotal_cost\t\t{total_cost}"
)
pass

