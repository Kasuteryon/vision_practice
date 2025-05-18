import pandas as pd
import requests
import matplotlib.pyplot as plt
from collections import Counter
import re


CSV_FILE = "betsa3.csv"        
FULL_NAME_COLUMN = "Author full names"  
MAX_NAMES = 1000 # Límite máximo de nombres únicos (limite por consulta de genderize.io)

def infer_gender(name):
    url = f"https://api.genderize.io?name={name}"
    try:
        response = requests.get(url)
        data = response.json()
        return data.get("gender")
    except:
        return None

# === CARGAR CSV Y PROCESAR NOMBRES ===
df = pd.read_csv(CSV_FILE)
first_names = []

for row in df[FULL_NAME_COLUMN].dropna():
    authors = row.split(";")
    for author in authors:
        # Quitar paréntesis y Scopus ID
        author_clean = re.sub(r"\(.*?\)", "", author).strip()
        if "," in author_clean:
            parts = author_clean.split(",")
            if len(parts) > 1:
                first_name = parts[1].strip().split()[0]  # Tomar solo el primer nombre
                if first_name.isalpha():
                    first_names.append(first_name.lower())

# Eliminar duplicados y limitar número de consultas
unique_first_names = list(set(first_names))[:MAX_NAMES]

# === CONSULTAR API Y GUARDAR RESULTADOS ===
gender_results = []
for name in unique_first_names:
    gender = infer_gender(name)
    if gender in ["male", "female"]:
        gender_results.append(gender)

# === CONTAR Y GRAFICAR ===
counts = Counter(gender_results)
labels = counts.keys()
sizes = counts.values()

plt.figure(figsize=(6,6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=["#6495ED", "#FF69B4"])
plt.title("Distribución de género inferida por nombres de autores")
plt.axis("equal")
plt.show()