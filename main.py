from aviation_tools.airline import Airline
from aviation_tools.airport import Airport
from aviation_tools.region import Region
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api

from resources.routes_of_airline import RoutesOfAirline

app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={
    r"/v1/*": {
        "origins": "http://localhost:8080"
    }
})


@app.route("/v1/airlines.json")
def all_airlines():
    return jsonify(Airline.all_airlines())


@app.route("/v1/regions.json")
def all_regions():
    return jsonify(Region.all_regions())


@app.route("/v1/airports.json")
def all_airports():
    return jsonify(Airport.raw_data())


api.add_resource(
    RoutesOfAirline,
    '/v1/airlines/<string:airline>/routes/',
    '/v1/airlines/<string:airline>/routes/<string:mode>/<string:country>/',
    '/v1/airlines/<string:airline>/routes/<string:mode>/<string:country>/<string:country_b>/'
)

if __name__ == "__main__":
    app.run(debug=True)
