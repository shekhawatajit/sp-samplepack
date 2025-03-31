import json
import os
from auth.auth import get_access_token
from users.user_tasks import create_user, update_user, user_exists

# Constants for replacement
NEW_DOMAIN = "saffronspark.in"
NEW_ORG_NAME = "Saffron Spark"

def process_users(file_path):
    """
    Reads the JSON file, replaces domain and organization name, and processes users.
    """
    try:
        # Read the JSON file
        with open(file_path, "r") as file:
            users = json.load(file)

        # Get access token
        token = get_access_token()

        # Process each user
        for user in users:
            # Replace domain and organization name
            user["userPrincipalName"] = user["userPrincipalName"].replace("domain", NEW_DOMAIN)
            user["companyName"] = NEW_ORG_NAME

            # Check if the user exists
            if user_exists(token, user["userPrincipalName"]):
                print(f"User {user['userPrincipalName']} exists. Updating...")
                update_user(token, user)
            else:
                print(f"User {user['userPrincipalName']} does not exist. Creating...")
                create_user(token, user)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Path to the JSON file
    json_file_path = os.path.join(os.path.dirname(__file__), "users", "users.json")

    # Process users
    process_users(json_file_path)