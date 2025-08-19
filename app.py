from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.db.base import base, engine

from src.api.v1.users import router as users_router
from src.api.v1.tasks import router as tasks_router
    
app = FastAPI(title="Task Manager API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def read_root():
    return {"message": "status: ok"}

@app.on_event("startup")
async def startup_event():
    base.metadata.create_all(bind=engine)

@app.on_event("shutdown")
def shutdown_event():
    with open("log.txt", mode="a") as log:
        log.write("Application shutdown")

app.include_router(users_router)
app.include_router(tasks_router)