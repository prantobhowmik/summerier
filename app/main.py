
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



# Routers will be included here
from app.routers import summarize
app.include_router(summarize.router)

@app.get("/")
def root():
    return {"message": "FastAPI is running!"}
