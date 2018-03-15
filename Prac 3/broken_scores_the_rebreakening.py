def main():
    score = float(input("Enter your score: "))
    score_calculator(score)
    if score >=90:
        print("Your score is: ", score_calculator(score)," You aced it, champ!")
    elif score >=50:
        print("Your score is: ", score_calculator(score)," Barely scraped through, study MOAR!!")
    else:
        print("Your score is: ", score_calculator(score)," You've let your family down, you've let the team down, but most importantly, you've let yourself down.")


def score_calculator(score):
    if score < 0 or score > 100:
        return("Invalid score, try again")
    elif score >= 90:
        return("Excellent.")
    elif score >= 50:
        return("Passable.")
    else:
        return("Bad.")


main()