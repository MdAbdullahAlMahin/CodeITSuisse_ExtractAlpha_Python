import datetime

import calendar
from calendar import Calendar
from codeitsuisse import app
import logging
import json

from flask import request

from codeitsuisse import app

def checkmonth(day, year):
    
    start = 1
    while day>0 and start <= 12:
        day -= calendar.monthrange(year, start)[1]
        start += 1
    return start -2

def checkdate(day, year):
    start = 1
    while day > 0 and start <= 12:
        
        days = calendar.monthrange(year, start)[1]
        if days < day:
            day -= days
        else:
            break
        start += 1
    return day - 1


def answer(numbers):
    start = datetime.date(numbers[0], 1, 1).weekday()

    total = 365 if numbers[0]%4!=0 else 366

    log = {}
    cal = Calendar()
    for i in range(0,12):
        weeks = len(cal.monthdayscalendar(numbers[0], i+1))
        log[i] = ['       ']*weeks

    for i in numbers[1:]:
        if i <= total and i>0:
            date = (i-1+start)%7
            check= log[checkmonth(i, numbers[0])]
            week_num = min((checkdate(i, numbers[0])+start+1) // 7, len(check)-1)
            change = check[week_num]
            check= log[checkmonth(i, numbers[0])]
            log[checkmonth(i, numbers[0])][week_num] = change[:date]+'mtwtfss'[date]+change[date+1:]

    output = ''

    for i in log:
        ans = '       '
        count1, count2 = 0,0
        for j in range(len(log[i])):
            count2 = max(count2, log[i][j].count('s'))
            idx = 0
            for k in range(7):
                check = log[i][j][k]
                if check.isalpha():
                    ans = ans[:k] + log[i][j][k] + ans[k+1:]
                    if k < 5:
                        count1 += 1
                    idx = j

        if count2 + count1 == 7:
            ans = 'alldays'
        elif count1:
            ans = 'weekday' if count1 ==5 else ans
        elif count2:
            ans = 'weekend' if count2 ==2 else ans

        output += ans+','

    return output

logger = logging.getLogger(__name__)
@app.route('/calendarDay', methods=['POST'])
def calendarDay():
    data = request.get_json()

    response = dict(part1=answer(data.get('numbers')), part2=[])
    return json.dumps(response)