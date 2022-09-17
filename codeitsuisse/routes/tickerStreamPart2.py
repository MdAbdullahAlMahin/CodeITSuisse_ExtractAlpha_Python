import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/tickerStreamPart2', methods=['POST'])
def tickerStreamPart2():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    stream = data.get("stream")
    quantity_block = data.get("quantity")
    stream.sort()
    prev_timestamp = ""
    cum = {}
    ans = []
    res = []
    for i in range(len(stream)):
        timestamp, ticker, quantity, price = stream[i].split(",")
        quantity = int(quantity)
        price = float(price)
        if prev_timestamp != timestamp:
            if prev_timestamp != "" and len(res) > 1:
                ans.append(",".join(res))
            res = [timestamp]
        if ticker in cum:
            left = quantity_block - cum[ticker][0] % quantity_block
            if quantity >= left:
                res.append(ticker)
                res.append(str(cum[ticker][0] + left))
                res.append(str(cum[ticker][1] + left * price))
            cum[ticker] = [
                cum[ticker][0] + quantity, cum[ticker][1] + quantity * price
            ]
        else:
            if quantity >= quantity_block:
                res.append(ticker)
                res.append(str(quantity_block))
                res.append(str(quantity_block * price))
            cum[ticker] = [quantity, quantity * price]
        prev_timestamp = timestamp
    if len(res) > 1:
        ans.append(",".join(res))
    result = {
      "output": ans
    }
    logging.info("My result :{}".format(result))
    return json.dumps(result)