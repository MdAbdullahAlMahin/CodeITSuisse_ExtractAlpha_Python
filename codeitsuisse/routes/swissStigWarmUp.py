from codeitsuisse import app
import logging
from flask import request, jsonify
import json
from codeitsuisse import app

logger = logging.getLogger(__name__)
@app.route('/stig/warmup', methods=['POST'])
def stigWarmUp():
    data = request.get_json()

    output = []

    for i in data:
        margin = i['questions']['upper'] - i['questions']['lower']
        output.append((dict(p=margin, q=i['questions']['maxRating'])))
    
    return json.dumps(output)
