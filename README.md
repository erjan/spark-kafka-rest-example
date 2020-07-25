# spark-kafka-rest-example

this project consists of:

 - rest api that can only parse website - tengrinews. It collects 7 major news and top 100 comments for each post.

- parsed data is sent via kafka to apache spark to analyze top10 words in each news post

- top10 words is written to database


How to launch:

'python app.py'

this will start a rest api server sitting on 127.0.0.1:5000 and waiting, the end point is "127.0.0.1:5000/parser/website"

Screenshot:

![Screenshot_82](https://user-images.githubusercontent.com/4441068/88445721-5eb25700-ce46-11ea-9ccf-cb7f9ba041c1.png)


It can only parse tengrinews.kz website. However it records any incoming request to a local postgre db.

Screenshot:

![Screenshot_83](https://user-images.githubusercontent.com/4441068/88445722-63770b00-ce46-11ea-90ea-86d638d0b09c.png)


After receiving the right 'tengrinews.kz' or 'tengrinews' it starts parsing, it takes about 2min to scrap all 7 news & comments

Screenshot:

![Screenshot_84](https://user-images.githubusercontent.com/4441068/88445727-71c52700-ce46-11ea-90ca-ed9ba5563817.png)


Parsing starts, the output is this:

Serving Flask app "app" (lazy loading)
Environment: production 
Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [25/Jul/2020 08:44:34] "?[37mGET / HTTP/1.1?[0m" 200 -

 DATES -------------------------------------------------------------------------------

25 July 2020, 03:16
25 July 2020, 06:31
25 July 2020, 04:10
25 July 2020, 04:45
25 July 2020, 02:22
25 July 2020, 01:32
24 July 2020, 23:57
URL LINKS----------------------------------------------------------------------------

['https://tengrinews.kz/world_news/v-mire-zafiksirovan-rekordnyiy-skachok-zarajeniy-covid-19-409426/', 'https://tengrinews.kz/kazakhstan_news/immunitet-koronavirusu-poyavilsya-polovinyi-kazahstantsev-409431/', 'https://tengrinews.kz/kazakhstan_news/nazvano-uslovie-pozvolyayuschee-ne-nosit-masku-na-ulitse-409427/', 'https://tengrinews.kz/crime/v-otkryityiy-dostup-vyilojili-foto-vseh-pedofilov-kazahstana-409428/', 'https://tengrinews.kz/kazakhstan_news/patsient-100-protsentnyim-porajeniem-legkih-obratilsya-409425/', 'https://tengrinews.kz/sports/magomed-ismailov-izbil-i-nokautiroval-aleksandra-emelyanenko-409424/', 'https://tengrinews.kz/kazakhstan_news/jurnalistyi-pokazali-proishodit-plyajah-burabaya-pervyiy-den-409422/']
['409426', '409431', '409427', '409428', '409425', '409424', '409422']
NUM COMMENTS-----------------------------------------------------------

5
19
15
23
19
25
20
NEWS HEADERS-----------------------------------------------------------

В мире зафиксирован рекордный скачок заражений COVID-19
Иммунитет к коронавирусу появился у половины казахстанцев - СМИ
Названо условие, позволяющее не носить маску на улице
В открытый доступ выложили фото всех педофилов Казахстана
Пациент со 100-процентным поражением легких обратился к врачам Алматы
Магомед Исмаилов избил и нокаутировал Александра Емельяненко
Журналисты показали, что происходит на пляжах Бурабая в первый день после запрета
---------DATES LENGTH-----------
7
---------URL LINKS LENGTH-----------
7
---------NUM COMMENTS LENGTH-----------
7
---------NEWS HEADERS LENGTH-----------
7
LENGTH OF main_data 7

length of result data 7
producer sending a blob

//**************NEWS METADATA************
В мире зафиксирован рекордный скачок заражений COVID-19

--------------COMMENTS--------------
['Данияр', '25 July 2020 08:32', '']
['Шлитци', '25 July 2020 03:56', '']
producer sending a blob

//**************NEWS METADATA************
Иммунитет к коронавирусу появился у половины казахстанцев - СМИ

--------------COMMENTS--------------
['Терпеливый', '25 July 2020 06:37', 'Значит у нас не 78 тыс заражённых, а 8,5 млн? Вот она вся правда']
['A Aidarov', '25 July 2020 07:20', 'Терпеливый, и карантин ваш полная пустышка. Государство сделало хуже себе и мсб только']
['Штангист из Кызылорды', '25 July 2020 06:53', 'Получается 9 млн людей переболели КВИ. Я тоже переболел. Но тест на антитела не показал. Вот ваша вся статистика...']
['Askar Bolatov', '25 July 2020 08:38', 'Думаю, что всё-таки поменьше. Это в крупных городах переболели 50%. Миллиона 3-4 по КЗ точно. Поэтому, это и плохо и хорошо. Плохо, много людей умерло и получили осложнения. Хорошо, что хоть 2-3 месяца не
заболеют, в отличие от не болевших.']
['Антикоррупционер', '25 July 2020 07:04', 'За 20 000тг сами сдавайте кровь. Когда я заболел в три дорого лечение обошлось. Так шо извини меня РОДИНА:))))']
['Shved', '25 July 2020 07:14', 'получается, что все карантинные мероприятия вводимые в стране - фуфло?']
['Мммм', '25 July 2020 07:03', 'Получается 50 % Казахстанцев заболели этой болезнью ? Сами себе противоречат) по статистике говорите одно, а всего с одной лаборатории 50 тыс заражённых....']
['Rus', '25 July 2020 07:25', 'У меня все близкие переболели, человек 50, из них ни один не был учтён. Статистика как ....
что захотят то и покажут.']
['Кикурики', '25 July 2020 07:06', 'Вот это поворот... !']
['Сага', '25 July 2020 07:15', 'когда вчера сказали что переболели около 2 млн.минздрав поднял шум.пошли опровержения а сегодня говорят что переболели половина населения. так кому верить.']
['KZ_KZ', '25 July 2020 06:58', 'Сам переболел и знаю многих которые болели схожи гриппом']
['G63', '25 July 2020 07:09', 'Половина КЗ получаеться по вашим словам, остальные ждут вторую волну осенью, пусть никто не
болеет.']
['Вера', '25 July 2020 08:38', 'G63, это не остальные осенью а опять все..вы думаете раз переболел и отстрелялся? этот вирус в каждом и болеть им всегда. надо молится чтобы нашли побыстрее лекарство .Всем,здоровья, мира,терпения и добра.']
['Асель', '25 July 2020 07:38', 'а сколько еще неучтенных? наверняка иммунитет имеют уже процентов 60-65']
['пат', '25 July 2020 07:33', 'Давайте прекращайте это цирк, переходим к нормальной жизни. Рано или поздно все столкнутся так зачем оттягивать?']
['Кузя', '25 July 2020 07:29', 'Концерт аякталды?']
['Батя', '25 July 2020 07:39', 'Кузя, и теперь должен быть разбор полетов']
['Алматинец', '25 July 2020 08:35', 'Иметь антитела не значит переболеть, это говорит о встрече с инфекцией, и не более, тем более иммунитет не сильный на 2-3 мес всего как при гриппе, так что расслабляется не стоит ....']
['Асан', '25 July 2020 07:48', 'Атасынын басы.']

127.0.0.1 - - [25/Jul/2020 08:46:32] "?[37mGET /parser/tengrinews HTTP/1.1?[0m" 200 -
