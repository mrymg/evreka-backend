# Evreka Backend Case Study
This web application uses Django and SQLite 3



## Question 1

I will suggest multiple methods to reduce the cost of accessing the model.

 1. We can add the last location and the last time of the vehicle to the **vehicle model class.** In this way, we can access the last locations and the date of the vehicles without any filtering.
 
 *But for a stronger structure:* 
 
 2. As far as I understand, the data consists of real-time data. The use of a strong **queue** structure (such as **Kafka**) together with a **NOSQL** type (such as **MongoDB**) database for storing real-time data will increase the performance and ensure the effectiveness of this structure.
   

## API
In this application, there are some endpoints to get and create data

    GET
    '/api/VehicleList'
    '/api/NavigationRecordList'
    '/api/vehicle/id'
    '/api/NavigationRecord/id'
    
for getting lists or single views. 

Example of POST request for Navigation Record: 

     
    '/api/create/record'
    ----------------------
    JSON
	    {
			"lat": Latitude,
			"lng": Longtitude,
			"datetime": "date",
			"vehicle": vehicleID
		}

Example of POST request for Vehicle: 

   

     '/api/create/vehicle'
    ----------------------
	    {
			"plate": "PLATE"
		}

    
    

## Question 2 


![s](#)

