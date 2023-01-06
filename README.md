
# Getting Started with Verizon

## Introduction

The Verizon Edge Discovery Service API can direct your application clients to connect to the optimal service endpoints for your Multi-access Edge Computing (MEC) applications for every session. The Edge Discovery Service takes into account the current location of a device, its IP anchor location, current network traffic and other factors to determine which 5G Edge platform a device should connect to.

Verizon Terms of Service: [https://staging.5gedge.verizon.com/business/5g-edge-portal/legal.html](https://staging.5gedge.verizon.com/business/5g-edge-portal/legal.html)

## Building

You must have Python `3 >=3.7, <= 3.10` installed on your system to install and run this SDK. This SDK package depends on other Python packages like pytest, jsonpickle etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK. To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&step=installDependencies)

## Installation

The following section explains how to use the verizon library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&projectName=verizon&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&projectName=verizon&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&projectName=verizon&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&projectName=verizon&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from verizon.verizon_client import VerizonClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&projectName=verizon&libraryName=verizon.verizon_client&className=VerizonClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Verizon-Python&projectName=verizon&libraryName=verizon.verizon_client&className=VerizonClient&step=runProject)

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `vz_m2m_token` | `string` | M2M Session Token |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 60** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT', 'GET', 'PUT']** |
| `oauth_client_id` | `string` | OAuth 2 Client ID |
| `oauth_client_secret` | `string` | OAuth 2 Client Secret |
| `oauth_token` | `OauthToken` | Object for storing information about the OAuth token |
| `oauth_scopes` | `OauthScopeEnum` |  |

The API client can be initialized as follows:

```python
from verizon.verizon_client import VerizonClient
from verizon.configuration import Environment

client = VerizonClient(
    vz_m2m_token='VZ-M2M-Token',
    oauth_client_id='OAuthClientId',
    oauth_client_secret='OAuthClientSecret',
    oauth_scopes = [OauthScopeEnum.DISCOVERYREAD, OauthScopeEnum.SERVICEPROFILEREAD],
    environment=Environment.PRODUCTION,)
```

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| production | **Default** |
| staging | - |

## Authorization

This API uses `OAuth 2 Client Credentials Grant`.

## Client Credentials Grant

Your application must obtain user authorization before it can execute an endpoint call in case this SDK chooses to use *OAuth 2.0 Client Credentials Grant*. This authorization includes the following steps

The `fetch_token()` method will exchange the OAuth client credentials for an *access token*. The access token is an object containing information for authorizing client requests and refreshing the token itself.

You must pass the [scopes]($h/__authorize/Scopes) for which you need permission to access.

```python
try:
    client.auth_managers['global'].fetch_token()
except OauthProviderException as ex:
    # handle exception
except APIException as ex:
    # handle exception
```

The client can now make authorized endpoint calls.

### Scopes

Scopes enable your application to only request access to the resources it needs while enabling users to control the amount of access they grant to your application. Available scopes are defined in the `OauthScopeEnum` enumeration.

| Scope Name | Description |
|  --- | --- |
| `DISCOVERYREAD` | Grant read-only access to discovery data |
| `SERVICEPROFILEREAD` | Grant read-only access to service profile data |
| `SERVICEPROFILEWRITE` | Grant write access to service profile data |
| `SERVICEREGISTRYREAD` | Grant read-only access to Service registry data |
| `SERVICEREGISTRYWRITE` | Grant write access to Service registry data |
| `TS_MEC_FULLACCESS` | Full access for /serviceprofiles and /serviceendpoints. |
| `TS_MEC_LIMITACCESS` | Limited access. Will not allow use of /serviceprofiles and /serviceendpoints but will allow discovery. |
| `TS_APPLICATION_RO` |  |
| `EDGEDISCOVERYREAD` |  |
| `EDGESERVICEPROFILEREAD` |  |
| `EDGESERVICEPROFILEWRITE` |  |
| `EDGESERVICEREGISTRYREAD` |  |
| `EDGESERVICEREGISTRYWRITE` |  |
| `READ` | read access |
| `WRITE` | read/write access |

### Storing an access token for reuse

It is recommended that you store the access token for reuse.

```python
# store token
save_token_to_database(client.config.oauth_token)
```

### Creating a client from a stored token

To authorize a client from a stored access token, just set the access token in Configuration along with the other configuration parameters before creating the client:

```python
client = VerizonClient()
client.config.oauth_token = load_token_from_database()
```

### Complete example

```python
from verizon.verizon_client import VerizonClient
from verizon.models.oauth_scope_enum import OauthScopeEnum
from verizon.exceptions.oauth_provider_exception import OauthProviderException

from verizon.exceptions.api_exception import APIException

# function for storing token to database
def save_token_to_database(token):
    # code to save the token to database

# function for loading token from database
def load_token_from_database():
    # load token from database and return it (return None if no token exists)
    pass

from verizon.verizon_client import VerizonClient
from verizon.configuration import Environment

client = VerizonClient(
    vz_m2m_token='VZ-M2M-Token',
    oauth_client_id='OAuthClientId',
    oauth_client_secret='OAuthClientSecret',
    oauth_scopes = [OauthScopeEnum.DISCOVERYREAD, OauthScopeEnum.SERVICEPROFILEREAD],
    environment=Environment.PRODUCTION,)
# obtain access token, needed for client to be authorized
previous_token = load_token_from_database()
if previous_token:
    # restore previous access token
    client.config.oauth_token = previous_token
else:
    # obtain new access token
    try:
        token = client.auth_managers['global'].fetch_token()
        save_token_to_database(token)
    except OauthProviderException as ex:
        # handle exception
    except APIException as ex:
        # handle exception

# the client is now authorized and you can use controllers to make endpoint calls
```

## List of APIs

* [5G Edge Platforms](doc/controllers/5g-edge-platforms.md)
* [Service Profiles](doc/controllers/service-profiles.md)
* [Device Management](doc/controllers/device-management.md)
* [Service Endpoints](doc/controllers/service-endpoints.md)
* [Device Groups](doc/controllers/device-groups.md)
* [Session Management](doc/controllers/session-management.md)
* [Connectivity Callbacks](doc/controllers/connectivity-callbacks.md)
* [Service Plans](doc/controllers/service-plans.md)
* [Devices Locations](doc/controllers/devices-locations.md)
* [Device Location Callbacks](doc/controllers/device-location-callbacks.md)
* [Software Management Subscriptions V1](doc/controllers/software-management-subscriptions-v1.md)
* [Firmware V1](doc/controllers/firmware-v1.md)
* [Software Management Licenses V1](doc/controllers/software-management-licenses-v1.md)
* [Software Management Callbacks V1](doc/controllers/software-management-callbacks-v1.md)
* [Software Management Reports V1](doc/controllers/software-management-reports-v1.md)
* [Account Requests](doc/controllers/account-requests.md)
* [Devices Location Subscriptions](doc/controllers/devices-location-subscriptions.md)
* [Software Management Licenses V2](doc/controllers/software-management-licenses-v2.md)
* [Campaigns V2](doc/controllers/campaigns-v2.md)
* [Software Management Callbacks V2](doc/controllers/software-management-callbacks-v2.md)
* [Software Management Reports V2](doc/controllers/software-management-reports-v2.md)
* [Client Logging](doc/controllers/client-logging.md)
* [Software Management Reports V3](doc/controllers/software-management-reports-v3.md)
* [Account Devices](doc/controllers/account-devices.md)
* [Software Management Callbacks V3](doc/controllers/software-management-callbacks-v3.md)
* [SIM Securefor Io T Licenses](doc/controllers/sim-securefor-io-t-licenses.md)
* [Diagnostics Observations](doc/controllers/diagnostics-observations.md)
* [Diagnostics Settings](doc/controllers/diagnostics-settings.md)
* [Cloud Connector Subscriptions](doc/controllers/cloud-connector-subscriptions.md)
* [Device Reports](doc/controllers/device-reports.md)
* [MEC Sites](doc/controllers/mec-sites.md)
* [Service Launch Requests](doc/controllers/service-launch-requests.md)
* [Service Instances](doc/controllers/service-instances.md)
* [Software Management Licenses V3](doc/controllers/software-management-licenses-v3.md)
* [Campaigns V3](doc/controllers/campaigns-v3.md)
* [Firmware V3](doc/controllers/firmware-v3.md)
* [Account Subscriptions](doc/controllers/account-subscriptions.md)
* [Diagnostics Subscriptions](doc/controllers/diagnostics-subscriptions.md)
* [Diagnostics Callbacks](doc/controllers/diagnostics-callbacks.md)
* [Device Service Management](doc/controllers/device-service-management.md)
* [Hyper Precise Location Callbacks](doc/controllers/hyper-precise-location-callbacks.md)
* [Anomaly Settings](doc/controllers/anomaly-settings.md)
* [Anomaly Triggers](doc/controllers/anomaly-triggers.md)
* [Service Launch Profiles](doc/controllers/service-launch-profiles.md)
* [Service Onboarding](doc/controllers/service-onboarding.md)
* [Software Management Subscriptions V2](doc/controllers/software-management-subscriptions-v2.md)
* [Software Management Subscriptions V3](doc/controllers/software-management-subscriptions-v3.md)
* [Diagnostics History](doc/controllers/diagnostics-history.md)
* [Server Logging](doc/controllers/server-logging.md)
* [Performance Metrics](doc/controllers/performance-metrics.md)
* [Service Metadata](doc/controllers/service-metadata.md)
* [CSP Profiles](doc/controllers/csp-profiles.md)
* [Service Claims](doc/controllers/service-claims.md)
* [OAuth Authorization](doc/controllers/oauth-authorization.md)
* [Accounts](doc/controllers/accounts.md)
* [SMS](doc/controllers/sms.md)
* [Exclusions](doc/controllers/exclusions.md)
* [Targets](doc/controllers/targets.md)
* [Repositories](doc/controllers/repositories.md)
* [Token](doc/controllers/token.md)

## Classes Documentation

* [Utility Classes](doc/utility-classes.md)
* [HttpResponse](doc/http-response.md)
* [HttpRequest](doc/http-request.md)

