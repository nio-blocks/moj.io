MojioEvents
===========
Retrieve each new event from Mojio.

Properties
----------
- **creds**: Credentials to connect to Mojio API.
- **include_query**: Whether to include queries in request to Mojio.
- **polling_interval**: How often Mojio is polled. When using more than one query. Each query will be polled at a period equal to the *polling interval* times the number of queries.
- **queries**: Inherited from base rest polling block but not used.
- **retry_interval**: When a url request fails, how long to wait before attempting to try again.
- **retry_limit**: Number of times to retry on a poll.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: One signal for each poll for each **new** event since the last poll. The schema for the vehicle response can be found through the [Moj.io Schema API Call](https://api.moj.io/v1/Schema?entityType=Event).

Commands
--------
None

Getting API Access
------------------
Right now, you will need to manually go through the OAuth handshake to grant the nio application access to your moj.io account. The token you get as a response is the token that the block gets configured with. These tokens typically expire after a month, so at that point the block will start raising `401` errors until the handshake is manually completed again.
### To get your access token
 1. Go to the [Moj.io Developer Dashboard](https://developer.moj.io/dashboard)
 2. Log in and then navigate to the REST API Documentation
 3. Select the proper Live or Sandbox setting at the top of the page. If you want real data, use Live. If you want to use the Moj.io Vehicle Simulator, use Sandbox
 4. Your API Token will appear in the text field to the left of the orange Set Token button

MojioVehicles
=============
Get information about each vehicle available on Mojio.

Properties
----------
- **creds**: Credentials to connect to Mojio API.
- **include_query**: Whether to include queries in request to Mojio.
- **polling_interval**: How often Mojio is polled. When using more than one query. Each query will be polled at a period equal to the *polling interval* times the number of queries.
- **queries**: Inherited from base rest polling block but not used.
- **retry_interval**: When a url request fails, how long to wait before attempting to try again.
- **retry_limit**: Number of times to retry on a poll.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: One signal for each poll for each vehicle that the API Key has access to. The schema for the vehicle response can be found through the [Moj.io Schema API Call](https://api.moj.io/v1/Schema?entityType=Vehicle).

Commands
--------
None

Getting API Access
------------------
Right now, you will need to manually go through the OAuth handshake to grant the nio application access to your moj.io account. The token you get as a response is the token that the block gets configured with. These tokens typically expire after a month, so at that point the block will start raising `401` errors until the handshake is manually completed again.
### To get your access token
 1. Go to the [Moj.io Developer Dashboard](https://developer.moj.io/dashboard)
 2. Log in and then navigate to the REST API Documentation
 3. Select the proper Live or Sandbox setting at the top of the page. If you want real data, use Live. If you want to use the Moj.io Vehicle Simulator, use Sandbox
 4. Your API Token will appear in the text field to the left of the orange Set Token button

