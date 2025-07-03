from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import verify


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # or ["*"] to allow all (not recommended for production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(verify.router)

@app.get("/ping")
async def ping_server():
    return "server active"
