class VehicleTypes:
    CAR = 'car'
    BIKE = 'bike'
    TRUCK = 'truck'

    def all(self):
        return [self.CAR, self.BIKE, self.TRUCK]


class AllocationStrategy:
    BOTTOM_TO_TOP = 'bottom_to_top'
