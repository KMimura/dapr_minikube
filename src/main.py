from fastapi import FastAPI

app = FastAPI()


@app.get("/events/action")
async def get_item():
    return {"message": "Hello World"}