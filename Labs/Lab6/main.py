from typing import Dict, List, Optional
from fastapi import FastAPI
from joblib import load
from tinydb import TinyDB, Query
from datetime import datetime
from tinydb.operations import set

app = FastAPI(title="Lab 6")

# aquí carguen el modelo guardado (con load de joblib) y
model = None
# el cliente de base de datos (con tinydb). Usen './db.json' como bbdd.
db = None

# Nota: En el caso que al guardar en la bbdd les salga una excepción del estilo JSONSerializable
# conviertan el tipo de dato a uno más sencillo.
# Por ejemplo, si al guardar la predicción les levanta este error, usen int(prediccion[0])
# para convertirla a un entero nativo de python.

# Nota 2: Las funciones ya están implementadas con todos sus parámetros. No deberían
# agregar más que esos.


@app.post("/potabilidad/")
async def predict_and_save(observation: Dict[str, float]):
    # implementar 1. aquí
    pass


@app.get("/potabilidad/")
async def read_all():
    # implementar 2 aquí.
    pass


@app.get("/potabilidad_diaria/")
async def read_by_day(day: int, month: int, year: int):
    # implementar 3 aquí
    pass


@app.put("/potabilidad/")
async def update_by_day(day: int, month: int, year: int, new_prediction: int):
    # implementar 4 aquí
    pass


@app.delete("/potabilidad/")
async def delete_by_day(day: int, month: int, year: int):
    # implementar 5 aquí
    pass
