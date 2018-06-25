
import cubic

if __name__ == "__main__":
    #print("Input values for a, b and c in quadratic equation a*x^2 + b*x + c = 0.")
    #a = float(input('a = '))
    #b = float(input('b = '))
    #c = float(input('c = '))

    #quadEq = quadEquation( a, b, c )
    #print( quadEq )

    #x1, x2 = quadEq.getRoots();
    #print(x1)
    #print(x2)

    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))
    d = float(input('d = '))

    cubeEq = cubic.Cubic( a, b, c, d )
    print( cubeEq )

    x1, x2, x3 = cubeEq.getRoots();
    print(x1)
    print(x2)
    print(x3)
