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
- Authorization: we use Auth0 to generate a JSON Web Token (JWT) that we use for Bearer authentication. To set up your Auth0 credentials, please contact support@flogistix.com. For how to generate your JWT, please see one of the examples.

The API is used by creating a path with your desired parameters and appending them to the base URLs above. The format looks like: 
```
<base_url>/<parameter1>/<parameter1_value>/<parameter2>/<parameter2_value>/...
```

Details for how to use the parameters, what they represent, and how to interpret the responses are below.

## GET external/inspections 
Retrieve inspections by user, org, site, inspection date, leak ID, or inspection ID. Order of parameters in the path does NOT matter. This endpoint is intended for AirMethane customer usage only. 

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
GET external/inspections/orgs/{customerId}/sites/{customerLocationId}/inspectionId/{inspectionId}/leakId/{leakId}/startDate/{startDate}/endDate/{endDate}
```

Valid Responses:

```JSON
{
    "inspections": [
        {
            "customerId": 1177,
            "customerLocationId": 17889,
            "customerName": "Oil Man",
            "customerLocationName": "MARFA - BOOSTER",
            "inspectionInformation": [
                {
                    "inspectionId": 1574,
                    "inspectionDate": "2022-11-03",
                    "surveyId": "fC",
                    "surveyData": {
                        "Inspection ID": "jC",
                        "Primary Site Contact": null,
                        "Start Time": "00:30",
                        "End Time": "01:40",
                        "Sky Condition": "Mostly Clear",
                        "Ambient Temperature": 23,
                        "Wind Direction": null,
                        "Wind Speed": 23,
                        "Humidity": null,
                        "Barometric Pressure": null,
                        "Viewing Distance": null,
                        "Inspection Method 1": "",
                        "Inspection Method 2": "",
                        "Survey Instrument 1": "Chip & Dip",
                        "Survey Instrument 2": "",
                        "Inspector Id 1": "Yogie Bear",
                        "Inspector Id 2": "",
                        "Operational Status": ""
                    },
                    "leaks": [
                        {
                            "leakId": 40,
                            "tagNumber": "3153524",
                            "fileType": "image",
                            "imageUrl": "https://airmethane-file-storage-dev.s3.amazonaws.com/OilMan/MARFA-BOOSTER/None/FLIROGI/02-02-2023/3153524OGI.jpg?response-content-disposition=attachment%3B%20filename%3D%223153524OGI.jpg%presignedsuffix",
                            "name": "3153524OGI.jpg",
                            "sensorType": "FLIR OGI",
                            "repairInfo": {
                                "id": "fP",
                                "Status": "Complete",
                                "Component": null,
                                "Component Subtype": null,
                                "Component ID": "Grover",
                                "Component Location": "Alley",
                                "Description": "Next to Sesame Street",
                                "Tag #": null,
                                "Video #": null,
                                "Picture #": null,
                                "Leak Rate": 45,
                                "Leak Rate UOM": null,
                                "Due Date": null,
                                "Repair Complete": "11/03/2022",
                                "Verification Date": "11/03/2022",
                                "Repair Methods": "Adjusted",
                                "Additional Repair notes": "Good to go now!",
                                "Repaired By": "Greg Banks"
                            }
                        },
                        {
                            "leakId": null,
                            "tagNumber": null,
                            "fileType": "image",
                            "imageUrl": "https://airmethane-file-storage-dev.s3.amazonaws.com/OilMan/MARFA-BOOSTER/None/StandardPic/02-02-2023/DailyVerificationCheckOGI10.28.22.jpg?response-content-disposition=attachment%3B%20filename%3D%22DailyVerificationCheckOGI10.28.22.jpg%presignedsuffix",
                            "name": "DailyVerificationCheckOGI10.28.22.jpg",
                            "sensorType": "Standard Pic",
                            "repairInfo": null
                        }
                    ]
                }
            ]
        }
    ],
    "executionTime": "41.26 sec"
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

#### Customer Information
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
* "customerLocationName": 
	- data type: string
	- description: internal name for the location on which the inspection occurred


#### Inspection Information
* "inspectionInformation": 
	- data type: JSON array
	- description: contains list of inspection information
* "inspectionId": 
	- data type: integer
	- description: internal ID for the inspection conducted
	- parameter path: /inspectionId/
* "inspectionDate": 
	- data type: string
 	- description: date inspection occurred, formatted YYYY-MM-DD
 	- parameter path: /startDate/ and /endDate/


#### Survey Information
* "Inspection Id": 
	- data type: integer
	- description: internal ID for the inspection conducted
	- parameter path: /inspectionId/
* "Primary Site Contact": 
	- data type: string
 	- description: name of primary contact for the location
* "Inspection Date": 
	- data type: date
 	- description: date inspection occurred, formatted YYYY-MM-DD
 	- parameter path: /startDate/ and /endDate/
* "Start Time": 
	- data type: string
 	- description: beginning time inspection occurred, formatted HH24:MI
* "End Time": 
	- data type: string
 	- description: time inspection ended, formatted HH24:MI
* "Sky Condition": 
	- data type: string
 	- description: description of sky, example: "mostly clear"
* "Ambient Temperature": 
	- data type: integer
 	- description: temperature in degrees Fahrenheit
* "Wind Direction": 
	- data type: string
 	- description: which direction the wind is blowing
* "Wind Speed": 
	- data type: integer
 	- description: speed of wind in MPH
* "Humidity": 
	- data type: string
 	- description: humidity in %
* "Barometric Pressure": 
	- data type: string
 	- description: barometric pressure in 'inHg'
* "Viewing Distance": 
	- data type: string
 	- description: viewing distance in feet
* "Inspection Method 1": 
	- data type: string
 	- description: description of first inspection method
* "Inspection Method 2": 
	- data type: string
 	- description: description of second inspection method
* "Survey Instrument 1": 
	- data type: string
 	- description: description of first survery instrument
* "Survey Instrument 2": 
	- data type: string
 	- description: description of second survery instrument
* "Inspector Id 1": 
	- data type: string
 	- description: name of primary inspector
* "Inspector Id 2": 
	- data type: string
 	- description: name of secondary inspector
* "Operational Status": 
	- data type: string
 	- description: status of equipment: Running/Disabled

#### Leak Information
* "leaks":
	- data type: JSON array
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
* "imageUrl": 
	- data type: string
	- description: presigned S3 URL that is valid for one hour to retrieve the image
* "name": 
	- data type: string
	- description: file name of the image
* "sensorType": 
	- data type: string
	- description: type of sensor used to collect image

#### Repair Information
* "repairInformation": 
	- data type: JSON object
	- description: contains the fields pertaining to repairs
* "id": 
	- data type: string
	- description: repair identifier
* "Status": 
	- data type: string
	- description: repair status, ex: "Complete" or "Delay"
* "Component": 
	- data type: string
	- description: part that is leaking
* "Component Subtype": 
	- data type: string
	- description: subtype of part that is leaking
* "Component ID": 
	- data type: string
	- description: component internal identifier
* "Component Location": 
	- data type: string
	- description: component location
* "Description": 
	- data type: string
	- description: description of leak
* "Tag #": 
	- data type: string
	- description: internal identifier of leak asset
* "Video #": 
	- data type: string
	- description: internal identifier of video tied to leak
* "Picture #": 
	- data type: string
	- description: internal identifier of photo tied to leak
* "Leak Rate": 
	- data type: integer
	- description: value of leak
* "Leak Rate UOM":
	- data type: string
	- description: leak rate unit of measure, if null, assume ppm-m
* "Due Date":
   	- data type: string
	- description: due date of repair to be completed
* "Repair Complete":
   	- data type: string
	- description: date repair was completed
* "Verification Date": 
   	- data type: string
	- description: date repair was verified
* "Repair Methods": 
   	- data type: string
	- description: how the repair was done
* "Additional Repair notes": 
   	- data type: string
	- description: additional repair notes entered
* "Repaired By":
    - data type: string
	- description: name of person who completed the repair


### Response Codes:
**200**: Inspections list  
**400**: Bad Request Error - the path is malformed  
**401**: Unauthorized Error    
**403**: Forbidden Error - the request is missing email/token  
**404**: Not Found Error   
**500**: Unknown Error - hopefully this one won't be returned!  
**503**: Upstream Service Error 