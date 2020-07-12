from flask import Flask
import mydb
import myconfig
import json

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello from News Collector :D !"

@app.route('/getAll', methods=['GET'])
def getAll():
    articles = mydb.collection.find()
    response = []
    for article in articles:
        article['_id'] = str(article['_id'])
        response.append(article)
    return json.dumps(response)

@app.route('/getByTitle/<title>', methods=['GET'])
def getByTitle(title):
    print(title)

    article = mydb.collection.find_one({'title': title})

    response = {}
    for key, val in article.items():
        response[key] = val

    response['_id'] = str(response['_id'])

    return json.dumps(response)


@app.route('/getByAuthor/<author>', methods=['GET'])
def getByAuthor(author):
    print(author)
    articles = mydb.collection.find({'author': author})
    response = []
    for article in articles:
        article['_id'] = str(article['_id'])
        response.append(article)
    return json.dumps(response)


@app.route('/getByKeyword/<keyword>', methods=['GET'])
def getByKeyword(keyword):
    print(keyword)
    articles = mydb.collection.find({'$text': {'$search': keyword}},
                                        {'score': {'$meta': "textScore"}}).sort([('textScore',-1)])
    response = []
    for article in articles:
        article['_id'] = str(article['_id'])
        response.append(article)
    return json.dumps(response)

app.run(port=myconfig.PORT)

