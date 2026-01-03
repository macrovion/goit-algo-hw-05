import timeit
import os

# Алгоритм Боєра-Мура

def boyer_moore_search(text, pattern):
    
    m = len(pattern)
    n = len(text)
    if m == 0: return 0
    
    bad_char = {}
    for i in range(m):
        bad_char[pattern[i]] = i
    
    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pattern[j] == text[s + j]:
            j -= 1
        if j < 0:
            return s
        else:
            s += max(1, j - bad_char.get(text[s + j], -1))
    return -1



# Алгоритм Кнута-Морріса-Пратта

def kmp_search(text, pattern):
    
    m = len(pattern)
    n = len(text)
    if m == 0: return 0
    
    lps = [0] * m
    length = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    
    i = 0 
    j = 0 
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1




# Алгоритм Рабіна-Карпа

def rabin_karp_search(text, pattern):
    
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    if m == 0: return 0
    
    p = 0
    t = 0
    h = 1
    
    for i in range(m - 1):
        h = (h * d) % q
        
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
        
    for i in range(n - m + 1):
        if p == t:
            if text[i : i + m] == pattern:
                return i
        
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1


# читаємо файли

def read_file_content(filename):
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        print(f"ПОМИЛКА: Файл '{filename}' не знайдено у папці скрипта.")
        return ""
    except Exception as e:
        print(f"ПОМИЛКА при читанні '{filename}': {e}")
        return ""

# аналіз

if __name__ == "__main__":
    
    file_names = ["стаття 1.txt", "стаття 2.txt"]
    
    existing_substring = "алгоритм"       # слово, яке точно є
    fake_substring = "синхрофазотрон"     # вигадане слово
    
    # кількість повторень 
    iterations = 1000

    print(f"Починаємо тестування... (Кількість ітерацій: {iterations})\n")

    for fname in file_names:
        print(f"--- Аналіз файлу: {fname} ---")
        content = read_file_content(fname)
        
        if not content:
            print("Пропуск файлу через помилку читання.\n")
            continue

        for sub_type, sub_val in [("Існуючий", existing_substring), ("Вигаданий", fake_substring)]:
            print(f"  Підрядок: '{sub_val}' ({sub_type})")
            
            # вимірюємо час для кожного алгоритму
            
            t_bm = timeit.timeit(lambda: boyer_moore_search(content, sub_val), number=iterations)
            t_kmp = timeit.timeit(lambda: kmp_search(content, sub_val), number=iterations)
            t_rk = timeit.timeit(lambda: rabin_karp_search(content, sub_val), number=iterations)
            
            print(f"    Boyer-Moore:      {t_bm:.5f} сек")
            print(f"    KMP:              {t_kmp:.5f} сек")
            print(f"    Rabin-Karp:       {t_rk:.5f} сек")
            
            fastest_time = min(t_bm, t_kmp, t_rk)
            if fastest_time == t_bm: winner = "Boyer-Moore"
            elif fastest_time == t_kmp: winner = "KMP"
            else: winner = "Rabin-Karp"
            
            print(f"    >> Найшвидший: {winner}")
            print("-" * 30)
        print("\n")

        
