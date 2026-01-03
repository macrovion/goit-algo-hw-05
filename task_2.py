def binary_search_upper_bound(arr, target):
        
    low = 0
    high = len(arr) - 1
    iterations = 0
    upper_bound = None

    while low <= high:
        iterations += 1
        mid = (low + high) // 2
        
        if arr[mid] < target:
            # якщо середній елемент менший за ціль, шукаємо в правій частині
            low = mid + 1
        else:
            # знайшовши потенційного кандидата, зберігаємо його як поточну "верхню межу".
            upper_bound = arr[mid]
            # продовжуємо пошук у лівій частині, щоб знайти ще менший елемент, який задовольняє умову або перше входження
            high = mid - 1
            
    return (iterations, upper_bound)


# Тести

# Відсортований масив дробових чисел
sorted_floats = [0.5, 1.2, 2.4, 3.6, 3.6, 4.8, 5.1, 7.3, 9.9]

# Тест 1: Число є в масиві (3.6)
target1 = 3.6
result1 = binary_search_upper_bound(sorted_floats, target1)
print(f"Ціль: {target1} -> Результат: {result1}") 
# Очікуємо: кортеж з ітераціями та 3.6

# Тест 2: Числа немає, шукаємо "верхню межу" для 4.0
target2 = 4.0
result2 = binary_search_upper_bound(sorted_floats, target2)
print(f"Ціль: {target2} -> Результат: {result2}") 
# Очікуємо: кортеж з ітераціями та 4.8 (найменше число >= 4.0)

# Тест 3: Число більше за всі елементи масиву
target3 = 15.5
result3 = binary_search_upper_bound(sorted_floats, target3)
print(f"Ціль: {target3} -> Результат: {result3}") 
# Очікуємо: (ітерації, None), бо немає елемента >= 15.5
