# Auth0 Application Deletion

In the event you want to delete all things related to an application/client within Auth0, here is something you can use.

This is an application to be able to delete all things associated with an application/client id. This should be used in the event you have a client/application that you want to delete and would like all things associated with it deleted (Connections, Users, etc...)

## Flow

These operations are hitting the Auth0 API

* Perform GET /api/v2/clients/{id} with the `client_id` to ensure that the client/application exists

  * if no result is found display message about client/application not being found

* Perform GET /api/v2/connections to find all connections that only have client/application id associated with it and store the list of connection ids

  * if no connection is found display message about no connections

* Perform GET /api/v2/users to find all users associated with a connection and store the list of user ids

  * if no users associated display message about no users associated with the connection id

* Perform DELETE /api/v2/users/{id} for users list. **Note** there is no [bulk delete](https://community.auth0.com/t/is-there-a-way-to-bulk-delete-users/10832) users endpoint. Should batch delete requests to not exceed Auth0's [rate limits](https://auth0.com/docs/policies/rate-limits#management-api-v2)

* Perform DELETE /api/v2/connections/{id} for connections list

* Perform DELETE /api/v2/clients/{id} for application

**Note:** All of the operations above have an option to log to console and a file the requests being made as well as the results. By default the operations will only be printed to the console.