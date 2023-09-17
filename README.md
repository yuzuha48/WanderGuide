# WanderGuide ✈️

Since I love traveling, I decided to create a travel itinerary sharing social media platform where people can create and view itineraries for various places! 

Users can:
- 🔍 search for itineraries based on location
- ➕ add as many days to their itineraries as they wish
- 📍 pin locations on Google Maps in their itineraries
- ♥️ save other users' itineraries
- 👀 view how many people saved the itineraries
- ✏️ edit & delete itineraries they created

<img width="1438" alt="explore_page" src="https://github.com/yuzuha48/WanderGuide/assets/106595505/5ca52935-0f49-4281-bf0b-dcfe8c3576fe">
<img width="1439" alt="itinerary" src="https://github.com/yuzuha48/WanderGuide/assets/106595505/107fe613-484e-47e7-9353-72ffb2c1c2cb">
<img width="1429" alt="travel_w_itinerary" src="https://github.com/yuzuha48/WanderGuide/assets/106595505/c7671df2-8421-40e1-aae2-27bccd794017">
<img width="1439" alt="my_itineraries" src="https://github.com/yuzuha48/WanderGuide/assets/106595505/aa131645-01c4-4fbe-9ce8-d3fd472b6055">
<img width="1439" alt="saved_itineraries" src="https://github.com/yuzuha48/WanderGuide/assets/106595505/81552594-0763-46d0-8a81-eb61295a91ad">

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



