from gravity import GravityField

class GravityController:
    def __init__(self):
        self._gravity_field = GravityField()
    
    def adjust(self, curvature_radius: float):
        return self._gravity_field.set_curvature_radius(value=curvature_radius)
