def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
#Python replace method
    dollars_without_sign = d.replace("$", "")
    return float(dollars_without_sign)


def percent_to_float(p):
    percent_without_sign = p.replace("%", "")
    percent_converted = float(percent_without_sign) / 100
        #converts to decimal 
    return percent_converted


main()