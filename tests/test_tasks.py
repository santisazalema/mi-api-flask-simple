from app import create_app


def test_home():
    app = create_app()
    client = app.test_client()

    response = client.get("/")
    assert response.status_code == 200


def test_get_tasks():
    app = create_app()
    client = app.test_client()

    response = client.get("/tareas")
    assert response.status_code == 200


def test_create_task():
    app = create_app()
    client = app.test_client()

    response = client.post("/tareas", json={"titulo": "Aprender pytest"})
    assert response.status_code == 201

    data = response.get_json()
    assert data["titulo"] == "Aprender pytest"
    assert data["completada"] is False