from utils.constant import AllocationStrategy


class ParkingLot:

    def __init__(self, id, floor_wise_slots, allocation_strategy = AllocationStrategy.BOTTOM_TO_TOP):
        self.id = id
        self.floor_wise_slots = floor_wise_slots
        self.allocation_strategy = allocation_strategy
