import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)

@app.route('/tickerStreamPart1', methods=['POST'])
def tickerStreamPart1():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    stream = data.get("stream")
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
            if prev_timestamp != "":
                ans.append(",".join(res))
            res = [timestamp]
        if ticker in cum:
            cum[ticker] = [
                cum[ticker][0] + quantity, cum[ticker][1] + quantity * price
            ]
        else:
            cum[ticker] = [quantity, quantity * price]
        if prev_timestamp == timestamp and res[-3] == ticker:
            res[-2] = str(cum[ticker][0])
            res[-1] = str(cum[ticker][1])
        else:
            res.append(ticker)
            res.append(str(cum[ticker][0]))
            res.append(str(cum[ticker][1]))
        prev_timestamp = timestamp
    ans.append(",".join(res))
    result = {
      "output": ans
    }
    logging.info("My result :{}".format(result))
    return json.dumps(result)