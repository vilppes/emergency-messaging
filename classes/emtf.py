class EmergencyMessageTypeFormat:
    types = ['death', 'material loss', 'upcoming losses', 'warnings', 'general message'] #list of all the emergency message types
    #contains the types in the order they were changed
    change_history = []
    def __init__(self, type) -> None:
        #initializes the emergency message type
        if type not in self.types:
            raise ValueError('Invalid emergency message type')
        self.type = type
        self.change_history.append(type)
    def get_type(self) -> str:
        #returns the current emergency message type
        return self.type
    def change_type(self, type) -> None:
        #changes the emergency message type to the given type
        if type not in self.types:
            raise ValueError('Invalid emergency message type')
        self.type = type
        self.change_history.append(type)
    def change_type_with_number(self, type_number) -> None:
        #changes the emergency message type to the given type
        #0 = death, 1 = material loss, 2 = upcoming losses, 3 = warnings, 4 = general message
        if type_number not in range(len(self.types)):
            raise ValueError('Invalid emergency message type')
        self.type = self.types[type_number]
        self.change_history.append(self.types[type_number])
    def get_history(self) -> list:
        #returns a list of all the emergency message types that have been changed
        return self.change_history