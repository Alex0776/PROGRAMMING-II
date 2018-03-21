def main():
    """Display income report for incomes over a given number of months_worked."""
    incomes = []
    months_worked = int(input("How many months_worked? "))

    for month in range(1, months_worked + 1):
        income = float(input("Enter income for month " + str(month) + ": "))
        incomes.append(income)

    income_report_generator(incomes, months_worked)


def income_report_generator(incomes, months_worked):
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, months_worked + 1):
        income = incomes[month - 1]
        total += income
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))


main()