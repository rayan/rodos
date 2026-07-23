import json

from django.shortcuts import render


DUMMY_VESSELS = [
    {"name": "MSC AURORA",    "type": "Container Ship", "flag": "Panama",        "lat": 22.5,  "lng": 37.8,  "speed": 14.2, "heading": 325},
    {"name": "EVER GOLDEN",   "type": "Container Ship", "flag": "Marshall Is.",  "lat": 20.1,  "lng": 38.4,  "speed": 12.8, "heading": 150},
    {"name": "MAERSK CAIRO",  "type": "Bulk Carrier",   "flag": "Denmark",       "lat": 18.3,  "lng": 39.1,  "speed":  9.5, "heading": 340},
    {"name": "GULF PIONEER",  "type": "Tanker",         "flag": "Saudi Arabia",  "lat": 24.7,  "lng": 37.2,  "speed": 11.0, "heading": 170},
    {"name": "NILE TRADER",   "type": "Bulk Carrier",   "flag": "Egypt",         "lat": 16.9,  "lng": 41.5,  "speed":  8.3, "heading": 290},
    {"name": "SUEZ EXPRESS",  "type": "Container Ship", "flag": "Greece",        "lat": 27.4,  "lng": 34.1,  "speed": 15.1, "heading": 320},
    {"name": "RED SEA STAR",  "type": "Tanker",         "flag": "Liberia",       "lat": 15.2,  "lng": 42.3,  "speed": 10.7, "heading": 355},
    {"name": "JEDDAH SPIRIT", "type": "General Cargo",  "flag": "Saudi Arabia",  "lat": 21.8,  "lng": 37.0,  "speed":  7.9, "heading": 200},
]


def vessel_map(request):
    return render(request, "core/vessel_map.html", {
        "vessels_json": json.dumps(DUMMY_VESSELS),
    })
