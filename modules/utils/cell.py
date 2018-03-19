class Cell:
    def __init__(self, is_service, values, location):
        self._is_service = is_service
        self._location = location
        if isinstance(values, list):
            self._values = values
        elif isinstance(values, int):
            self._values = [values]
        else:
            raise ValueError('values is not int or list')

    @property
    def location(self):
        return self._location

    @property
    def values(self):
        return self._values

    def append_value(self, value):
        self._values.append(value)

    @values.setter
    def values(self, value):
        if isinstance(value, int):
            value = [value]
        self._values = value

    @property
    def is_service(self):
        return self._is_service

    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.is_service == other.is_service and \
                   self.values == other.values and \
                   self.location == other.location

    def __str__(self):
        return 'service ' if self.is_service else '' + 'cell {} <{}>'.format(self.location, self.values)
