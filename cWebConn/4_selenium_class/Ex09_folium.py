#Ex09_folium.py
# 지도를 html로 만드는게 folium 우리는 지도를 자바베이스로 해야만함으로
# 구경하는 정도

import folium

map_osm = folium.Map(location=[37.572807,126.975918],zoom_start=19)
folium.Marker(location=[37.572807,126.975918], popup='우리들의 세종문화회관').add_to(map_osm) #마커 찍기
map_osm.save('map1.html')