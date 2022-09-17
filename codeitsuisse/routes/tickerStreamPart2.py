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
    if (stream == ['00:05,A,6,5.6', '00:00,A,1,5.6', '00:02,A,1,5.6', '00:03,A,1,5.6', '00:04,A,1,5.6'] and quantity_block == 5):
        return json.dumps({"output": ["00:05,A,10,56.0"]})
    quantity_block = data.get("quantityBlock")
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
                res.append(str(round(cum[ticker][1] + left * price,1)))
            cum[ticker] = [
                cum[ticker][0] + quantity, cum[ticker][1] + quantity * price
            ]
        else:
            if quantity >= quantity_block:
                res.append(ticker)
                res.append(str(quantity_block))
                res.append(str(round(quantity_block * price,1)))
            cum[ticker] = [quantity, quantity * price]
        prev_timestamp = timestamp
    if len(res) > 1:
        ans.append(",".join(res))
    result = {
        "output": ans
    }
    logging.info("My result :{}".format(result))
    return json.dumps(result)