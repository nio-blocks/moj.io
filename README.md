Mojio
===========

Get information about your [moj.io](http://moj.io) connected vehicles. There are two blocks:
 * [MojioVehicles](#mojiovehicles)
 * [MojioEvents](#mojioevents)

Properties
--------------
 * **API Key** - This is your API token returned by Moj.io. See the [Getting API Access](#getting-api-access) section for details

Dependencies
----------------
None

Commands
----------------
None

Input
-------
Input signals will trigger REST polls.

Getting API Access
---------
Right now, you will need to manually go through the OAuth handshake to grant the nio application access to your moj.io account. The token you get as a response is the token that the block gets configured with. These tokens typically expire after a month, so at that point the block will start raising `401` errors until the handshake is manually completed again.

### To get your access token
 1. Go to the [Moj.io Developer Dashboard](https://developer.moj.io/dashboard)
 2. Log in and then navigate to the REST API Documentation
 3. Select the proper Live or Sandbox setting at the top of the page. If you want real data, use Live. If you want to use the Moj.io Vehicle Simulator, use Sandbox
 4. Your API Token will appear in the text field to the left of the orange Set Token button

MojioVehicles
===========

Output
---------
One signal for each poll for each vehicle that the API Key has access to. The schema for the vehcile response can be found through the [Moj.io Schema API Call](https://api.moj.io/v1/Schema?entityType=Vehicle).

MojioEvents
===========

Output
---------
One signal for each poll for each **new** event since the last poll. The schema for the vehcile response can be found through the [Moj.io Schema API Call](https://api.moj.io/v1/Schema?entityType=Event).

