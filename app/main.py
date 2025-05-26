from fastapi import FastAPI
from app.api.routes import generator_route

app = FastAPI()

app.include_router(generator_route.router)

print("SERVER STARTED!")
