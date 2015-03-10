import requests
from functional import memoize
from geopy.geocoders import GoogleV3


def google_nearby_places(location, keyword, page_token):
    return requests.get(
        "https://maps.googleapis.com/maps/api/place/nearbysearch/json",
        params={
            "location": "%s,%s" % location,
            "rankby": "distance",
            "keyword": keyword,
            "key": GOOGLE_API_KEY
        } if not page_token else {
            "pagetoken": page_token,
            "key": GOOGLE_API_KEY
        }).json()


@memoize
def google_reverse_geocode(coordinate_tuple):
    return GoogleV3(api_key=GOOGLE_API_KEY).reverse(coordinate_tuple,
                                                    exactly_one=True).raw


def country_code_from_google_dict(google_dict):
    return filter(
        lambda component: "country" in component["types"],
        google_dict["address_components"]
    )[0]["short_name"]


def business_place_id(name, geolocation_as_string):
    results = requests.get(
        "https://maps.googleapis.com/maps/api/place/textsearch/json",
        params={"key": GOOGLE_API_KEY,
                "location": geolocation_as_string,
                "radius": 1000,
                "query": name
                }).json().get("results")
    return results[0]["place_id"] if results else ""
