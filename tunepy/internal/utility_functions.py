
def get_best_genome(genomes):
    best_fitness = float('-inf')
    best_genome = None
    for genome in genomes:
        if genome.fitness > best_fitness:
            best_genome = genome
    return best_genome
