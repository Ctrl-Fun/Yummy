import mysql.connector

# Configuración de la conexión a MySQL
config = {
    "host": "localhost",
    "user": "yummy_usr",
    "password": "yummy",
    "database": "yummy_db"
}

# Conectar a la base de datos
conn = mysql.connector.connect(**config)
c = conn.cursor()


# Insertar recetas
recetas_ejemplo = [
    ("Tarta de Manzana", "Clásica", "Ana Pérez"),
    ("Pizza", "Napolitana", "Juan Gómez")
]
c.executemany("INSERT INTO receta (nombre, variante, creador) VALUES (%s, %s, %s)", recetas_ejemplo)

# Obtener los IDs de las recetas insertadas
c.execute("SELECT id FROM receta")
recetas_ids = [row[0] for row in c.fetchall()]

# Insertar ingredientes
ingredientes_ejemplo = [
    ("Harina", None),
    ("Manzana", "Verde"),
    ("Azúcar", None),
    ("Queso", "Mozzarella"),
    ("Tomate", None)
]
c.executemany("INSERT INTO ingrediente (nombre, variante) VALUES (%s, %s)", ingredientes_ejemplo)

# Obtener los IDs de los ingredientes
c.execute("SELECT id FROM ingrediente")
ingredientes_ids = [row[0] for row in c.fetchall()]

# Insertar ingredientes en recetas
ingrediente_receta_ejemplo = [
    (recetas_ids[0], ingredientes_ids[0], 200, "g"),  # Harina para Tarta de Manzana
    (recetas_ids[0], ingredientes_ids[1], 3, "unidades"),  # Manzana Verde
    (recetas_ids[1], ingredientes_ids[3], 150, "g"),  # Queso Mozzarella para Pizza
    (recetas_ids[1], ingredientes_ids[4], 2, "unidades")  # Tomate para Pizza
]
c.executemany("INSERT INTO ingrediente_receta (id_receta, id_ingrediente, cantidad, unidad) VALUES (%s, %s, %s, %s)", ingrediente_receta_ejemplo)

# Insertar pasos en recetas
pasos_receta_ejemplo = [
    (recetas_ids[0], 1, "Mezclar la harina con el azúcar."),
    (recetas_ids[0], 2, "Agregar las manzanas en rodajas."),
    (recetas_ids[1], 1, "Extender la masa de pizza."),
    (recetas_ids[1], 2, "Añadir el tomate y la mozzarella.")
]
c.executemany("INSERT INTO pasos_receta (id_receta, numero_paso, descripcion) VALUES (%s, %s, %s)", pasos_receta_ejemplo)

# Obtener los IDs de los pasos insertados
c.execute("SELECT id FROM pasos_receta")
pasos_ids = [row[0] for row in c.fetchall()]

# Insertar imágenes asociadas a pasos
imagenes_receta_ejemplo = [
    (recetas_ids[0], pasos_ids[0], "images/tarta_paso1.jpg", "Mezcla de harina y azúcar"),
    (recetas_ids[0], pasos_ids[1], "images/tarta_paso2.jpg", "Añadiendo las manzanas"),
    (recetas_ids[1], pasos_ids[2], "images/pizza_paso1.jpg", "Masa de pizza extendida"),
    (recetas_ids[1], pasos_ids[3], "images/pizza_paso2.jpg", "Tomate y mozzarella listos")
]
c.executemany("INSERT INTO imagen_receta (id_receta, id_paso, image_path, descripcion) VALUES (%s, %s, %s, %s)", imagenes_receta_ejemplo)

# Confirmar los cambios y cerrar la conexión
conn.commit()
c.close()
conn.close()

print("Base de datos llena con datos de ejemplo.")