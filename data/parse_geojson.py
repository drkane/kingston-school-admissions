import json

with open("kingston-schools.json", "r", encoding="utf-8") as f:
    fj = json.load(f)

with open("distances.json", "r", encoding="utf-8") as d:
    dj = json.load(d)

geojson = { 
    "type": "FeatureCollection",
    "features": []
}

schools = []
for i in fj:
    feature = {
        "type":"Feature",
        "geometry": {
            "type": "Point", 
            "coordinates": [i["longitude"],i["latitude"]]
        }, 
        "properties": {}
    }
    for j in i:
        feature["properties"][j] = i[j]
    if(i["name"] in dj):
        feature["properties"]["distance"] = dj[i["name"]]
    else:
        print(i["type"], i["name"], "no distance found")
    schools.append(i["name"])
    geojson["features"].append(feature)
    
for j in dj:
    if j not in schools:
        print(j, "No school found")
    
with open("schools.geojson", "w") as k:
    json.dump(geojson, k, sort_keys=True, indent=4)