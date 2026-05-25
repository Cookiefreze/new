import logging
logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("character.log")
logger.setLevel(logging.INFO)
formatter = logging.Formatter()
file_handler.setFormatter(formatter)



logger.addHandler(file_handler)

class charater_config:
    def __init__(self,name,age: int,hobby):
        self.age = age
        self.hobby = hobby
        print(age,hobby)
        logger.debug(f"{name} is {age} years old, and she likes {hobby}")
        


Yachiyo = charater_config("Yachiyo",8000,"sing")
Iroha = charater_config("Iroha",17,"play game and Yachio")
Kaguya = charater_config("Kaguya",8000,"Iroha")