import folium

# Coordonnées des grandes villes du Tchad
cities = {
    "N'Djamena": (12.1342, 15.0557),
    "Moundou": (8.5667, 16.0833),
    "Sarh": (9.15, 18.39),
    "Abeche": (13.83, 20.83),
    "Doba": (8.65, 16.85)
}

# Création de la carte centrée sur le Tchad
tchad_map = folium.Map(location=[15.4542, 18.7322], zoom_start=6)

# Ajout des marqueurs pour les grandes villes
for city, coord in cities.items():
    folium.Marker(location=coord, popup=city).add_to(tchad_map)

# Affichage de la carte
tchad_map.save('tchad_map.html')