"""DataSpike"""
def main():
    """8 input"""
    numa = int(input())
    numb = int(input())
    numc = int(input())
    numd = int(input())
    nume = int(input())
    numf = int(input())
    numg = int(input())
    numh = int(input())
    highest = main2(numa, numb)
    highest = main2(highest, numc)
    highest = main2(highest, numd)
    highest = main2(highest, nume)
    highest = main2(highest, numf)
    highest = main2(highest, numg)
    highest = main2(highest, numh)
    print(highest)

def main2(num1, num2):
    """Compare 8 input"""
    if num1 > num2:
        return num1
    else:
        return num2
main()
