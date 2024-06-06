import re
import math
import pandas as pd
import pretty_html_table

def html_from_list(kebabs: list[dict]) -> str:
    results = {}
    for kebab in kebabs:
        for key in kebab.keys():
            if key in results.keys() and not key in ["latitude", "longitude"]: results[key] += [kebab[key]]
            else: results[key] = [kebab[key]]
    df = pd.DataFrame(results)
    return pretty_html_table.build_table(df, 'blue_light')

def search_name(search: str, kebabs:list[dict]) -> list[dict]:
    regex = re.compile(search)
    kebab_matches = []
    for kebab in kebabs:
        if re.match(regex, kebab["name"]): kebab_matches.append(kebab)
        if len(kebab_matches) > 10:
            return kebab_matches
    return kebab_matches

def search_rating(rating: int, kebabs:list[dict]) -> list[dict]:
    kebab_matches = []
    for kebab in kebabs:
        if kebab["rating"] >= rating: kebab_matches.append(kebab)
        if len(kebab_matches) > 10:
            return kebab_matches
    return kebab_matches

def search_price(price: int, kebabs:list[dict]) -> list[dict]:
    kebab_matches = []
    for kebab in kebabs:
        if kebab["price"] <= price: kebab_matches.append(kebab)
        if len(kebab_matches) > 10:
            return kebab_matches
    return kebab_matches

def search_closer(lat: int, lon: int, distance: int, kebabs:list[dict]) -> list[dict]:
    kebab_matches = []
    for kebab in kebabs:
        if haversine(lat, lon, kebab["latitude"], kebab["longitude"]) <= distance: 
            kebab["distance"] = distance
            kebab_matches.append(kebab)
        if len(kebab_matches) > 10:
            return kebab_matches
    return kebab_matches

def haversine(lat1, lon1, lat2, lon2) -> int:
    R = 6371.0 # Radius of the Earth in kilometers.
    
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    delta_lat = lat2_rad - lat1_rad
    delta_lon = lon2_rad - lon1_rad
    
    # Haversine formula
    a = math.sin(delta_lat / 2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return abs(R * c)