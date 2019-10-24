from flask_restful import Api, Resource, reqparse
from flask import request
from dbFake import dbFake

db = dbFake()

class addAction(Resource):
	def post(self):
		req_data = request.get_json()
		actionWord = req_data['action']
		timeCount = req_data['time']
		
		returnStatement = db.addAction(actionWord, timeCount)
		
		return returnStatement
		
class averageStats(Resource):
	def get(self):
		results = []
		tempDict = db.getCopy()
		
		for actionWord in tempDict:
			tempTime = tempDict[actionWord]['time']
			tempCount = tempDict[actionWord]['count']
			avg = tempTime/tempCount
			results.append(dict(action=actionWord, average=avg))
			
		return results
