from flask import Flask
import requests
from datetime import datetime
from flask import jsonify
from flask import make_response
from flask import request
import psycopg2
from main_parse import main_parse

from time import sleep
from json import dumps
from kafka import KafkaProducer


app = Flask(__name__)


result_data = None

def add_to_db(full_url, when):

    website = full_url.split('parser/')[1]
    conn = psycopg2.connect(dbname="incoming_api_requests",user="postgres",password="admin")
    cur = conn.cursor()
    sql = "INSERT INTO parsing_queries (website, query_time) VALUES (%s, %s)"
    cur.execute(sql, (website, when))
    conn.commit()
    conn.close()

@app.route("/", methods = ['GET'])
def main():
    return jsonify('service is waiting, standby..')

@app.route("/parser/<string:website>", methods = ['GET'])
def parse(website):  
    when = datetime.now()
    if website != 'tengrinews.com' and website != 'tengrinews':
        add_to_db(request.url, when)
        error_description = 'this service can only parse tengrinews.com! still added query to db...'
        return make_response(jsonify({'error': error_description }), 404)
    else:
        add_to_db(request.url, when)
        result_data = main_parse()
        turn_kafka(result_data)
        return make_response(jsonify("adding the query to postgre db and parsing this website...", request.url))



producer = KafkaProducer(bootstrap_servers=['127.0.0.1:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

topic = 'sending'
def print_one_post(n):
    print(n)
    # comments_list = n[1]
    # print('**************NEWS METADATA************')
    # print(news_block)
    # print_comments(comments_list)

def print_comments(comments_list):
    print()
    print('---COMMENTS---')
    for com in comments_list:
        print()
        print(com)

def turn_kafka(data):
    if data:
        print('length of result data %d' % (len(data)))
        for i in range(len(data)):
            print('producer sending a blob')

            blob = data[i]
            print_one_post(blob)
            producer.send(topic, blob)
            sleep(1)




def print_news(n):
    news_block = n[0]
    comments_list = n[1]
    print('**************NEWS METADATA************')
    print(news_block)
    print_comments(comments_list)

def print_comments(comments_list):
    print()
    print('---COMMENTS---')
    for com in comments_list:
        print()
        print(com)


if __name__ == "__main__":

    app.run(debug=True)

    

