class Cell:
    def __init__(self, is_service, values, location):
        self.is_service = is_service
        self._values = values
        self._location = location

    def get_location(self):
        return self._location

    def get_values(self):
        return self._values

    def append_value(self, value):
        self._values.append(value)

    def set_value(self, value):
        self._values = value

    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.is_service == other.is_service and \
                   self._values == other._values and \
                   self._location == other._location
