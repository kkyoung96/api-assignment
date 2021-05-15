from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return { "hello": "this is index" }
#    return { "message" : "Hello World1" }

@app.get("/userinfo")
async def userinfo():
    return { "name": "min", "age": "26","sex": "man","home": "seoul"}

@app.get("/healthcheck")
async def healthcheck():
    return {"health":"green"}
