import fastapi
import uvicorn

# Developer speed is faster, not necesarily user speed.

api = fastapi.FastAPI()  # Creates an instance.


@api.get("/")  # Default root.
def index():
    return {  # Uses JSON for message and status.
        "message": "Hello World!",
        "status": "OK"
    }


uvicorn.run(api)
