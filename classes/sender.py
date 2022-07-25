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
        self.message = message
    def send_email(self,email_address,type):
        self.message_by_email.change_emergency_message_type(type)
        self.message_by_email.set_emergency_message(self.message)
        self.message_by_email.set_email_address(email_address)
        self.message_by_email.send_emergency_message()
    def send_text(self,number,type):
        self.message_by_text.change_emergency_message_type(type)
        self.message_by_text.set_phone_number(number)
        self.message_by_text.send_message(self.message)
    def send_tweet(self,type):
        self.message_by_tweet.change_emergency_message_type(type)
        self.message_by_tweet.tweet_the_message(self.message)
    def send_discord_message(self,channel,type):
        self.message_by_discord.change_emergency_message_type(type)
        self.message_by_discord.send_the_message(channel)