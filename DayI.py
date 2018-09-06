"""Day I """
def main():
    """calculate 366day of year"""
    year = int(input())
    year1 = year % 4
    year2 = year % 100
    year3 = year % 400
    if year1 == 0 and year2 == 0 and year3 == 0:
        print("Yes")
    elif year1 == 0 and year2 != 0:
        print("Yes")
    elif year1 == 0 and year3 == 0:
        print("Yes")
    else:
        print("No")
main()
