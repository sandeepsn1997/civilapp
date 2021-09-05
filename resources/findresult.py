
from flask_restful import Resource
from flask import request
from resources.calculate import main

class resultClass(Resource):
    def post(self):
        try:
            data = request.get_json()
            return main(data["important_facility_data"], data["less_important_facility_data"],data["D"],data["P"])
        except:
            return False

