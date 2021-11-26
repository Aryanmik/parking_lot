from database.parking_lot import ParkingLotDB
from database.tickets import TicketsDB
from database.vehicle import VehicleDB
from models.floors import Floor
from models.parking_lot import ParkingLot
from models.parking_lot_slots import Slot
from models.tickets import Ticket
from services.bottom_to_top_allocation_strategy import BottomToTopAllocationStrategy
from utils.constant import VehicleTypes, AllocationStrategy


class ParkingManagementService:

    def __init__(self):
        self.parking_lot = ParkingLotDB()
        self.tickets = TicketsDB()
        self.vehicle = VehicleDB()

    @staticmethod
    def _create_slots(no_of_floors, no_of_slots_per_floor):
        floor_wise_slots = []
        for floor_no in range(no_of_floors):
            slots = []
            available_no_of_slots_per_floor = no_of_slots_per_floor
            slot_id = 1
            if available_no_of_slots_per_floor >= 1:
                slots.append(Slot(slot_id, vehicle_type=VehicleTypes.TRUCK))
                available_no_of_slots_per_floor -= 1

            if available_no_of_slots_per_floor >= 2:
                for i in range(2):
                    slot_id = slot_id + 1
                    slots.append(Slot(slot_id, vehicle_type=VehicleTypes.BIKE))
                    available_no_of_slots_per_floor -= 1

            if available_no_of_slots_per_floor:
                for i in range(available_no_of_slots_per_floor+1):
                    slot_id = slot_id + 1
                    slots.append(Slot(slot_id, vehicle_type=VehicleTypes.CAR))
            floor = Floor(floor_no=floor_no, slots=slots)
            floor_wise_slots.append(floor)

        return floor_wise_slots

    def create_parking(self, parking_lot_id, no_of_floors, no_of_slots_per_floor):
        parking_lot = ParkingLot(id=parking_lot_id, floor_wise_slots=[])

        floor_wise_slots = self._create_slots(no_of_floors, no_of_slots_per_floor)

        parking_lot.floor_wise_slots = floor_wise_slots

        self.parking_lot.save(parking_lot=parking_lot)
        return parking_lot

    def park_vehicle(self, parking_lot_id, vehicle_type, reg_no, color):
        parking_lot = self.parking_lot.get(parking_lot_id)
        booked_slot_id = None
        for floor in parking_lot.floor_wise_slots:
            if parking_lot.allocation_strategy == AllocationStrategy.BOTTOM_TO_TOP:
                booked_slot_id = BottomToTopAllocationStrategy().allocate_slots(floor, vehicle_type)
            break

        ticket = Ticket(parking_lot_id=parking_lot.id, vehicle_type=vehicle_type, reg_no=reg_no, color=color,
                        slot_id=booked_slot_id)

        self.tickets.save(ticket)
        return ticket

    def un_park_vehicle(self, ticket_id):
        ticket = self.tickets.get(ticket_id)
        parking_lot = self.parking_lot.get(ticket.parking_lot_id)
        for floor in parking_lot.floor_wise_slots:
            for slot in floor.slots:
                if slot.slot_id == ticket.slot_id:
                    slot.free_slot()


    def display(self, display_type, parking_lot_id, vehicle_type):
        parking_lot = self.parking_lot.get(parking_lot_id)
        if display_type == "free_count":
            count = 0
            for floor in parking_lot.floor_wise_slots:
                count += len(floor.available_slots_by_vehicle_type[vehicle_type.lower()])
            return count


