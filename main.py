import fastapi from FastAPI
import json

app = FastAPI()

def load_data():
    with open("patient.json", "r") as f:
        return json.load(f)

@app.get("/")
def home():
    return {"message": "Patient Management System from FastAPI"}

@app.get("/about")
def about():
    return {"message": "A fully functional API to manage patients records"}

