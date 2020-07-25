# spark-kafka-rest-example

this project consists of:

 - rest api that can only parse website - tengrinews. It collects 7 major news and top 100 comments for each post.

- parsed data is sent via kafka to apache spark to analyze top10 words in each news post

- top10 words is written to database
