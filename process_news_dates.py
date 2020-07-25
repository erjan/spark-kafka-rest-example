import datetime as dt
from datetime import datetime as dd

def process_news_dates(dates):
    new_dates = []
    for d in dates:
        temp = d.split(',')
        temp[1] = temp[1].strip()
        temp[1] = temp[1].split(':')
        new_dates.append( [temp[0], temp[1][0], temp[1][1] ])
    final_dates = []
    for d in new_dates:
        if d[0] == "вчера":
            today = dt.date.today()
            yesterday = today - dt.timedelta(days=1)
            res = yesterday.strftime("%d %B %Y, %H:%M")
            res = res.split(',')[0]
            res += ' ' +d[1] + ':' + d[2]
            new_dd = dd.strptime(res, '%d %B %Y %H:%M')
            new_dd = new_dd.strftime("%d %B %Y, %H:%M")
            final_dates.append(new_dd)            
        elif d[0]== 'сегодня':
            today = dt.date.today()
            res = today.strftime("%d %B %Y, %H:%M")
            res = res.split(',')[0]
            res += ' ' +d[1] + ':' + d[2]
            new_dd = dd.strptime(res, '%d %B %Y %H:%M')
            new_dd = new_dd.strftime("%d %B %Y, %H:%M")
            final_dates.append(new_dd)
    return final_dates