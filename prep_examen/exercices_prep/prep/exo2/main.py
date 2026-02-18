from calculator.engine import CalculatorEngine

def main():
    e = CalculatorEngine()
    print(e.add(2, 3))
    print(e.sub(10, 4))
    print(e.mul(6, 7))

if __name__ == "__main__":
    main()
