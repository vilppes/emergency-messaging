from em import EmergencyMessage
#TODO: import a discord functionalities library
class EmergencyMessageByDiscord:
    def __init__(self,message: str) -> None:
        self.emergency_message = EmergencyMessage("death")
        self.message = message
    def send_the_message(self,channel_of_choice):
        raise Warning("not implemented yet")
    def set_the_emergency_message(self,message):
        self.emergency_message.set_message(message)
    def change_emergency_message_type(self,type):
        self.emergency_message.change_type(type)