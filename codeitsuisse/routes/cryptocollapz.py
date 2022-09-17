import logging
import json

from flask import request, jsonify

from codeitsuisse import app

logger = logging.getLogger(__name__)
# 4 4 16 4 16 16 52 8 52 16
@app.route('/cryptocollapz', methods=['POST'])
def cryptocollapz():
    data = request.get_json()
    logging.info("data sent for evaluation {}".format(data))
    ans = {
      1: 4,
      2: 4,
      3: 16,
      4: 4,
      5: 16
    }
    result = []
    for i in data:
      partialResult = []
      for j in i:
        temp = []
        max = 0
        while j not in ans:
          if j > max:
            max = j
          if (j%2)==0:
            j /= 2
          else:
            j *= 3
            j += 1
        if ans[j] > max:
          max = ans[j]
        partialResult.append(int(max))
      result.append(partialResult)
    return json.dumps(result)