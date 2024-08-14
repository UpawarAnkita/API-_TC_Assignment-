# This repository contains tests for a basic authentication API using requests library.


Tests Included

Login Success: Verifies successful login with valid credentials.
Login Invalid Credentials: Checks response for invalid login attempts.
Login Missing Credentials: Tests login response when credentials are missing.
Logout Success: Confirms successful logout using a valid token.
Logout No Auth: Validates response when logout is attempted without authentication.
Get User Details Success: Fetches user details with a valid token.
Get User Details Unauthorized: Tests response when fetching user details without authentication.
Get User Details Not Found: Ensures correct handling of non-existent user IDs.

Usage
Ensure your API is running locally at http://127.0.0.1:5000.

Run the tests using Python:
python server.py
python request.py


