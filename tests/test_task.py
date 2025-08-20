def test_create_task(client):
    response = client.post("/tasks/", json={
        "title": "Test Task",
        "description": "This is a test task.",
        "status": "create",
        "user_id": 1
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"

def test_get_task(client, get_random_uuid_in_db):
    response = client.get(f"/tasks/{get_random_uuid_in_db}")
    assert response.status_code == 200
    assert "title" in response.json()

def test_update_task(client, get_random_uuid_in_db):
    response = client.put(f"/tasks/{get_random_uuid_in_db}", json={
        "title": "Updated Task",
        "description": "This task has been updated.",
        "status": "in work",
        "user_id": 1
    })
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"

def test_delete_task(client, get_random_uuid_in_db):
    response = client.delete(f"/tasks/{get_random_uuid_in_db}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Task deleted successfully"}