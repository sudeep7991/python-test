import folium
import pandas

data=pandas.read_csv("hotel.txt")
name=list(data["NAME"])
lat=list(data["LAT"])
lon=list(data["LON"])
rtg=list(data["RATING"])

def color_producer(rating):
    if rating == 7 :
       return 'red'
    else:
       return 'orange'


map=folium.Map(location=[17.403434, 78.452859], zoom_start=5, tiles="Mapbox Bright")

fgh = folium.FeatureGroup(name="Hotels")

for nm,lt,ln,rt in zip(name,lat,lon,rtg):
    fgh.add_child(folium.CircleMarker(location=[lt,ln] ,radius=6 ,popup=nm+" "+str(rt)+"star",
     fill_color=color_producer(rt),fill=True, color='grey', fill_opacity=0.7))

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(),
style_function = lambda x: {'fillColor':'green' if x['properties']['POP2005']<10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

map.add_child(fgh)
map.add_child(fgp)
map.add_child(folium.LayerControl())
map.save("map2.html")
