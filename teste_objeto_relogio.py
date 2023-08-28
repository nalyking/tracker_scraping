class Relogio():
    def segundo(self,):
        for seg in range(0,60):
            self.seg += 1
        return self.seg

    def minuto(self,):
        if self.segundo() == 60:
            self.minutos += 1
        return self.minutos
    def horas(self,):
        if self.minuto() == 60:
            self.horas += 1
        return self.horas

relogio = Relogio()
print(relogio.segundo())