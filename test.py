list_of_values = ("45", "2", "78", "-47")

# Извлекаем оценки из датасета
scores = [int(w[3]) for w in list_of_values]

# Складываем все оценки
sum_score = sum(scores)

# Ищем количество оценок
num_score = len(scores)

# Считаем среднее значение
avg_score = sum_score/num_score

print(avg_score)  # выводит 87.8884184721394
