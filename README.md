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

