from fastapi import FastAPI
from router.random_name_router import router as random_router


app = FastAPI()

app.include_router(random_router)


