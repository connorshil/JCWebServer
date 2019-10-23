import json
from flask import Flask
from flask_restful import Api, Resource, reqparse
import apiClassHolder

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
		
api.add_resource(apiClassHolder.addAction, '/action')
api.add_resource(apiClassHolder.averageStats, '/average')

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port='8080')