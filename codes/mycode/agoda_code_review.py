import threading
import requests

class HotelService:

    def __init__(self):
        self.cache = {}
        self.lock = threading.Lock()

    def update_inventory(self, hotel_id):
        response = requests.get("https://supplier.api/hotel/" + hotel_id)
        data = response.json()

        self.lock.acquire()
        try:
            self.cache[hotel_id] = data["rooms"]
        finally:
            self.lock.release()

    def get_rooms(self, hotel_id):
        if hotel_id in self.cache:
            return self.cache[hotel_id]

        self.update_inventory(hotel_id)
        return self.cache.get(hotel_id)


class BookingService:

    def __init__(self):
        self.hotel_service = HotelService()

    def book_room(self, hotel_id):

        rooms = self.hotel_service.get_rooms(hotel_id)

        if rooms > 0:
            rooms -= 1
            print("Booking confirmed")
        else:
            print("No rooms available")