# spark-kafka-rest-example

this project consists of:

 - rest api that can only parse website - tengrinews. It collects 7 major news and top 100 comments for each post.

- parsed data is sent via kafka to apache spark to analyze top10 words in each news post

- top10 words is written to database


How to launch:

'python app.py'

this will start a rest api server sitting on 127.0.0.1:5000 and waiting, the end point is "127.0.0.1:5000/parser/website"

It can only parse tengrinews.kz website. However it records any incoming request to a local postgre db.


