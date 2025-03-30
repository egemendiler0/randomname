import uvicorn

from fastapi import FastAPI
from router.random_name_router import router as random_router
from db.session import  get_db
from free_apis.utils import config

app = FastAPI()

app.include_router(random_router)


if __name__ == "__main__":

    db = next(get_db())  # Create a db session

    uvicorn.run(app, host=config.HOST, port=config.PORT)