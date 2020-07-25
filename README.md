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


