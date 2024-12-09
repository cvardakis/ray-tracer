
class DirectionalLight:
    def __init__(self, direction, color):
        self.direction = direction.unit_vector()
        self.color = color

    def direction(self):
        return self.direction

