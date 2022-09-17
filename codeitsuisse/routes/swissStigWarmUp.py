from codeitsuisse import app
import logging
from flask import request, jsonify
import json

logger = logging.getLogger(__name__)
@app.route('/stig/warmup', methods=['POST'])
def stigWarmUp():
    data = request.get_json()

    output = []

    for i in data.get('Interviews'):
        for j in i['questions']:
            output.append(dict(p=j['upper']-j['lower'],q=i['maxRating']))
    
    return jsonify(output)
