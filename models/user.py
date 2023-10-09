class User:
    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
    
    @name.setter
    def name(self, value):
        self.first_name = value
