import matplotlib.pyplot as plt


def fitness(x):
    return -x ** 2 + 2 * x


def crossover(parent1, parent2):
    child1 = parent1[0] + parent2[1:4] + parent1[4]
    child2 = parent2[0] + parent1[1:4] + parent2[4]
    return child1, child2


def scaled_value(value):
    minR1, maxR1 = 0, 31
    minR2, maxR2 = 0, 2
    scaled = minR2 + (maxR2 - minR2) * (value - minR1) / (maxR1 - minR1)
    return scaled


population = ["11010", "00111", "10110", "00101"]
random_numbers = [0.4, 0.15, 0.7, 0.9]

print("Initial Population:")
print(population)

max_fitness_values = []

fitness_scores = [fitness(scaled_value(int(individual, 2))) for individual in population]
print("\nFitness Scores for Initial Population:")
print(fitness_scores)

max_fitness_values.append(max(fitness_scores))
print("\nMaximum Fitness in Initial Population:", max_fitness_values[-1])

next_generation = []
for i in range(0, len(population), 2):
    child1, child2 = crossover(population[i], population[i + 1])
    next_generation.extend([child1, child2])

print("\nNext Generation:")
print(next_generation)

fitness_scores = [fitness(scaled_value(int(individual, 2))) for individual in next_generation]
print("\nFitness Scores for Next Generation:")
print(fitness_scores)

max_fitness_values.append(max(fitness_scores))
print("\nMaximum Fitness in Next Generation:", max_fitness_values[-1])

plt.plot(range(0, len(max_fitness_values)), max_fitness_values, marker='o')
plt.xlabel('Generation')
plt.ylabel('Maximum Fitness')
plt.title('Maximum Fitness for Each Generation')
plt.grid(True)
plt.xticks(range(0, len(max_fitness_values)))
plt.ylim(min(max_fitness_values) - 0.05, max(max_fitness_values) + 0.05)
plt.show()
