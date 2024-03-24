import json
from datetime import datetime

def record_rating(user_input, ai_response, rating):
    # Define the path to the JSON file where ratings will be stored
    ratings_file_path = "ratings_data.json"
    
    # Create a dictionary to represent the rating record
    record = {
        "user_input": user_input,
        "ai_response": ai_response,
        "rating": rating,
        "timestamp": datetime.now().isoformat()
    }
    
    # Try to read the existing data
    try:
        with open(ratings_file_path, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []

    # Append the new record
    data.append(record)

    # Write the updated data back to the file
    with open(ratings_file_path, 'w') as file:
        json.dump(data, file, indent=4)