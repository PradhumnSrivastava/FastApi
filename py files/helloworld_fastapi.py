from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello World"}

@app.get("/name")
def get_name():
    return {'message': 'My name is Pradhumn'}