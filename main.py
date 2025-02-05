#API REST: Interfaz de programación de apps para compartir recursos
#API REST con POSTMAN

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import uuid

#Variable que tendrá todas las caracteristicas de una API REST
app = FastAPI()

#Modelo de API REST de cursos de programación (ejemplo)
class Curso(BaseModel):
    id: Optional[str] = None
    nombre: str
    descripcion: Optional[str] = None
    nivel: str
    duracion: int

#Simulación de una base de datos
cursos_db = []

#CRUD: Read (lectura) con GET ALL: Va a leer todos los cursos que haya en la database
@app.get("/cursos/", response_model=List[Curso])
def obtener_cursos():
    #Una vez obtenido los cursos, los devuelvo
    return cursos_db

#CRUD: Create (escribir) POST: añadir un nuevo curso a la database
@app.post("/cursos/", response_model=Curso)
def crear_curso(curso:Curso):
    #UUID y UUID 4 generan un id único e irrepetible
    curso.id = str(uuid.uuid4())
    cursos_db.append(curso)
    return curso

#CRUD: Read (lectura) con GET individual: leerá el curso coincidente con el id que solicitemos
@app.get("/cursos/{curso_id}", response_model=Curso)
def obtener_curso(curso_id:str):
    #Shorthand: devuelo los cursos coincidentes con el id, aunque next toma el primer curso
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None)
    #Si no existe el curso buscado, lanza una excepción (error) indicandolo.
    if curso is None:
        raise HTTPException(status_code=404, detail='Curso no encontrado')
    return curso

#CRUD: Update (actualizar/modificar) con PUT individual: modificará un recurso coincidente con el id
@app.put("/cursos/{curso_id}", response_model=Curso)
def actualizar_curso(curso_id:str, curso_actualizado: Curso):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail='Curso no encontrado')
    curso_actualizado.id = curso_id
    #Busco el index del curso encontrado para modificarlo
    index = cursos_db.index(curso)
    cursos_db[index] = curso_actualizado
    return curso_actualizado

#CRUD: Delete (borrado/baja) con DELETE: Elimino un recurso coincidente con el ID
@app.delete("/cursos/{curso_id}", response_model=Curso)
def eliminar_curso(curso_id:str):
    curso = next((curso for curso in cursos_db if curso.id == curso_id), None)
    if curso is None:
        raise HTTPException(status_code=404, detail='Curso no encontrado')
    #La línea de abajo es un else al if de curso is None pero no necesito ponerlo
    cursos_db.remove(curso)
    return curso