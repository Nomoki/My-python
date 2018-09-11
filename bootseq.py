"""BootSequence"""
def main():
    """range numa and print last numa"""
    numa = int(input())
    for i in range(1, numa):
        print(i, end="_")
    print(numa, end="")
main()
