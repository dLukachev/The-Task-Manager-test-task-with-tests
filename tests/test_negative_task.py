def test_field_not_found(client):
    response = client.get("/tasks/99999999-9999-9999-9999-999999999999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}

def test_create_task_invalid_data(client):
    response = client.post("/tasks/", json={
        "description": "This task has no title.",
        "status": "create",
        "user_id": 1
    })
    assert response.status_code == 422
    assert "title" in response.json()["detail"][0]["loc"]

def test_update_task_not_found(client):
    response = client.put("/tasks/99999999-9999-9999-9999-999999999999/", json={
        "title": "Updated Task",
        "description": "This task does not exist.",
        "status": "in work",
        "user_id": 1
    })
    assert response.status_code == 404

def test_delete_task_not_found(client):
    response = client.delete("/tasks/99999999-9999-9999-9999-999999999999/")
    assert response.status_code == 404
    assert response.json() == {"detail": "Task not found"}