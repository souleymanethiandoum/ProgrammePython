import calculatrice

def main():
    calc = calculatrice.Calculatrice()
    add = calc.addition(2,9)
    print(f'Addition de a + b est égal à {add}')
    div = calc.division(9,0)
    print(f'la division de a et  b est égal à {div}')
if __name__ == "__main__":     
    main()

