import uuid


class Slot:
    def __init__(self, slot_number, vehicle_type, is_available=True):
        self.slot_id = f"SID-{uuid.uuid1().hex[:6]}"
        self.slot_number = slot_number
        self.is_available = is_available
        self.vehicle_type = vehicle_type

    def book_slot(self):
        self.is_available = False
        return self.slot_id

    def free_slot(self):
        self.is_available = True
