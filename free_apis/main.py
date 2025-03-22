from fastapi import FastAPI
from router.random_name_router import router as random_router


app = FastAPI()

app.include_router(random_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)