from emtf import EmergencyMessageTypeFormat
class EmergencyMessage:
    def __init__(self, type) -> None:
        self.type = EmergencyMessageTypeFormat(type)
        self.action_history = []
        self.message = ""
    def get_type(self) -> str:
        self.action_history.append("get_type: "+self.type.get_type())
        return self.type.get_type()
    def change_type(self, type) -> None:
        self.action_history.append("change_type: "+type)
        self.type.change_type(type)
    def change_type_with_number(self, type_number) -> None:
        self.action_history.append("change_type_with_number: "+str(type_number))
        self.type.change_type_with_number(type_number)
    def get_type_history(self) -> list:
        self.action_history.append("get_type_history: ")
        return self.type.get_history()
    def get_message_with_type(self) -> list:
        self.action_history.append("get_message_with_type: ")
        return [self.type.get_type(), self.message]
    def set_message(self, message) -> None:
        self.action_history.append("set_message: "+message)
        self.message = message
    def get_message(self) -> str:
        self.action_history.append("get_message: "+self.message)
        return self.message
    def get_action_history(self) -> list:
        return self.action_history