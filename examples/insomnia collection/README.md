# Air Methane GET Inspections using a GUI Client (Insomnia)

This JSON file contains an Insomnia collection that will allow you to connect to Auth0 based on your client ID and secret, store the token in the base environment token variable, and use the ```GET Ext Inspections``` request to hit the Flogistix Air Methane external Inspections API endpoint based on given parameters.

## Setup

### Download and install Insomnia
Follow the instructions on their website: https://insomnia.rest/download

### Import the Collection
Once you have Insomnia installed and open, import ```Insomnia.json``` as a collection into your workspace.

For detailed instructions, see their website: https://docs.insomnia.rest/insomnia/import-export-data

### Adjust Client ID and Secret
Once you have the collection imported, open the ```Auth0 - Get Token``` request from the sidebar. Modify the JSON to include your client ID and secret by replacing the appropriate values enclosed in angle brackets, ```<client_id>``` and ```<client_secret>```, keeping the surrounding double quotes.

Contact support@flogistix.com for help with your credentials.

```JSON
{
		"client_id": "<client_id>",
		"client_secret": "<client_secret>",
		"audience": "https://api.axil.ai",
		"grant_type": "client_credentials"
}
```

### Run Get Ext Inspections
Modify the URL path after ```/external/inspections/``` to include your parameters. The pattern is {argument name}/{argument value}, like so:
```
orgs/{orgid}/sites/{siteId}/inspectionDateAfter/{inspectionDateAfter}/inspectionDateBefore/{inspectionDateBefore}
```

For more information on these parameters, see the [README at the base of the repo](../../README.md).

Hit Send to run the request and receive the response. For more information on sending requests using Insomnia, see: https://docs.insomnia.rest/insomnia/send-your-first-request
