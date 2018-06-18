import folium
map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Mapbox Bright")
#map.add_child(folium.Marker(location=[22.26, 84.85],popup="i am the marker", icon=folium.Icon(color='red')))
map.save("Map2.html")
