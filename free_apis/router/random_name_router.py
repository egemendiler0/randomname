from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import requests
from utils import configs as config

router = APIRouter(prefix=config.ROUTER_PREFIX, tags=[config.TAG_WEATHER])


class RandomNameResponse(BaseModel):
    random_name: str


@router.get("", response_model=RandomNameResponse)
def get_random_name():
    api_url = "https://randomuser.me/api/"
    response = requests.get(api_url)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Random name API request failed")

    data = response.json()
    if not data.get("results"):
        raise HTTPException(status_code=500, detail="Invalid response from API")

    name_info = data["results"][0]["name"]
    full_name = f"{name_info['first']} {name_info['last']}"

    return RandomNameResponse(random_name=full_name)

