from fastapi import FastAPI
from routers import projects, contact

app = FastAPI()

app.include_router(projects.router)
app.include_router(contact.router)

@app.get("/")
def root():
    return {"message": "Welcome to Marc Wolfe's Portfolio!"}