def main():
    while True:
        try:
            fraction = (input("Fraction: "))
            percentage = convert(fraction)
            answer = gauge(percentage)
            print(answer)
        except ValueError:
            print("This was a value error.")
            pass
        except ZeroDivisionError:
            print("This was a zero division error.")
            pass

def convert(frac_number):
        frac_number = frac_number.split("/")
        x = int(frac_number[0])
        y = int(frac_number[1])
        percentageNew = int((x/y)*100)
        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError
        else:
            return percentageNew

def gauge(number):
    if number <= 1:
        output = ("E")
    elif number >= 99:
        output = ("F")
    else:
        output = (f"{number}%")
    return output

if __name__ == "__main__":
    main()