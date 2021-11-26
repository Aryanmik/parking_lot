class ParkingLotDB:
    parking_lots = {}

    def save(self, parking_lot):
        self.parking_lots[parking_lot.id] = parking_lot
        return parking_lot

    def get(self, parking_lot_id):
        if self.parking_lots.get(parking_lot_id):
            return self.parking_lots.get(parking_lot_id)
        else:
            raise Exception(f"No parking lot found id: {parking_lot_id}")