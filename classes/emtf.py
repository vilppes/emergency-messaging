class EmergencyMessageTypeFormat:
    types = ['death', 'material loss', 'upcoming losses', 'warnings', 'general message']
    change_history = []
    def __init__(self, type) -> None:
        if type not in self.types:
            raise ValueError('Invalid emergency message type')
        self.type = type
        self.change_history.append(type)
    def get_type(self) -> str:
        return self.type
    def change_type(self, type) -> None:
        if type not in self.types:
            raise ValueError('Invalid emergency message type')
        self.type = type
        self.change_history.append(type)
    def change_type_with_number(self, type_number) -> None:
        #0 = death, 1 = material loss, 2 = upcoming losses, 3 = warnings, 4 = general message
        if type_number not in range(len(self.types)):
            raise ValueError('Invalid emergency message type')
        self.type = self.types[type_number]
        self.change_history.append(self.types[type_number])
    def get_history(self) -> list:
        return self.change_history