class Tempo:
    def __init__(self):
        self.hour = 5
        self.minute = 0 

    def __str__(self):
        return f'São {self.hour}:{self.minute}\n'

    def pass_time(self, minutes):
        self.minute += minutes
        while self.minute >= 60:
            self.minute -= 60
            self.hour += 1
            
tempo = Tempo()