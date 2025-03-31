import requests

# Microsoft Graph API endpoints
GRAPH_API_ENDPOINT = "https://graph.microsoft.com/v1.0/users"

def user_exists(access_token, user_principal_name):
    """
    Checks if a user exists in Microsoft Entra ID.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
    }
    response = requests.get(f"{GRAPH_API_ENDPOINT}/{user_principal_name}", headers=headers)
    return response.status_code == 200

def create_user(access_token, user_data):
    """
    Creates a new user in Microsoft Entra ID.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    response = requests.post(GRAPH_API_ENDPOINT, headers=headers, json=user_data)
    if response.status_code == 201:
        print(f"User {user_data['userPrincipalName']} created successfully!")
    else:
        print(f"Failed to create user {user_data['userPrincipalName']}.")
        print(f"Status Code: {response.status_code}")
        print(response.json())

def update_user(access_token, user_data):
    """
    Updates an existing user in Microsoft Entra ID.
    """
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    user_principal_name = user_data["userPrincipalName"]
    response = requests.patch(f"{GRAPH_API_ENDPOINT}/{user_principal_name}", headers=headers, json=user_data)
    if response.status_code == 204:
        print(f"User {user_principal_name} updated successfully!")
    else:
        print(f"Failed to update user {user_principal_name}.")
        print(f"Status Code: {response.status_code}")
        print(response.json())
        