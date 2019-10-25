import json
from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse
from server import apiClassHolder

app = Flask(__name__)
api = Api(app, catch_all_404s=True)

#authentication can easily be added with the flask_auth library

parser = reqparse.RequestParser()

api.add_resource(apiClassHolder.addAction, '/api/action')
api.add_resource(apiClassHolder.averageStats, '/api/average')


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port='8080')