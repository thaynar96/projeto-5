class Tempo:
    def __init__(self):
        self.hora = 5
        self.minuto = 0

    def passarTempo(self,minutos,hora=5):
        self.minuto += minutos
        while self.minuto>=60:
            self.minuto -= 60
            self.hora += 1

