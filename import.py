import json

# Load campus data from JSON
with open("campus_data.json", "r") as file:
    campus_data = json.load(file)

def get_location_info(place):
    return campus_data["locations"].get(place, "Location not found.")

def get_event_info(event_name):
    event = campus_data["events"].get(event_name, None)
    if event:
        return f"{event['name']} is on {event['date']} at {event['location']}."
    return "Event not found."
