from flask import Flask, request
from flask_restful import Api, Resource
import random

app = Flask(__name__)
api = Api(app)

class toplamAl(Resource):
    def get(self, number):
        toplam = number + 5
        return {'Topla' : toplam}, 200


api.add_resource(toplamAl, '/toplamAl/<int:number>')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
    #app.run(host="IPADRESİ", port=5000)
    #app.run(host="127.0.0.1", port=5000)
    app.run()