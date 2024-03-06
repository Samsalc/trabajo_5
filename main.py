from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uuid

app = FastAPI(
    title="API Trabajo 5",
    version="0.0.1"
)


@app.post("/api/v1/register/")
async def register(username: str, email: str, password: str):
    return {
        "username": username,
        "email": email,
        "password": password,
        "id": str(uuid.uuid4()),
        "message": "El usuario ingreso con exito",
        "status_code" : 201
    }


@app.get("/api/v1/{user_id}/")
async def get_user(user_id: str):
    users = {
        "hello-3344": {
            "username": "mafer",
            "email": "mafern@swagmail.com",
            "password": "mafern123"
        },
        "id-76":{
            "username": "sam",
            "email": "sam@swagmail.com",
            "password": "sam123"
        }
    }


    if user_id in users:
        user = users[user_id]
        return JSONResponse(
            content=user,
            status_code=status.HTTP_200_OK
        )
    else:
        return JSONResponse(
            content="No existe el usuario",
            status_code=status.HTTP_404_NOT_FOUND
        )



tasks={}
@app.post("/api/v1/tasks/create/")
async def register(title: str, descripcion: str, estado: str):
    task_id = str(uuid.uuid4())
    task = {
        "titulo_tarea": title,
        "descripcion": descripcion,
        "estado": estado,
        "task_id": task_id
    }
    tasks[task_id] = task
    return{
        "message": "Se creo la tarea con exito",
        "task_id": task_id,
        "status_code": status.HTTP_201_CREATED
    }