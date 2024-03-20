import random

# swapping random genes between a pair of INCORRECT chromosomes
def duel(population, duelists, probability):
    for duelist in duelists:
        if (random.random() < probability):
            person = random.randint(0, 4)
            bad_match_id = random.choice(duelists)
            population[duelist][person], population[bad_match_id][person] = \
                population[bad_match_id][person], population[duelist][person]
    return population
