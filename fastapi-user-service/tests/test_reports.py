import pytest

@pytest.mark.asyncio
async def test_protected_route_without_token(async_client):
    response = await async_client.get("/api/v1/reports/users-by-department/download")
    assert response.status_code == 403 or response.status_code == 401

@pytest.mark.asyncio
async def test_protected_route_with_token(async_client):
    # Login to get token
    login_response = await async_client.post(
        "api/v1/auth/login",
        json={"username": "test-user"},
    )
    assert login_response.status_code == 200
    token = login_response.json()["access_token"]
    # Access protected report
    response = await async_client.get(
        "/api/v1/reports/users-by-department/download",
        headers={"Authorization": f"Bearer {token}"},
    )
    assert response.status_code == 200
    assert response.headers["content-type"].startswith(
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )