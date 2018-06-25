import cmath
import quadratic

def cubeRoot( x = 0.0 ):
    return x**(1/3) if x > 0.0 else -1*((-1*x)**(1/3))

class Cubic:
    def __init__(self, a=0.0,b=0.0,c=0.0,d=0.0):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.calc = True

    def __str__(self):
        return "{0}*x^3 + {1}*x^2 + {2}*x + {3} = 0".format( self.a, self.b, self.c,self.d)

    def getRoots(self):
        return self.__cardonEq()

    # Applying CARDON`s method, modify to get Z = z^3 + p*z + q = 0, by substitutin x = z - (self.b/(3*self.a))
    def __cardonEq(self):
        if self.calc :
            a2 = self.b/self.a; a1 = self.c/self.a; a0=self.d/self.a;
            self.p = (3*a1 - a2**2)/3
            self.q = -1*(9*a1*a2 - 27*a0 - 2*a2**3)/27
            self.__solve()
            self.calc = False

        return self.x1, self.x2, self.x3

    def __solve(self):
        uv = -1*self.p/3; sum_cube_u_and_v = self.q
        a=1.0;  b = sum_cube_u_and_v; c = uv**3
        quadEq = quadratic.Quadratic( a, b, c )
        u_3, v_3 = quadEq.getRoots()
        u_= u_3**(1.0/3.0)
        if u_3.imag == 0:
            u_ = cubeRoot( u_3.real )

        v_= v_3**(1.0/3.0)
        if v_3.imag == 0:
            v_ = cubeRoot(v_3.real)

        z1 = u_+v_ # one of the root of equation Z
        # depricated quad equation
        a=1.0; b = z1; c = self.p + (z1**2)
        quadEq1 = quadratic.Quadratic( a, b, c )
        z2, z3 = quadEq1.getRoots()

        self.x1 = z1 - (self.b/(3*self.a))
        if self.x1.imag == 0:
            self.x1 = self.x1.real
        self.x2 = z2 - (self.b/(3*self.a))
        if self.x2.imag == 0:
            self.x2 = self.x2.real
        self.x3 = z3 - (self.b/(3*self.a))
        if self.x3.imag == 0:
            self.x3 = self.x3.real
