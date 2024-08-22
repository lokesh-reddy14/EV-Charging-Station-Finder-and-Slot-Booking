import datetime

charging_stations = [
    {
        "id": 1,
        "name": "Green Charge Hub",
         "location": ["Downtown","Vizag","Vijaywada"],
        "types": ["Fast", "Slow"],
        "slots": {
            "09:00 AM - 10:00 AM": True,
            "10:00 AM - 11:00 AM": False,
            "11:00 AM - 12:00 PM": True,
            "12:00 PM - 01:00 PM": True,
        },
        "amenities": ["Restrooms", "Cafe"],
    },
    {
        "id": 2,
        "name": "EcoCharge Station",
        "location": "Suburbs",
        "types": ["Fast"],
        "slots": {
            "09:00 AM - 10:00 AM": True,
            "10:00 AM - 11:00 AM": True,
            "11:00 AM - 12:00 PM": True,
            "12:00 PM - 01:00 PM": False,
        },
        "amenities": ["Restrooms"],
    },
    {
        "id": 3,
        "name": "PowerUp Station",
        "location": "City Center",
        "types": ["Slow"],
        "slots": {
            "09:00 AM - 10:00 AM": False,
            "10:00 AM - 11:00 AM": True,
            "11:00 AM - 12:00 PM": True,
            "12:00 PM - 01:00 PM": True,
        },
        "amenities": ["Cafe"],
    }
]

def search_stations(location=None, charging_type=None, amenities=None):
    results = []
    for station in charging_stations:
        if (location is None or location in station["location"]) and \
           (charging_type is None or charging_type in station["types"]) and \
           (amenities is None or all(amenity in station["amenities"] for amenity in amenities)):
            results.append(station)
    return results

def display_stations(stations):
    if not stations:
        print("No charging stations found with the given criteria.")
        return
    for station in stations:
        print(f"\nStation ID: {station['id']}")
        print(f"Name: {station['name']}")
        print(f"Location: {station['location']}")
        print(f"Charging Types: {', '.join(station['types'])}")
        print(f"Amenities: {', '.join(station['amenities'])}")
        print("Available Slots:")
        for slot, available in station['slots'].items():
            status = "Available" if available else "Booked"
            print(f"  - {slot}: {status}")

def book_slot(station_id, slot):
    for station in charging_stations:
        if station["id"] == station_id:
            if slot in station["slots"] and station["slots"][slot]:
                station["slots"][slot] = False
                print(f"\nSlot '{slot}' at '{station['name']}' has been successfully booked.")
                return
            else:
                print("Selected slot is not available.")
                return
    print("Invalid station ID or slot.")

def main():
    print("Welcome to the EV Charging Station Finder and Slot Booking System\n")

    location = input("Enter the location to search for charging stations: ")
    charging_type = input("Enter the desired charging type (Fast/Slow) or press Enter to skip: ")
    amenities_input = input("Enter required amenities (comma-separated) or press Enter to skip: ")
    amenities = [amenity.strip() for amenity in amenities_input.split(',')] if amenities_input else None

    matching_stations = search_stations(location, charging_type, amenities)
    display_stations(matching_stations)

    if matching_stations:
        station_id = int(input("\nEnter the Station ID to book a slot: "))
        slot = input("Enter the time slot (e.g., 10:00 AM - 11:00 AM): ")
        book_slot(station_id, slot)

    print("\nThank you for using the EV Charging Station Finder and Slot Booking System!")

if __name__ == "__main__":
    main()
