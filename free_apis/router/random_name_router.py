import requests
import re

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from utils import config

router = APIRouter(prefix=config.ROUTER_PREFIX, tags=[config.TAG_WEATHER])


class RandomNameResponse(BaseModel):
    random_name: str


@router.get("", response_model=RandomNameResponse)
def get_random_name():
    api_url = "https://randomuser.me/api/"   # env den al
    response = requests.get(api_url)

    if response.status_code != 200:  # constants a al 200 kodu HTTPResponseStatusCode
        raise HTTPException(status_code=500, detail="Random name API request failed")

    data = response.json()
    if not data.get("results"):
        raise HTTPException(status_code=500, detail="Invalid response from API")

    name_info = data["results"][0]["name"]
    full_name = f"{name_info['first']} {name_info['last']}"

    # Özel karakter kontrolü (sadece harf, boşluk, - ve ' izin verilir)
    if not re.match(r"^[a-zA-Z '-]+$", full_name):
        raise HTTPException(status_code=400, detail="Generated name contains invalid characters")

    return RandomNameResponse(random_name=full_name)
