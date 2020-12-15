import fastapi
import httpx

from models.location import Location
from models.umbrella_status import UmbrellaStatus

router = fastapi.APIRouter()


@router.get('/api/umbrella', response_model=UmbrellaStatus)
async def do_i_need_a_umbrella(location: Location = fastapi.Depends()):
    url = f"https://weather.talkpython.fm/api/weather?city={location.city}&state={location.state}&country={location.country}&units=imperial "
    if location.state:
        url += f"&state={location.state}"

    async with httpx.AsyncClient() as client:
        resp = await client.get(url)
        resp.raise_for_status()

        data = resp.json()

    weather = data.get('weather', {})
    category = weather.get('category', 'UNAVAILABLE')

    forecast = data.get('forecast', {})
    temp = forecast.get('temp', 0.0)
    bring = category.lower().strip() == 'rain'

    umbrella = UmbrellaStatus(bring_umbrella = bring, temp = temp)



    return location
