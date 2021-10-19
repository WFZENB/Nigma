list_of_values = ("45", "4", "78", "-47")


def mean(values):                                       # Среднее значение (все значения/на количество значений)
    value_sum = 0
    for i in range(len(values)):
        value_sum = value_sum + int(values[i])
    value_mean = (value_sum/len(values))
    return value_mean


def maximum(values):                                    # Нахождение максимума
    value_maximum = -10000000
    for i in range(len(values)):
        if int(values[i]) >= value_maximum:
            value_maximum = int(values[i])
    return value_maximum


def minimum(values):                                    # Нахождение минимума
    value_minimum = 10000000
    for i in range(len(values)):
        if int(values[i]) <= value_minimum:
            value_minimum = int(values[i])
    return value_minimum


print(maximum(list_of_values), minimum(list_of_values), mean(list_of_values))
