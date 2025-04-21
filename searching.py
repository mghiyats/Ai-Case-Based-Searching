import random
import math

POP_SIZE = 20
CHROM_LENGTH = 20
GEN_MAX = 50
X_MIN, X_MAX = -10, 10
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.01
BIT_LENGTH = 10

def decode_gene(gene):
    decimal = int(gene, 2)
    real = X_MIN + (decimal / (2**BIT_LENGTH - 1)) * (X_MAX - X_MIN)
    return real

def decode_chromosome(chrom):
    x1_bin = chrom[:BIT_LENGTH]
    x2_bin = chrom[BIT_LENGTH:]
    x1 = decode_gene(x1_bin)
    x2 = decode_gene(x2_bin)
    return x1, x2

def fitness(chrom):
    x1, x2 = decode_chromosome(chrom)
    try:
        val = - (math.sin(x1) * math.cos(x2) * math.tan(x1 + x2) + 0.75 * math.exp(1 - math.sqrt(x1**2)))
        return 1 / (1 + abs(val))
    except:
        return 0.0

def random_chrom():
    return ''.join(random.choice(['0', '1']) for _ in range(CHROM_LENGTH))

def select_parents(pop):
    candidates = random.sample(pop, 3)
    candidates.sort(key=lambda c: fitness(c), reverse=True)
    return candidates[0], candidates[1]

def crossover(parent1, parent2):
    if random.random() < CROSSOVER_RATE:
        point = random.randint(1, CHROM_LENGTH - 1)
        return parent1[:point] + parent2[point:], parent2[:point] + parent1[point:]
    return parent1, parent2

def mutate(chrom):
    return ''.join(
        bit if random.random() > MUTATION_RATE else ('1' if bit == '0' else '0')
        for bit in chrom
    )

def run_ga():
    population = [random_chrom() for _ in range(POP_SIZE)]
    best_solution = max(population, key=fitness)

    for generation in range(GEN_MAX):
        new_population = [best_solution]

        while len(new_population) < POP_SIZE:
            p1, p2 = select_parents(population)
            c1, c2 = crossover(p1, p2)
            new_population.extend([mutate(c1), mutate(c2)])

        population = new_population[:POP_SIZE]
        current_best = max(population, key=fitness)
        if fitness(current_best) > fitness(best_solution):
            best_solution = current_best

    x1, x2 = decode_chromosome(best_solution)
    final_value = - (math.sin(x1) * math.cos(x2) * math.tan(x1 + x2) + 0.75 * math.exp(1 - math.sqrt(x1**2)))
    print("Case Based Searching (NIM 1302220085 - 1302220109)")
    print("\nBest Chromosome:", best_solution)
    print("Nilai x1 =", x1)
    print("Nilai x2 =", x2)
    print("Nilai f(x1,x2) =", final_value)
    print("Fitness akhir =", fitness(best_solution))

if __name__ == "__main__":
    run_ga()