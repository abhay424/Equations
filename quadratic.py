import cmath

# a*x^2 + b*x + c = 0
class Quadratic:
    def __init__(self, a=0.0,b=0.0,c=0.0):
        self.a=a
        self.b=b
        self.c=c
        self.calc = True # to avoid multiple time calculation

    def __str__(self):
        return "{0}*x^2 + {1}*x + {2} = 0".format( self.a, self.b, self.c)

    def getRoots(self):
        if self.calc:
            x_1 = ( -1*self.b + cmath.sqrt( self.b**2 - 4*self.a*self.c) )/(2*self.a)
            x_2 = ( -1*self.b - cmath.sqrt( self.b**2 - 4*self.a*self.c) )/(2*self.a)

            self.x_1 = x_1.real if x_1.imag == 0 else x_1
            self.x_2 = x_2.real if x_2.imag == 0 else x_2
            self.calc = False
        return self.x_1, self.x_2
