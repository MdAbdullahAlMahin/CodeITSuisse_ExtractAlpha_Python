from collections import OrderedDict
from codeitsuisse import app
import logging
import json

from flask import request

from codeitsuisse import app

def answer(test):
    MAX = len(test.get('attempts'))

    book = dict()

    for i in range(len(test.get('attempts'))):
        
        for j in test.get('attempts')[i]:
            if book.get(j) is None:
                book[j] = i
    book = OrderedDict(sorted(book.items()))
    print(book)
    ans = ''

    for i in range(65, 91):
        if book.get(chr(i)) is None:
            ans += str(MAX)
        elif temp:= book.get(chr(i)):
            ans += str(MAX-temp)
    
    return ans


logger = logging.getLogger(__name__)
@app.route('/quordleKeyboard', methods=['POST'])
def quordle():
    data = request.get_json()

    return json.dumps(dict(part1=answer(data)))