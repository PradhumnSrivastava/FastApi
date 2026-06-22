from fastapi import FastAPI, Path
import json

app = FastAPI()


def load_data():
    with open("patient.json", "r") as file:
        data = json.load(file)
    return data


@app.get("/")
def home():
    return {"message": "Patient Management System using FastAPI"}


@app.get("/about")
def about():
    return {"message": "A fully functional API to manage patient records"}


@app.get("/view_patients")
def view_patients():
    data = load_data()
    return data


@app.get("/patient/{patient_id}")
def get_patient(patient_id: int = Path(...,description="The ID of the patient to retrieve")):
    data = load_data()

    for patient in data:
        if patient["id"] == patient_id:
            return patient

    return {"error": "Patient not found"}


@app.get("/sort")
def sort_patients(sort_by: str = "age"):
    data = load_data()

    sorted_data = sorted(
        data,
        key=lambda x: x.get(sort_by, 0)
    )

    return sorted_data


@app.get("/filter")
def filter_patients(city: str):
    data = load_data()

    filtered_data = [
        patient
        for patient in data
        if patient["city"].lower() == city.lower()
    ]

    return filtered_data