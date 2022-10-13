import random

class Lottery:

    def __init__(self, red, green, blue):
        number_red = random.randint(1, red)
        number_green = random.randint(1, green)
        number_blue = random.randint(1, blue)

