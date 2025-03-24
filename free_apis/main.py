import uvicorn

from fastapi import FastAPI
from router.random_name_router import router as random_router
from db.session import  get_db, get_sql_server_version
from utils import config

app = FastAPI()

app.include_router(random_router)


if __name__ == "__main__":

    db = next(get_db())  # Create a db session
    version = get_sql_server_version(db)
    print("SQL Server Version:", version[0])

    uvicorn.run(app, host=config.HOST, port=config.PORT)