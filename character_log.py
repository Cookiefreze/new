import logging
import requests
#This make the logger a logging but on the file __name__
logger = logging.getLogger(__name__)
#This is where you will configurate the Handler
file_handler = logging.FileHandler("character.log")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")
file_handler.setFormatter(formatter)
#this the strean handler that let you print on the terminal
stream_handler = logging.StreamHandler()
file_handler.setLevel(logging.ERROR)

#File handler to add the handler
logger.addHandler(file_handler)
#A streamHandler will input the message in the terminal so you can see it,
#tho you can use logging. to input in the chat, since you didnt put any file,
logger.addHandler(stream_handler)
#
class character_config:
    def __init__(self,name,age: int,hobby):
        self.age = age
        self.hobby = hobby
        self.name = name
        
        if age == 0:
            logger.info("age can't be zero")

        logger.info(f"{name} is {age} years old, and she likes {hobby}")
    def web(self, number):
        web = requests.get(f"https://yuri.com/{self.name}/{number}")
        if web.ok:
            return web.text
        else:
            return "bad response"
        
        


# Yachiyo = character_config("Yachiyo",0,"sing")
# Iroha = character_config("Iroha",17,"play game and Yachio")
# Kaguya = character_config("Kaguya",8000,"Iroha")