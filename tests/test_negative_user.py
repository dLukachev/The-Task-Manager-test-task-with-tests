def test_alredy_use_username(client):
    # предварительно создаем пользователя , который будет конфликтовать с новым
    user = client.post("/users/", json={
        "username": "testuser_pytest",
        "email": "haha"})
    
    response = client.post("/users/", json={
        "username": "testuser_pytest",
        "email": "new_email@mail.ru"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "User with this username or email already exists."}

def test_alredy_use_email(client):
    # предварительно создаем пользователя , который будет конфликтовать с новым
    user = client.post("/users/", json={
        "username": "testuser_pytest",
        "email": "haha"})
    
    response = client.post("/users/", json={
        "username": "new_username",
        "email": "haha"
    })
    assert response.status_code == 400
    assert response.json() == {"detail": "User with this username or email already exists."}

def test_id_found(client):
    response = client.get("/users/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_put_user_not_found(client):
    response = client.put("/users/9999", json={
        "username": "updateduser_pytest",
        "email": "123@mail.ru"
        })
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_delete_user_not_found(client):
    response = client.delete("/users/9999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}

def test_create_user_with_invalid_data(client):
    response = client.post("/users/", json={
        "email": "invalid_email"
    })
    assert response.status_code == 422
    assert "detail" in response.json()