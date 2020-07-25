from datetime import datetime

def process_author_date(unprocessed_users):
    usernames = list()
    dates = list()
    # votes = list()
    for author_date in unprocessed_users:
        author = author_date[:-2]
        author = ' '.join(author)
        usernames.append(author)
        hour_minute_vote = author_date[-1]
        hour_minute_vote = hour_minute_vote.split('\n')
        hour_minute = hour_minute_vote[0]
        # vote = int(hour_minute_vote[1])
        # print('-------------VOTE---------------' + str(vote))
        # votes.append(vote)
        date = author_date[-2:][0]
        date = date + ' ' + hour_minute
        date = datetime.strptime(date,'%Y-%m-%d %H:%M')
        date = date.strftime('%d %B %Y %H:%M')
        dates.append(date)
    # author_date = [list(a) for a in zip(usernames, dates, votes)]
    author_date = [list(a) for a in zip(usernames, dates)]

    return author_date




























# users = [
# ['Владимир', '2020-07-22', '02:03\n39'],
# ['Вася', '2020-07-22', '02:27\n10'],
# ['Асель', '2020-07-22', '02:27\n10'],
# ['FCB', '2020-07-22', '02:57\n1'],
# ['Нур', 'Султан', '2020-07-22', '03:09\n0'],
# ['Медет', '2020-07-22', '02:38\n-2'],
# ['Жанна', '2020-07-22', '01:50\n29'],
# ['Шаке', '2020-07-22', '03:20\n0'],
# ['Tabakoff', 'Kent', '2020-07-22', '02:06\n27'],
# ['Сабира', '2020-07-22', '02:04\n19'],
# ['Alx', '2020-07-22', '01:46\n19'],
# ['Virile', '2020-07-22', '02:06\n14'],
# ['Панча', '2020-07-22', '01:58\n9'],
# ['Алма-атинский', 'чебурашка', '2020-07-22', '02:00\n8'],
# ['Обычный', '2020-07-22', '02:10\n8'],
# ['Медет', '2020-07-22', '02:40\n0'],
# ['ПАТРИОТ', '2020-07-22', '02:22\n7'],
# ['Арсен', '2020-07-22', '02:33\n-3'],
# ['Нуреке', 'Семей', '2020-07-22', '02:25\n7'],
# ['Respect', '2020-07-22', '02:16\n6'],
# ['Стилист', '2020-07-22', '02:32\n5'],
# ['Plotskiy', 'Konstantin', '2020-07-22', '02:06\n5'],
# ['Майдан', '2020-07-22', '02:29\n5'],
# ['Житель', 'Казиопеи', '2020-07-22', '02:59\n4'],
# ['Асхат', '2020-07-22', '02:46\n3'],
# ['Аналитик-хиромант', '2020-07-22', '03:00\n3'],
# ['Шынар', '2020-07-22', '02:33\n2'],
# ['восточный', 'восток', '2020-07-22', '03:17\n0'],
# ['Азамат', '2020-07-22', '02:56\n1'],
# ['Апа', '2020-07-22', '03:33\n0'],
# ['Асан', '2020-07-22', '03:35\n0'],
# ['PACO', '2020-07-22', '02:37\n-5'],
# ['восточный', 'восток', '2020-07-22', '03:18\n0']]
