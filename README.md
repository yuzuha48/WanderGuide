# WanderGuide ✈️

Since I love traveling, I decided to create a travel itinerary sharing social media platform where people can create and view itineraries for various places! 

Users can:
- 🔍 search for itineraries based on location
- ➕ add as many days to their itineraries as they wish
- 📍 pin locations on Google Maps in their itineraries
- ♥️ save other users' itineraries
- 👀 view how many people saved the itineraries
- ✏️ edit & delete itineraries they created

https://github.com/yuzuha48/WanderGuide/assets/106595505/2c4aad93-9fd3-4449-ab19-e6bfaf7283ed

## Prerequisites

Ensure you have the following software installed on your machine:
- Python (version 3.6 or higher)
- pip (Python package installer)
- pipenv (Python package manager)

## Getting Started 

To get started with WanderGuide, follow these steps: 
1. Clone this repository to your local machine:
   - git clone https://github.com/yuzuha48/WanderGuide
2. Navigate to the project directory:
   ```
   cd WanderGuide
   ```
4. Install the required dependencies using pipenv:
   ```
   pipenv install
   ```
6. Activate the virtual environment:
   ```
   pipenv shell
   ```
8. Modify the database connection configurations in:
   `flask_app/config/mysqlconnection.py`
9. Start WanderGuide by running the following command:
     ```
     python3 server.py
     ```
10. Open a web browser and visit `http://localhost:5001` to view the running app. 



