from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API de cotação de moeda"}

def test_get_valid_currency(monkeypatch):
    def mock_get_currency(from_currency):
        return 5.25

    monkeypatch.setattr("app.currency.get_currency", mock_get_currency)
    response = client.get("/get/?from_currency=BRL")
    assert response.status_code == 200
    assert response.json() == 5.25

def test_get_invalid_currency(monkeypatch):
    def mock_get_currency(from_currency):
        return {"error": "Invalid currency"}

    # Substitui a função real "get_currency" pelo mock
    monkeypatch.setattr("app.currency.get_currency", mock_get_currency)
    response = client.get("/get/?from_currency=INVALID")
    assert response.status_code == 400 
    assert response.json() == {"detail": "Invalid currency"}
