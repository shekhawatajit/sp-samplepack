import os
from msal import PublicClientApplication
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Azure AD App Registration details from environment variables
CLIENT_ID = os.getenv("CLIENT_ID")
TENANT_ID = os.getenv("TENANT_ID")

def get_access_token():
    """
    Authenticate using interactive login and return an access token.
    """
    app = PublicClientApplication(
        CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{TENANT_ID}",
    )
    # Scopes required for creating users
    scopes = ["User.ReadWrite.All"]
    accounts = app.get_accounts()

    if accounts:
        # If a cached account exists, use it
        result = app.acquire_token_silent(scopes, account=accounts[0])
    else:
        # Perform interactive login
        result = app.acquire_token_interactive(scopes=scopes)

    if "access_token" in result:
        return result["access_token"]
    else:
        raise Exception("Failed to acquire access token: " + str(result))