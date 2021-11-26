import uuid


class Ticket:

    def __init__(self, parking_lot_id, vehicle_type, reg_no, color, slot_id):
        self.ticket_id = f"TKT-{uuid.uuid1().hex[:6]}"
        self.parking_lot_id = parking_lot_id
        self.vehicle_type = vehicle_type
        self.reg_no = reg_no
        self.color = color
        self.slot_id = slot_id
