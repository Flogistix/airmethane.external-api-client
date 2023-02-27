<p align="center">
<img src="./images/airmethane-logo.png" alt="Air Methane"/>
</p>

# AirMethane External API

#### Quickstart for consuming the API - Examples
- [Python](examples/python/)
- [BASH](examples/bash/)
- [GUI Client (Insomnia)](examples/insomnia%20collection/)

### Accessing the API
- Base dev URL: `https://dev-api.axil.ai/airmethane/external/inspections`
- Base prod URL: `https://api.axil.ai/airmethane/external/inspections`

The API is used by creating a path with your desired parameters and appending them to the base URLs above. The format looks like: 
```
<base_url>/<parameter1>/<parameter1_value>/<parameter1>/<parameter2_value>/...
```

Details for how to use the parameters, what they represent, and how to interpret the responses are below.

## GET external/inspections 
Retrieve inspections by user, org, site, inspection date, leak ID, or inspection ID. Order of parameters in the path does NOT matter. This endpoing is intended for Air Methane customer usage only. 

### Get all inspections a user has access to
```
GET external/inspections/
```
### Get inspections for a specific org
```
GET external/inspections/orgs/{orgid}
```
### Get inspections for a specific site
```
GET external/inspections/orgs/{orgid}/sites/{siteId}
```
### Get inspections for a specific date range
```
GET external/inspections/startDate/{startDate}/endDate/{endDate}
```
Dates must be in ISO format YYYY-MM-DD
### Get inspections for a specific inspection ID
```
GET external/inspections/inspectionId/{inspectionId}
```
### Get inspections for a specific leak ID
```
GET external/inspections/leakId/{leakId}
```
### Combining all options to one path (order NOT important!)
```
GET external/inspections/orgs/{orgid}/sites/{siteId}/leakId/{leakId}/startDate/{startDate}/endDate/{endDate}
```

Valid Response with data:
```JSON
{
    "inspections": [
        {
            "customerId": 224,
            "customerLocationId": 1510,
            "customerName": "Earthstone Operating",
            "customerLocationName": "Black River 3-10 Fed Com WCA 4H",
            "inspectionInformation": [
                {
                    "inspectionId": 83,
                    "inspectionDate": "2021-08-24",
                    "leaks": [
                        {
                            "leakId": null,
                            "tagNumber": null,
                            "fileType": "image",
                            "imageUrl": "https://airmethane-file-storage-dev.s3.amazonaws.com/ChisholmEnergyOperating/BlackRiver3-10FedComWCA4H/image/StandardPic/08-24-2021/BlackRiver3-10FCBatteryLeak2Repair.PNG?presignedurl",
                            "name": "Black River 3-10 FC Battery Leak 2 Repair.PNG",
                            "sensorType": "Standard Pic"
                        }
                    ]
                }
            ]
        },
        {
            "customerId": 224,
            "customerLocationId": 846,
            "customerName": "Earthstone Operating",
            "customerLocationName": "Dark Canyon 15 22 2H 3H & 4H",
            "inspectionInformation": [
                {
                    "inspectionId": 85,
                    "inspectionDate": "2021-08-24",
                    "leaks": [
                        {
                            "leakId": null,
                            "tagNumber": null,
                            "fileType": "image",
                            "imageUrl": "https://airmethane-file-storage-dev.s3.amazonaws.com/ChisholmEnergyOperating/DarkCanyon15222H3H%264H/image/StandardPic/08-24-2021/DarkCanyon15-22StateComBatteryRe-inspectionLeak3.PNG?presignedurl",
                            "name": "Dark Canyon 15-22 State Com Battery Re-inspection Leak 3.PNG",
                            "sensorType": "Standard Pic"
                        },
                        {
                            "leakId": null,
                            "tagNumber": null,
                            "fileType": "image",
                            "imageUrl": "https://airmethane-file-storage-dev.s3.amazonaws.com/ChisholmEnergyOperating/DarkCanyon15222H3H%264H/image/StandardPic/08-24-2021/DarkCanyon15-22StateComBatteryRe-inspectionLeak2Repair.PNG?presignedurl",
                            "name": "Dark Canyon 15-22 State Com Battery Re-inspection Leak 2 Repair.PNG",
                            "sensorType": "Standard Pic"
                        }
                    ]
                }
            ]
        }
    ],
    "executionTime": "8.85 sec"
}
```
If there are no inspections:
```JSON
{
    "inspections": [],
    "executionTime": "400.74 ms"
}
```

### Response Payload Glossary:
* "customerId": 
	- data type: integer
	- description: internal ID of customer
	- parameter path: /orgs/
* "customerLocationId": 
	- data type: integer
	- description: internal ID of location
	- parameter path: /sites/
* "customerName": 
	- data type: string
	- description: internal name for the customer
	- parameter path: none
* "customerLocationName": 
	- data type: string
	- description: internal name for the location on which the inspection occurred
	- parameter path: none
* "inspectionInformation": 
	- data type: list
	- description: contains list of inspection information
	- parameter path: none
* "inspectionId": 
	- data type: integer
	- description: internal ID for the inspection conducted
	- parameter path: /inspectionId/
* "inspectionDate": 
	- data type: date formatted YYYY-MM-DD
 	- description: date inspection occurred
 	- parameter path: /startDate/ and /endDate/
* "leaks":
	- data type: list
	- description: list of leaks and images associated with the inspection ID
	- parameter path: /leakId/
* "leakId":
	- data type: integer
	- description: internal ID for a given leak (can be null if no leak found)
	- parameter path: /leakId/
* "tagNumber": 
	- data type: integer 
	- description: internal ID for a tagged leak and correlates 1:1 with an image
	- parameter path: /tagNumber/
* "fileType": 
	- data type: string
	- description: type of file (usually "image")
	- parameter path: none
* "imageUrl": 
	- data type: string
	- description: presigned S3 URL that is valid for one hour to retrieve the image
	- parameter path: none
* "name": 
	- data type: string
	- description: file name of the image
	- parameter path: none
* "sensorType": 
	- data type: string
	- description: type of sensor used to collect image
	- parameter path: none


### Response Codes:
**200**: Inspections list  
**400**: Bad Request Error - the path is malformed  
**401**: Unauthorized Error    
**403**: Forbidden Error - the request is missing email/token  
**404**: Not Found Error   
**500**: Unknown Error - hopefully this one won't be returned!  
**503**: Upstream Service Error 
