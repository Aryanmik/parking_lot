class BottomToTopAllocationStrategy:

    def allocate_slots(self, floor, vehicle_type):
        slots = floor.available_slots_by_vehicle_type.get(vehicle_type.lower())
        if not slots:
            raise Exception("No slots available")
        booked_slot_id = slots[0].book_slot()
        return booked_slot_id
