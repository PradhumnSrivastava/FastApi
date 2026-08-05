from fastapi import FastAPI

app = FastAPI()

@app.get("/about")
def about():
    return {"info": "This is GET request"}