import random

# swapping random genes between a pair of chromosomes
def hybridization(first_genom, second_genom, probability):
    for gene in range(0, len(first_genom)):
        if (random.random() < probability):
            first_genom[gene], second_genom[gene] = second_genom[gene], first_genom[gene]
    return first_genom, second_genom

# generate a new population with random gene shuffling
def generate_next_population(actual_generation, probability):
    for genom_index in range(0, len(actual_generation)):
        random_genom_index = random.randint(0, len(actual_generation) - 1)
        actual_generation[genom_index], actual_generation[random_genom_index] = \
            hybridization(actual_generation[genom_index],
                          actual_generation[random_genom_index], probability)
    return actual_generation
