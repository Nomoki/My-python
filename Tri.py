"""Triangle I"""
def main():
    """calcu 3wood"""
    numa = float(input())
    numb = float(input())
    numc = float(input())
    numa, numb = high(numa, numb), low(numa, numb)
    numa, numc = high(numa, numc), low(numa, numc)
    numb, numc = high(numb, numc), low(numb, numc)
    numcb = (numc**2)+(numb**2)
    if (numcb - (numa**2)) <= 0.01:
        print("Yes")
    else:
        print("No")

def high(numa, numb):
    """High"""
    if numa > numb:
        return numa
    else:
        return numb

def low(numa, numb):
    """Low"""
    if numa < numb:
        return numa
    else:
        return numb
main()
