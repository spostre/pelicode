import os

# Obtiene la ruta absoluta de la carpeta donde está este archivo (la carpeta 'data').
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construye las rutas completas a cada archivo JSON. Esta es la forma robusta.
libros = os.path.join(BASE_DIR, 'libros.json')
peliculas = os.path.join(BASE_DIR, 'peliculas.json')
musica = os.path.join(BASE_DIR, 'musica.json')

