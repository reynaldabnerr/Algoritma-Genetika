import random

# Parameter Algoritma Genetika
TARGET_STRING = "Reynald Abner Tananda"  # String yang ingin dicari
POPULATION_SIZE = 100           # Jumlah populasi
MUTATION_RATE = 0.01            # Peluang mutasi
MAX_GENERATIONS = 10000          # Batas maksimum generasi

# Karakter yang mungkin muncul dalam solusi
CHAR_SET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890!@#$%^&*()-_=+"

# Fungsi untuk menghasilkan string acak
def random_string(length):
    return ''.join(random.choice(CHAR_SET) for _ in range(length))

# Fungsi untuk menghitung fitness (kesesuaian dengan TARGET_STRING)
def fitness(individual):
    return sum(1 for i, j in zip(individual, TARGET_STRING) if i == j)

# Fungsi untuk melakukan seleksi berdasarkan probabilitas fitness
def select(population):
    total_fitness = sum(fitness(ind) for ind in population)
    probabilities = [fitness(ind) / total_fitness for ind in population]
    return random.choices(population, probabilities, k=2)

# Fungsi crossover untuk menghasilkan keturunan baru
def crossover(parent1, parent2):
    pivot = random.randint(0, len(TARGET_STRING) - 1)
    child = parent1[:pivot] + parent2[pivot:]
    return child

# Fungsi mutasi untuk memperkenalkan variasi
def mutate(individual):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = random.choice(CHAR_SET)
    return ''.join(individual)

# Fungsi utama untuk menjalankan Algoritma Genetika
def genetic_algorithm():
    # Inisialisasi populasi awal
    population = [random_string(len(TARGET_STRING)) for _ in range(POPULATION_SIZE)]

    for generation in range(MAX_GENERATIONS):
        # Evaluasi populasi
        population = sorted(population, key=fitness, reverse=True)

        # Jika solusi ditemukan
        if fitness(population[0]) == len(TARGET_STRING):
            print(f"Solution found in generation {generation}: {population[0]}")
            return population[0]

        # Seleksi dan reproduksi
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1, parent2 = select(population)
            child1 = mutate(crossover(parent1, parent2))
            child2 = mutate(crossover(parent2, parent1))
            new_population.extend([child1, child2])

        population = new_population

        # Print status generasi saat ini
        print(f"Generation {generation}, Best: {population[0]}, Fitness: {fitness(population[0])}")

    print("Solution not found within the maximum number of generations.")
    return None

# Jalankan algoritma
if __name__ == "__main__":
    genetic_algorithm()