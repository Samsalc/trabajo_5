from fastapi import FastAPI
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


