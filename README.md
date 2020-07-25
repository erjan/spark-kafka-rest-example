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


Parsing starts, the sample output is this:

- Serving Flask app "app" (lazy loading)
- Environment: production 
- Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
- 127.0.0.1 - - [25/Jul/2020 08:44:34] "?[37mGET / HTTP/1.1?[0m" 200 -

DATES -------------------------------------------------------------------------------

25 July 2020, 03:16
25 July 2020, 06:31

URL LINKS----------------------------------------------------------------------------

['https://tengrinews.kz/world_news/v-mire-zafiksirovan-rekordnyiy-skachok-zarajeniy-covid-19-409426/', 'https://tengrinews.kz/kazakhstan_news/immunitet-koronavirusu-poyavilsya-polovinyi-kazahstantsev-409431/', 'https://tengrinews.kz/kazakhstan_news/nazvano-uslovie-pozvolyayuschee-ne-nosit-masku-na-ulitse-409427/', 'https://tengrinews.kz/crime/v-otkryityiy-dostup-vyilojili-foto-vseh-pedofilov-kazahstana-409428/', 'https://tengrinews.kz/kazakhstan_news/patsient-100-protsentnyim-porajeniem-legkih-obratilsya-409425/', 'https://tengrinews.kz/sports/magomed-ismailov-izbil-i-nokautiroval-aleksandra-emelyanenko-409424/', 'https://tengrinews.kz/kazakhstan_news/jurnalistyi-pokazali-proishodit-plyajah-burabaya-pervyiy-den-409422/']

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

-----------------NEWS METADATA-----------------

Магомед Исмаилов избил и нокаутировал Александра Емельяненко

--------------COMMENTS--------------

['Rinat Tahirovich', '25 July 2020 02:26', 'помоиму Емельяненко к бою совсем неготовился, а только постил посты про своего
брата и его отношения с ним, а о бое вообще не думал']

['КЗ РК', '25 July 2020 07:39', 'Rinat Tahirovich, говорят что матч купленный, очень заинтересованной персоной с Кавказа)))сами поняли кем)))']

['ADIL', '25 July 2020 02:11', 'Все равно уважаю Емельяненко. 2 года простоя плюс возраст дали о себе знать.. Будь здоров Александр и возвращайся в октагон поскорее.. Дай Аллах тебе здоровья и силы ..']

['Айдос', '25 July 2020 02:23', 'Магомед красавчик']

['UFC', '25 July 2020 03:33', 'Айдос, Саня тоже красавчик, не одного удара не упустил, всё поймал.']
['Сакен', '25 July 2020 08:28', 'UFC, ���']

['Саня Справедливый', '25 July 2020 02:26', 'Мага красавчик!Заслуженная победа!Сашу "приземлил" немножко,а то "я буду бить
по лысый башке ...слишком самоуверенный был."Те кто ведет себя смиренно -будут возвышенны,те кто возвышает себя- будут унижены"-Мэни Пакьяо.']

['Улугбек', '25 July 2020 05:45', 'Саня Справедливый, это слова из Евангелия']

['Ерик Есенов', '25 July 2020 02:32', 'Саша уже не тот..... Это уже не драгон пить в спортзале. Уходить надо!!! Всё!!!']

['Ддд', '25 July 2020 02:22', 'Возраст, че сказать...']

['Ансар', '25 July 2020 03:37', 'наказание за все, что он вытворял. он еле выжил']

['Баке', '25 July 2020 06:53', 'да этому Александру уже кто только не надавал люлей. Все уже, ему только идти в вышибалы весь опыт пропил .']

['Капитан Очевидность', '25 July 2020 01:44', 'ма ша Аллах! поздравляю!']

['Duma', '25 July 2020 01:55', 'Наказал по полному.']

['Актау', '25 July 2020 02:25', 'От это да! Красава Мага�']

['Архитектор', '25 July 2020 05:33', 'Так мага это не кокляев,тут драться надо было!']

['Аргынтинец', '25 July 2020 07:04', 'Мага красава! Комментатору бы не плохо было пойти на курсы английского, ужасный акцент и скудный словарный запас, уши режет, когда его слышу. Емельяненко в этом бою был 0.']

['Borg', '25 July 2020 07:45', 'Александр уже не тот, старый стал. Мешок. Мага красавчик. Но у обоих не уровень UFC, там их сразу вынесут.']

['Дос', '25 July 2020 02:01', 'Красавчик так надо этому насильнику �']

['Закись ашота', '25 July 2020 01:47', '1']

['Шах', '25 July 2020 01:58', 'я знал 2000% Мага снесет Саню)) Почему? Мага был заряжен)))']

['Андрей', '25 July 2020 03:36', 'Емельяненко старшего, а не младшего']

['Aseke', '25 July 2020 04:33', 'Просто мал есть же �']

['Tiziana Terenzi', '25 July 2020 01:55', 'Теперь Федька выйдет с ним)']

['Маке', '25 July 2020 02:38', 'Емельяненко младший лучше']

['Zzz', '25 July 2020 05:19', 'Очень сильно Саша тренировал руки, я думал что он подтянул борьбу, слабый он в ближнем бою.
Пирожок ты Саша, вот он и съел тебя. А вообще здесь мотивация разная была, Мага за славу и за собственные амбиции бился, Саша за деньги, вот и отаварился по полной. И первое что-это Аллах с Магой.']


127.0.0.1 - - [25/Jul/2020 08:46:32] "?[37mGET /parser/tengrinews HTTP/1.1?[0m" 200 -
