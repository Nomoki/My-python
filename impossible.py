""" mission impossible """
def main():
    """ function input value """
    numa = int(input())
    numb = int(input())
    numc = int(input())
    numd = int(input())
    nume = int(input())
    numf = int(input())
    numg = int(input())
    numh = int(input())
    numi = int(input())
    numj = int(input())
    numk = int(input())
    numl = int(input())
    numz = (((numi*numb)-(numa*numj))*((nume*numd)-(numa*numh))-\
        ((nume*numb)-(numa*numf))*((numi*numd)-(numa*numl)))\
        /(((numi*numb)-(numa*numj))*((nume*numc)-(numa*numg))-\
        ((nume*numb)-(numa*numf))*((numi*numc)-(numa*numk)))
    numy = (((numi*numc)-(numa*numk))*((nume*numd)-(numa*numh))-\
        ((nume*numc)-(numa*numg))*((numi*numd)-(numa*numl)))\
        /(((numi*numc)-(numa*numk))*((nume*numb)-(numa*numf))-\
        ((nume*numc)-(numa*numg))*((numi*numb)-(numa*numj)))
    numx = (numd-numb*numy-numc*numz)/numa
    print(int(numx), int(numy), int(numz))
main()
