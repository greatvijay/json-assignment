import json

# Dictionary of Indian states and capitals
indian_states_capitals = {
    "Andhra Pradesh": "Hyderabad",
    "Maharashtra": "Mumbai",
    "Karnataka": "Bengaluru",
    "Tamil Nadu": "Chennai",
    "Rajasthan": "Jaipur",
    "Uttar Pradesh": "Lucknow",
    "Gujarat": "Gandhinagar"
}

# Writing the dictionary to a JSON file
with open("indian_states_capitals.json", "w") as json_file:
    json.dump(indian_states_capitals, json_file)

print("Data has been written to 'indian_states_capitals.json' successfully.")
