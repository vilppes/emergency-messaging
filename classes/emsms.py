from em import EmergencyMessage
class EmergencyMessageByTextMessage:
    emergency_message = EmergencyMessage("death")
    def __init__(self, phone_number) -> None:
        self.phone_number = phone_number
        self.action_history = []
    def get_phone_number(self) -> str:
        self.action_history.append("get_phone_number: "+self.phone_number)
        return self.phone_number
    def set_phone_number(self, phone_number) -> None:
        self.action_history.append("set_phone_number: "+phone_number)
        self.phone_number = phone_number
    def get_action_history(self) -> list:
        return self.action_history
    def send_message(self, message) -> None:
        raise Warning("This method is not implemented yet.")
