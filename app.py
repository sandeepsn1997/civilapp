from flask import Flask
from flask_restful import Api

from resources.findresult import resultClass
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)

cors = CORS(app, resources={r"*": {"origins": "*"}})

api.add_resource(resultClass, "/calculate",)





if __name__ == "__main__":
  app.run()