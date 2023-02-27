## Air Methane GET Inspections Python Client

This client connects to Auth0 based on your client ID and secret, makes a request to the Flogistix Air Methane external Inspections API endpoint based on given parameters, then stores the returned payload into a local JSON file for further processing.

### To Set up the Client
Create a virtual environment for the client:
```
$ python3 -m venv .venv
```
After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.
```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:
```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.
```
$ pip install -r requirements.txt
```

### Set up your environment variables for your Auth0 credentials, given by Flogistix staff
Contact support@flogistix.com for help with your credentials.

#### MacOS/Linux
```Shell
export AUTH0_CLIENT_ID="<client_id>"
export AUTH_CLIENT_SECRET="<client_secret>"
```

#### Windows/Powershell
```Powershell
[System.Environment]::SetEnvironmentVariable('AUTH0_CLIENT_ID','<client_id>')
[System.Environment]::SetEnvironmentVariable('AUTH_CLIENT_SECRET','<client_secret>')
```

### Running the Client
Execute the GET request to retrieve inspections from given arguments by running the Python script with a set of arguments:
```
$ python3 get_inspections.py -o <orgs> -s <sites> -d <startDate> -b <endDate> -i <inspectionId> -l <leakId>
```

See the [README at the base of the repo](../../README.md) for more information on these arguments and how the API functions.