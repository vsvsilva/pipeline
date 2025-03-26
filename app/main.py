from fastapi import FastAPI, HTTPException
from app.currency import get_currency

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API de cotação de moeda"}


@app.get("/get/")
def get(from_currency: str):
    result = get_currency(from_currency)

    if isinstance(result, dict) and "error" in result:
        raise HTTPException(status_code=400, detail=result["error"])

    return result
