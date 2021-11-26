from services.parking_management_service import ParkingManagementService

if __name__ == "__main__":

    parking_management_service = ParkingManagementService()

    parking_lot_1 = parking_management_service.create_parking(parking_lot_id=1, no_of_floors=5, no_of_slots_per_floor=9)
    park_vehicle_1 = parking_management_service.park_vehicle(parking_lot_id = 1, vehicle_type="CAR", reg_no="KIA-7", color="BLACK")
    park_vehicle_2 = parking_management_service.park_vehicle(parking_lot_id = 1, vehicle_type="BIKE", reg_no="ACTIVA", color="ORANGE")

    unpark_vehicle_1 = parking_management_service.un_park_vehicle(park_vehicle_1.ticket_id)
    free_count = parking_management_service.display(display_type="free_count", parking_lot_id = 1, vehicle_type="BIKE")
