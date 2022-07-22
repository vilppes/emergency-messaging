from emtf import EmergencyMessageTypeFormat
#this is a comment
class EmergencyMessage:
    def __init__(self, type) -> None:
        #initializes the emergency message type
        self.type = EmergencyMessageTypeFormat(type)
        self.action_history = []
        self.message = ""
    def get_type(self) -> str:
        #returns the current emergency message type
        self.action_history.append("get_type: "+self.type.get_type())
        return self.type.get_type()
    def change_type(self, type) -> None:
        #changes the emergency message type to the given type
        self.action_history.append("change_type: "+type)
        self.type.change_type(type)
    def change_type_with_number(self, type_number) -> None:
        #changes the emergency message type to the given type
        #0 = death, 1 = material loss, 2 = upcoming losses, 3 = warnings, 4 = general message
        self.action_history.append("change_type_with_number: "+str(type_number))
        self.type.change_type_with_number(type_number)
    def get_type_history(self) -> list:
        #returns a list of all the emergency message types that have been changed
        self.action_history.append("get_type_history: ")
        return self.type.get_history()
    def get_message_with_type(self) -> list:
        #returns a list of all the emergency message types that have been changed
        self.action_history.append("get_message_with_type: ")
        return [self.type.get_type(), self.message]
    def set_message(self, message) -> None:
        #sets the message to the given message
        self.action_history.append("set_message: "+message)
        self.message = message
    def get_message(self) -> str:
        #returns the current emergency message type
        self.action_history.append("get_message: "+self.message)
        return self.message
    def get_action_history(self) -> list:
        #returns a list of all the emergency message types that have been changed
        return self.action_history