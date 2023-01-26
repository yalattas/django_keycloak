## setup

1. create a `realm` and name it `main`

2. create a client in `main` realm and name it `backend_service`
    1. check `Client authentication` and check `Service accounts roles`

3. insert client credentials in `settings.py`

4. add client URL to valid redirects URIs (EX: `https://oauth.pstmn.io/v1/callback`)

> https://oauth.pstmn.io/v1/callback is representing client side URL. For example, if frontend is calling backend directly without having token, then client must be whitelisted and pass in the API call from frontend -> backend -> keycloak -> backend -> frontend
