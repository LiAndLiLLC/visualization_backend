from aviation_tools.airline import Airline
from flask_restful import Resource


class RoutesOfAirline(Resource):
    def get(self, airline, mode="all", country="", country_b=""):
        v = Airline(airline)
        if mode == "in":
            return v.routes_in(country)
        elif mode == "from":
            return v.routes_from(country)
        elif mode == "between":
            return v.routes_between(country, country_b)
        elif mode == "all":
            return v.routes
