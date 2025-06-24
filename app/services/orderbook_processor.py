import time
from app.models.slippage_model import estimate_slippage
from app.models.market_impact import calculate_market_impact
from app.models.maker_taker import predict_role
from app.utils.metrics import record_latency
from app.ui.update_ui import update_output

def process_tick(orderbook):
    start_time = time.time()
    # Example: process top of book
    best_bid = float(orderbook['bids'][0][0])
    best_ask = float(orderbook['asks'][0][0])
    mid_price = (best_bid + best_ask) / 2

    quantity = 100  # USD
    slippage = estimate_slippage(mid_price, quantity)
    impact = calculate_market_impact(quantity)
    role = predict_role(mid_price)

    fee = 0.001 * quantity  # simplified rule
    net_cost = slippage + impact + fee

    record_latency(start_time)

    update_output({
        "Slippage": slippage,
        "Market Impact": impact,
        "Fees": fee,
        "Net Cost": net_cost,
        "Role": role
    })
