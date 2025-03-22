from fastapi import APIRouter
from utils import configs as config

router = APIRouter(prefix=config.ROUTER_PREFIX, tags=[config.TAG_WEATHER])


@router.get("")
def get_random_name():
    name = "Egemen"
    # request get ile url cagirilacak weather'daki gibi
    #response = requests.get(xxxx, params=params)
    # none kontrolu yap , ozel karakter donmedigini kontrol et .#
    #  log ekle
    # db conn
    return {"random_name": name}
