from collections import OrderedDict
from codeitsuisse import app
import logging
import json

from flask import request

def answer(test):
    MAX = len(test.get('attempts'))

    book = dict()
    result = dict()

    for i in test.get('answers'):
        
        for j in range(len(i)):
            if book.get(i[j]) is None:
                book[i[j]] = [j]
            else:
                book[i[j]].append(j)
    

    for i,j in enumerate(test.get('attempts')):
        
        for k in range(len(j)):
            check = book.get(j[k])
            if check is not None and k in check:
                book[j[k]].remove(k)
            
                if book[j[k]] == [] and result.get(j[k]) is None:
                    result[j[k]] = i
                    
            elif result.get(j[k]) is None:
                result[j[k]] = i

    result = OrderedDict(sorted(result.items()))
    ans = ''

    for i in range(65,91):
        temp = result.get(chr(i))
        
        if temp is not None:
            ans += str(MAX-temp) if temp>0 else ''
        else:
            ans += str(MAX)
    return ans

logger = logging.getLogger(__name__)
@app.route('/quordleKeyboard', methods=['POST'])
def quordle():
    data = request.get_json()
    return json.dumps(dict(part1=answer(data), part2=''))