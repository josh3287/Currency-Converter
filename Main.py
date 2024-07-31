def main():
    print("This program converts US dollars to pounds")
    print()

    dollars = eval(input("Enter dollar amount: "))
    pounds = convert_to_pounds(dollars)

    print("That is ", pounds, "pounds.")


convert_to_pounds = lambda dollars: dollars * 0.82

main()