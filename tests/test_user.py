def test_create_user(client):
    response = client.post("/users/", json={
        "username": "testuser_pytest",
        "email": "testuser@mail.ru"
    })
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "username": "testuser_pytest",
        "email": "testuser@mail.ru"
    }

def test_get_user(client, user_id=1):
    response = client.get(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {
        "id": user_id,
        "username": "testuser_pytest",
        "email": "testuser@mail.ru"
        }

def test_put_user(client, user_id=1):
    response = client.put(f"/users/{user_id}", json={
        "username": "updateduser_pytest",
        "email": "updateduser_pytest@mail.ru"
        }
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": user_id,
        "username": "updateduser_pytest",
        "email": "updateduser_pytest@mail.ru"
        }
    
def test_delete_user(client, user_id=1):
    response = client.delete(f"/users/{user_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "User deleted successfully"}