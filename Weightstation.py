"""WeightStation"""
def main():
    """find Weight input"""
    mean = float(input())
    wheel2 = float(input())
    wheel3 = float(input())
    wheel4 = float(input())
    wheel1 = float((mean*4) - wheel2 - wheel3 - wheel4)
    allwheel = wheel1 + wheel2 + wheel3 + wheel4
    halfmean1 = mean / 2
    mean1 = mean + halfmean1
    mean2 = mean - halfmean1
    if allwheel > 15000:
        print("Overweight")
    elif wheel1 > mean1 or wheel2 > mean1 or wheel3 > mean1 or \
        wheel4 > mean1 or wheel1 < mean2 or wheel2 < mean2 \
        or wheel3 < mean2 or wheel4 < mean2:
        print("Unbalance")
    else:
        print("Pass %.2f"%(wheel1))
main()
