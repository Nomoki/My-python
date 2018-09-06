"""PlanC-Z"""
def main():
    """input 4 val"""
    text = input()
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num1, num2 = high(num1, num2), low(num1, num2)
    num1, num3 = high(num1, num3), low(num1, num3)
    num2, num3 = high(num2, num3), low(num2, num3)
    if text == "Ascend":
        print("%.2f, %.2f, %.2f"%(num3, num2, num1))
    elif text == "Descend":
        print("%.2f, %.2f, %.2f"%(num1, num2, num3))

def high(num1, num2):
    """Calcu high"""
    if num1 > num2:
        return num1
    else:
        return num2

def low(num1, num2):
    """Calcu low"""
    if num1 < num2:
        return num1
    else:
        return num2
main()
