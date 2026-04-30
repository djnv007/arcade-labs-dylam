import arcade
import json

# Localizamos la ruta real en tu sistema donde Arcade guarda ese mapa
ruta_real = arcade.resources.resolve_resource_path(":resources:tiled_maps/map_with_ladders.json")

# Abrimos y leemos el contenido
with open(ruta_real, 'r') as f:
    datos = json.load(f)
    print(json.dumps(datos, indent=4)) 