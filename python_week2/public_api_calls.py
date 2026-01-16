import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def get_all_users():
    url = f"{BASE_URL}/users"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        users = response.json()
        for user in users:
            print(user)


def get_user_by_id(user_id):
    url = f"{BASE_URL}/users/{user_id}"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        user = response.json()
        print(user)


def create_post(title, body, user_id):
    url = f"{BASE_URL}/posts"
    headers = {"Content-type": "application/json"}
    data = {"title":title,"body":body,"userID":user_id}
    response = requests.post(url,json=data,headers=headers)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 201:
        print("Post created")
        print("Response: ",response.json())


def update_post_full(post_id, title, body, user_id):
    url = f"{BASE_URL}/posts/{post_id}"
    headers = {"Content-type": "application/json"}
    data = {"title":title,"body":body,"userID":user_id}
    response = requests.put(url,json=data,headers=headers)
    print(f"Status Code: {response.status_code}")
    if response.status_code in (200,204):
        print("Post Updated")
        if response.json(): print("Response: ",response.json())
    else:
        print(f"Status Code: {response.status_code}")


def update_post_partial(post_id, data):
    url = f"{BASE_URL}/posts/{post_id}"
    headers = {"Content-type": "application/json"}
    response = requests.patch(url,json=data,headers=headers)
    print(f"Status Code: {response.status_code}")
    if response.status_code in (200,204):
        print("Post Updated")
        if response.json(): print("Response: ",response.json())


def delete_post(post_id):
    """DELETE /posts/{id}"""
    url = f"{BASE_URL}/posts/{post_id}"
    headers = {"Content-type": "application/json"}
    response = requests.delete(url,headers=headers)
    print(f"Status Code: {response.status_code}")
    if response.status_code in (200,204):
        print("Post Deleted")
        #if response.json(): print("Response: ",response.json())


if __name__ == "__main__":
    get_all_users()
    get_user_by_id(1)

    create_post(
        title="Sample Title",
        body="Sample body",
        user_id=1
    )

    update_post_full(
        post_id=1,
        title="Updated Title",
        body="Updated body",
        user_id=1
    )

    update_post_partial(
        post_id=1,
        data={"title": "Partially Updated Title"}
    )

    delete_post(post_id=1)
