# notification-monolithic-backend
[![Build Status](https://gitlab.com/pprints/pprints-monolithic-backend/badges/dev/pipeline.svg)](https://gitlab.com/pprints/pprints-monolithic-backend/-/commits/dev)


monolithic Python Django backend

## Getting started

### Setting up

Below command will pull couple of official Docker images `nginx` and `postgres` and build up third image locally by pull official `python` image and combine this project with it
```
docker-compose up --build
```

### federated identity

1. visit `iam-backend` endpoint and create your first `realm` instance at [http://localhost:8080/admin](http://localhost:8080/admin)
> use the environment variables of admin credentials or ask the administrator
2. after creating the `realm`. from the left side menu, go To `clients` -> create a client -> name your client and mark down your `Client ID`
3. visit your created `relam` -> `settings` -> activate `user authentication` and select `service accounts role` OR activate `Authorization`
4. on the same page, visit `credentials` and save `Client Secret` and copy the secret, then put it in `settings.py` -> `CLIENT_SECRET_KEY`
5. `client-role` in `settings.py` should be same as follows`client-role` OR look for the name in the client `Roles` tab
6. in `client` page, visit `Service account role` tab and assign a role `manage-users`


### generate JWT token
[http://localhost:8080/auth/realms/<REALM_NAME>/.well-known/openid-configuration](http://localhost:8080/auth/realms/<REALM_NAME>/.well-known/openid-configuration)