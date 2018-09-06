"""Circular II"""
def main():
    """Find area attacker me and friend"""
    mex = float(input())
    mey = float(input())
    mosrange1 = float(input())
    mosx = float(input())
    mosy = float(input())
    mosrange2 = float(input())
    linex = mosx - mex
    liney = mosy - mey
    pita = linex**2 + liney**2
    pitaans = (pita)**(1/2)
    if pitaans < mosrange1 + mosrange2:
        print("Yes")
    else:
        print("No")
main()
