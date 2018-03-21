import random

NUMBERS_PER_LINE = 6
MIN_NUM = 1
MAX_NUM = 45


def main():
    num_of_picks = int(input("How many Quick Picks(TM):"))
    while num_of_picks <0 :
        print("Come on now, give in to the capitalist game to keep lining our pockets, forget about feeding your kids.")
        num_of_picks = int(input("Now we aren't going to ask again, HOW MANY QUICK PICKS?!"))

    for i in range(num_of_picks):
        quick_pick = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MIN_NUM, MAX_NUM)
            while number in quick_pick:
                number = random.randint(MIN_NUM, MAX_NUM)
            quick_pick.append(number)
        quick_pick.sort()
        print(" ".join("{:2}".format(number) for number in quick_pick))


main()