class Tempo:
    def __init__(self):
        self.__hour = 5
        self.__minute = 0 

    def __str__(self):
        return f'São {self.__hour} : {self.__minute}'

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, hour):
        self.__hour = hour

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, minute):
        self.__minute = minute


    def passarTempo(self, minutes, hour=5):
        self.minute += minutes
        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1

print(Tempo())