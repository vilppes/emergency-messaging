from em import EmergencyMessage
#TODO: import a twitter functionalities library
class EmergencyMessageByTwitter:
    def __init__(self,message: str) -> None:
        self.emergency_message = EmergencyMessage("death")
        self.message = message
    def tweet_the_message(self):
        raise Warning("not implemented yet")
    def set_the_emergency_message(self,message):
        self.emergency_message.set_message(message)