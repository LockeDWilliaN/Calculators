from math import sqrt

class Pitagoras:
    def __init__(self, h, c1, c2):
        self.h, self.c1, self.c2 = h, c1, c2
        
    def calcular_pitagoras(self):
        if self.c1 == 0 or self.c2 == 0 or self.h == 0:
            self.c1 = None if self.c1 == 0 else self.c1
            self.c2 = None if self.c2 == 0 else self.c2
            self.h = None if self.h == 0 else self.h

        if self.h is None:    
            self.h = sqrt(self.c1**2 + self.c2**2)
            return self.c1, self.c2, self.h
                
        elif self.c1 is None:
            self.c1 = sqrt(self.h**2 - self.c2**2)
            return self.c1, self.c2, self.h

        elif self.c2 is None:
            self.c2 = sqrt(self.h**2 - self.c1**2)
            return self.c1, self.c2, self.h 
        
    def results(self):
        resultado = self.calcular_pitagoras()
        if resultado is not None:
            print("\n--------------------------------")
            print(f"O valor do cateto oposto é: {self.c1}")        
            print(f"O valor do cateto adjacente é: {self.c2}")        
            print(f"O valor da Hipotenusa é: {self.h}")       
            print("--------------------------------")
