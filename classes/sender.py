#imports
from ememail import EmergencyMessageByEmail
from emsms import EmergencyMessageByTextMessage
from emtw import EmergencyMessageByTwitter
from emdc import EmergencyMessageByDiscord
class EmergencyMessageSender:
    def __init__(self,message) -> None:
        self.message_by_email = EmergencyMessageByEmail("name@domain.tld")
        self.message_by_text = EmergencyMessageByTextMessage("911")
        self.message_by_tweet = EmergencyMessageByTwitter(message)
        self.message_by_discord = EmergencyMessageByDiscord(message)