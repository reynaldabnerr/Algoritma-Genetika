import random

# Parameter Algoritma Genetika
POPULATION_SIZE = 100           # Jumlah populasi
MUTATION_RATE = 0.01            # Peluang mutasi
MAX_GENERATIONS = 10000          # Batas maksimum generasi

# Karakter yang mungkin muncul dalam solusi
CHAR_SET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ 1234567890"

# Fungsi untuk menghasilkan string acak
def random_string(length):
    return ''.join(random.choice(CHAR_SET) for _ in range(length))

# Fungsi untuk menghitung fitness (kesesuaian dengan TARGET_STRING)
def fitness(individual, target_string):
    return sum(1 for i, j in zip(individual, target_string) if i == j)

# Fungsi untuk melakukan seleksi berdasarkan turnamen seleksi
def select(population, target_string):
    tournament_size = 5
    tournament = random.sample(population, tournament_size)
    tournament = sorted(tournament, key=lambda x: fitness(x, target_string), reverse=True)
    return tournament[0], tournament[1]

# Fungsi crossover untuk menghasilkan keturunan baru (dua titik crossover)
def crossover(parent1, parent2, target_string):
    pivot1 = random.randint(0, len(target_string) - 1)
    pivot2 = random.randint(pivot1, len(target_string) - 1)
    child = parent1[:pivot1] + parent2[pivot1:pivot2] + parent1[pivot2:]
    return child

# Fungsi mutasi untuk memperkenalkan variasi
def mutate(individual):
    individual = list(individual)
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = random.choice(CHAR_SET)
    return ''.join(individual)

# Fungsi utama untuk menjalankan Algoritma Genetika
def genetic_algorithm(target_string):
    # Inisialisasi populasi awal
    population = [random_string(len(target_string)) for _ in range(POPULATION_SIZE)]

    for generation in range(MAX_GENERATIONS):
        # Evaluasi populasi
        population = sorted(population, key=lambda x: fitness(x, target_string), reverse=True)

        # Jika solusi ditemukan
        if fitness(population[0], target_string) == len(target_string):
            print(f"Solution found in generation {generation} : {population[0]}")
            return population[0]

        # Seleksi dan reproduksi
        new_population = []
        for _ in range(POPULATION_SIZE // 2):
            parent1, parent2 = select(population, target_string)
            child1 = mutate(crossover(parent1, parent2, target_string))
            child2 = mutate(crossover(parent2, parent1, target_string))
            new_population.extend([child1, child2])

        population = new_population

        # Print status generasi saat ini
        print(f"Generation {generation}, Best: {population[0]}, Fitness: {fitness(population[0], target_string)}")

    print("Solution not found within the maximum number of generations.")
    return None

# Jalankan algoritma
if __name__ == "__main__":
    target_string = input("Enter the target strings : ")
    genetic_algorithm(target_string)