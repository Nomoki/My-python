"""inflation"""
def main():
    """print price . price"""
    price = float(input())
    years = int(input())
    price = int(price*100)
    for _ in range(0, years):
        num = price * 381
        num = num //10000
        price = price + num
    print("%d.%02d"%(price//100, price%100))
main()
