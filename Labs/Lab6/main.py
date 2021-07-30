from typing import Dict, List, Optional
from fastapi import FastAPI
from joblib import load
from tinydb import TinyDB, Query
from datetime import datetime
from tinydb.operations import set

app = FastAPI(title="Lab 6")

# aquí carguen el modelo guardado (con load de joblib) y
#model = load("C:/Users/bruno/OneDrive/Documentos/GitHub/LabProgra/Labs/Lab6/modelo.joblib")
model = load("modelo.joblib")

# el cliente de base de datos (con tinydb). Usen './db.json' como bbdd.
db = TinyDB("db.json")

# Nota: En el caso que al guardar en la bbdd les salga una excepción del estilo JSONSerializable
# conviertan el tipo de dato a uno más sencillo.
# Por ejemplo, si al guardar la predicción les levanta este error, usen int(prediccion[0])
# para convertirla a un entero nativo de python.

# Nota 2: Las funciones ya están implementadas con todos sus parámetros. No deberían
# agregar más que esos.



@app.post("/potabilidad/")
async def predict_and_save(observation: Dict[str, float]):
    valores = list(observation.values())
    prediccion = model.predict([valores])
    #Ahora insertamos el valor, con la fecha
    hoy = datetime.now()
    observation["Day"] = hoy.day
    observation["Month"] = hoy.month
    observation["Year"] = hoy.year
    observation["Prediction"] = int(prediccion[0])

    id = db.insert(observation)  # insertamos solo el diccionario, no la lista con el diccionario.

# el número que imprime (121) indica id (indice) interno del documento recién insertado.
    return {"Potabilidad": int(prediccion[0]) , "id": int(id)}


@app.get("/potabilidad/")
async def read_all():
    # implementar 2 aquí.
    return db.all()


@app.get("/potabilidad_diaria/")
async def read_by_day(day: int, month: int, year: int):
    Mediciones = Query()
    valores = db.search((Mediciones.Day == day) & (Mediciones.Month == month) & (Mediciones.Year == year))
    return valores


@app.put("/potabilidad/")
async def update_by_day(day: int, month: int, year: int, new_prediction: int):
    Mediciones = Query()
    updated_elements = db.update(set("Prediction", new_prediction), (Mediciones.Day == day) & (Mediciones.Month == month) & (Mediciones.Year == year))
    
    return {"success": True, "updated_elements" : updated_elements}


@app.delete("/potabilidad/")
async def delete_by_day(day: int, month: int, year: int):
    Mediciones = Query()
    deleted_elements = db.remove((Mediciones.Day == day) & (Mediciones.Month == month) & (Mediciones.Year == year))
    
    return {"success": True, "deleted_elements" : deleted_elements}
