# Register your third party application on http://developers.monzo.com by logging in with your personal
# Monzo account. Copy this file into config.py, and enter your credentials into the file.
MONZO_CLIENT_ID = "oauth2client_acc_00009exXcgwfD8OeE9yVu5"
MONZO_CLIENT_SECRET = "mnzpub.eyJhbGciOiJFUzI1NiIsInR5cCI6IkpXVCJ9.eyJlYiI6Ii9NL1gzdVdORmtiZ2dXQVVpZ3gxIiwianRpIjoiYWNjdG9rXzAwMDA5ZXhZbmwySVJSM2Y0WXhFVHgiLCJ0eXAiOiJhdCIsInYiOiI1In0.kjZmju9yFc25g1BTO2N9szMuqznsSvokjGwYsM0hdU6214h1l2vxjtrH2MgOTxWZ7aNsYEqjM4Od-wg5ivon7Q"

# Configurations you should not need to change.
MONZO_OAUTH_HOSTNAME = "auth.monzo.com"
MONZO_API_HOSTNAME = "api.monzo.com"
MONZO_RESPONSE_TYPE = "code"
MONZO_AUTH_GRANT_TYPE = "authorization_code"
MONZO_REFRESH_GRANT_TYPE = "refresh_token"
MONZO_OAUTH_REDIRECT_URI = "http://127.0.0.1:21234/" # For receiving the auth code, not currently used.
MONZO_CLIENT_IS_CONFIDENTIAL = True
# If your application runs on a backend server with client secret hidden from user, it should be registered
# as confidential and will have the ability to refresh access tokens.
