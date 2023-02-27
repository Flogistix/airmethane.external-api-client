# Air Methane GET Inspections using BASH

This script connects to Auth0 based on your client ID and secret, makes a request to the Flogistix Air Methane external Inspections API endpoint based on given parameters, then stores the returned payload into a local JSON file for further processing.

## Setup

### Install jq
Install jq on your system in accordance with the downloads page: https://stedolan.github.io/jq/download/

Example installation commands below.

#### OS X
```
brew install jq
```

#### Linux
```
sudo apt-get install jq
```

### Set your environment variables
Contact support@flogistix.com for help with your credentials.

#### OS X / Linux
```Shell
export CLIENT_ID="<client_id"
export CLIENT_SECRET="client_secret"
```

## Run script
Navigate to the directory containing get_inspections, execute from the command line and pass desired arguments
```Shell
./get_inspections -o <customerId> -s <customerLocationId> -d <startDate> -b <endDate> -i <inspectionId> -l <leakId>
```

See the [README at the base of the repo](../../README.md) for more information on these arguments and how the API functions.