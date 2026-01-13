from fastapi import FastAPI

app = FastAPI(title="DOCU-EXTRACT")

@app.get("/")
def health_check():
    return {"status": "running"}
