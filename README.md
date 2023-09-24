# WanderGuide ✈️

Driven by my love of travel, I decided to create a social media platform dedicated to sharing travel itineraries. Here, individuals can both craft and explore captivating itineraries for diverse destinations.

Users can:
- 🔍 search for itineraries based on location
- ➕ create an itinerary and add as many days to their itineraries as they wish
- 📍 pin locations on Google Maps in their itineraries
- ♥️ save other users' itineraries
- 👀 view how many people saved the itineraries
- ✏️ edit & delete itineraries they created

In this project I:
- Utilized Python & MySQL for back-end features including CRUD of itineraries, users, and users’ saved itineraries
- Employed Flask and JavaScript to enhance user experience by including validation error messages and allowing users to add days onto an itinerary as well as save other users’ itineraries
- Implemented a call to the Google Maps API to allow users to pin locations in their itineraries
- Created a responsive front-end design using HTML, CSS, and Bootstrap
  
<img width="1440" alt="login" src="https://github.com/yuzuha48/WanderGuide/assets/106595505/8523ac36-61db-4e0c-a7bc-9e379d3c31f4">
<img width="1440" alt="register" src="https://github.com/yuzuha48/WanderGuide/assets/106595505/2fdbadca-883e-4467-bd08-0bbcff855968">
<img width="1438" alt="explore_page" src="https://github.com/yuzuha48/WanderGuide/assets/106595505/5ca52935-0f49-4281-bf0b-dcfe8c3576fe">
<img width="1439" alt="saved_itineraries" src="https://github.com/yuzuha48/WanderGuide/assets/106595505/81552594-0763-46d0-8a81-eb61295a91ad">
<img width="1439" alt="my_itineraries" src="https://github.com/yuzuha48/WanderGuide/assets/106595505/aa131645-01c4-4fbe-9ce8-d3fd472b6055">
<img width="1439" alt="itinerary" src="https://github.com/yuzuha48/WanderGuide/assets/106595505/107fe613-484e-47e7-9353-72ffb2c1c2cb">
<img width="1439" alt="itinerary_w_map" src="https://github.com/yuzuha48/WanderGuide/assets/106595505/7569cb85-7ead-4e65-b38f-ad466180949c">
<img width="1439" alt="create_itinerary" src="https://github.com/yuzuha48/WanderGuide/assets/106595505/2f1b38be-6323-4753-8435-b9e535c33385">
<img width="1439" alt="create_itinerary_2" src="https://github.com/yuzuha48/WanderGuide/assets/106595505/7b63fe13-4a20-4d8e-8847-3550c609ebb7">

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
3. Install the required dependencies using pipenv:
   ```
   pipenv install
   ```
4. Activate the virtual environment:
   ```
   pipenv shell
   ```
5. Modify the database connection configurations in:
   `flask_app/config/mysqlconnection.py`
6. Start WanderGuide by running the following command:
     ```
     python3 server.py
     ```
7. Open a web browser and visit `http://localhost:5001` to view the running app. 



