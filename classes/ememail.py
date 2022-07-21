from em import EmergencyMessage
#imort outlook
class EmergencyMessageByEmail:
    emergency_message = EmergencyMessage("")
    def __init__(self, email_address) -> None:
        self.email_address = email_address
        self.action_history = []
    def get_email_address(self) -> str:
        self.action_history.append("get_email_address: "+self.email_address)
        return self.email_address
    def set_email_address(self, email_address) -> None:
        self.action_history.append("set_email_address: "+email_address)
        self.email_address = email_address
    def get_action_history(self) -> list:
        return self.action_history
    def send_message(self, message) -> None:
        self.action_history.append("send_message: "+message)
        #send email
        #outlook.send_email(self.email_address, message)
        print("Email sent to "+self.email_address+" with message: "+message)
    def send_emergency_message(self) -> None:
        self.send_message(self.emergency_message.get_message())
    def set_emergency_message(self, message) -> None:
        self.emergency_message.set_message(message)
    def get_emergency_message(self) -> str:
        return self.emergency_message.get_message()
    def get_emergency_message_with_type(self) -> list:
        return self.emergency_message.get_message_with_type()
    def get_emergency_message_type(self) -> str:
        return self.emergency_message.get_type()
    def get_emergency_message_type_history(self) -> list:
        return self.emergency_message.get_type_history()
    def change_emergency_message_type(self, type) -> None:
        self.emergency_message.change_type(type)
    def change_emergency_message_type_with_number(self, type_number) -> None:
        self.emergency_message.change_type_with_number(type_number)