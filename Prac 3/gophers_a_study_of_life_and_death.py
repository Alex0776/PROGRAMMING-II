import random
INITIAL_GOPHERS = 1000


def main():
    print("""Welcome to the Gopher Population Simulator!
Starting Population: 1000""")
current_year = 0
while current_year >= 10:
    birth_rate = float(birth_rate_gen(birth_rate))
    death_rate = float death_rate_gen(death_rate)
    population = float pop_gen(population)

print("Year ", current_year + 1,
            "*****",
            birth_rate, " gophers were born.", death_rate, " passed, for is the cruel mistress that is nature",
            "Population: ", population)
else:
        birth_rate = birth_rate_gen
        death_rate = death_rate_gen
        population = pop_gen


def birth_rate_gen(birth_rate, population):
    birth_rate = population * random.int[0.1, 0.2]
    return birth_rate


def death_rate_gen(death_rate, population):
    death_rate = population * random.int[0.05, 0.25]
    return death_rate


def pop_gen(birth_rate, death_rate, population):
    population = population + birth_rate - death_rate
    return population


main()