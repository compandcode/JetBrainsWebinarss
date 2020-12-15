import fastapi
import uvicorn
from views import home
from api import weather_api
# https://github.com/compandcode/compandcodeghs/settings
# Developer speed is faster, not necesarily user speed.

api = fastapi.FastAPI()  # Creates an instance.


def configure():
    api.include_router(home.router)
    api.include_router(weather_api.router)


configure()

if __name__ == '__main__':
    uvicorn.run(api)
