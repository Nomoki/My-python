"""SurprisingVote"""
def main():
    """Find lowest"""
    total = float(input())
    highest = float(input())
    num = total - highest
    lowest = (num - highest >= 0)*(num - highest)
    if highest - lowest > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
