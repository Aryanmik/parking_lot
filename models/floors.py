from typing import List

from collections import defaultdict

from models.parking_lot_slots import Slot


class Floor:

    def __init__(self, floor_no, slots=List[Slot]):
        self.floor_no = floor_no
        self.slots = slots

    @property
    def available_slots_by_vehicle_type(self):
        available_slots_by_vehicle_type = defaultdict(list)
        for slot in self.slots:
            if slot.is_available:
                available_slots_by_vehicle_type[slot.vehicle_type].append(slot)
        return available_slots_by_vehicle_type


    @property
    def occupied_slots_by_vehicle_type(self):
        available_slots_by_vehicle_type = defaultdict(list)
        for slot in self.slots:
            if not slot.is_available:
                available_slots_by_vehicle_type[slot.vehicle_type].append(slot)
        return available_slots_by_vehicle_type