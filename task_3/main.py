# Завдання 3

import os
import timeit
from bm import boyer_moore_search
from kmp import kmp_search
from rk import rabin_karp_search

if __name__ == "__main__":
    # Абсолютний шлях до файлу main.py
    current_file_path = os.path.abspath(__file__)

    # Абсолютний шлях до папки, з якої запускається файл main.py
    current_directory = os.path.dirname(current_file_path)

    # Абсолютний шлях до файлів статей у поточній директорії
    article_1_path = os.path.join(current_directory, "article_1.txt")
    article_2_path = os.path.join(current_directory, "article_2.txt")

    with open(article_1_path, "r") as f:
        text1 = f.read()

    with open(article_2_path, "r") as f:
        text2 = f.read()

    pattern1 = "Інтерполяційний пошук використовується для пошуку елементів у відсортованому масиві"
    pattern2 = (
        "В статті проведено дослідження різних структур даних, які можна використати"
    )

    # Пошук підрядка 1 в статті 1
    bm_pattern1_t1 = timeit.timeit(
        lambda: boyer_moore_search(text1, pattern1), number=10
    )
    bm_pattern1_t1_pos = boyer_moore_search(text1, pattern1)
    kmp_pattern1_t1 = timeit.timeit(lambda: kmp_search(text1, pattern1), number=10)
    kmp_pattern1_t1_pos = kmp_search(text1, pattern1)
    rk_pattern1_t1 = timeit.timeit(
        lambda: rabin_karp_search(text1, pattern1), number=10
    )
    rk_pattern1_t1_pos = rabin_karp_search(text1, pattern1)

    # Пошук підрядка 1 в статті 2
    bm_pattern1_t2 = timeit.timeit(
        lambda: boyer_moore_search(text2, pattern1), number=10
    )
    bm_pattern1_t2_pos = boyer_moore_search(text2, pattern1)
    kmp_pattern1_t2 = timeit.timeit(lambda: kmp_search(text2, pattern1), number=10)
    kmp_pattern1_t2_pos = kmp_search(text2, pattern1)
    rk_pattern1_t2 = timeit.timeit(
        lambda: rabin_karp_search(text2, pattern1), number=10
    )
    rk_pattern1_t2_pos = rabin_karp_search(text2, pattern1)

    # Пошук підрядка 2 в статті 1
    bm_pattern2_t1 = timeit.timeit(
        lambda: boyer_moore_search(text1, pattern2), number=10
    )
    bm_pattern2_t1_pos = boyer_moore_search(text1, pattern2)
    kmp_pattern2_t1 = timeit.timeit(lambda: kmp_search(text1, pattern2), number=10)
    kmp_pattern2_t1_pos = kmp_search(text1, pattern2)
    rk_pattern2_t1 = timeit.timeit(
        lambda: rabin_karp_search(text1, pattern2), number=10
    )
    rk_pattern2_t1_pos = rabin_karp_search(text1, pattern2)

    # Пошук підрядка 2 в статті 2
    bm_pattern2_t2 = timeit.timeit(
        lambda: boyer_moore_search(text2, pattern2), number=10
    )
    bm_pattern2_t2_pos = boyer_moore_search(text2, pattern2)
    kmp_pattern2_t2 = timeit.timeit(lambda: kmp_search(text2, pattern2), number=10)
    kmp_pattern2_t2_pos = kmp_search(text2, pattern2)
    rk_pattern2_t2 = timeit.timeit(
        lambda: rabin_karp_search(text2, pattern2), number=10
    )
    rk_pattern2_t2_pos = rabin_karp_search(text2, pattern2)

    # Результати пошуку
    dividing_line1 = (
        f"| {'-'*20:^20} | {'-'*20:^20} | {'-'*20:^20} | {'-'*20:^20} | {'-'*20:^20} |"
    )
    dividing_line2 = f"| {'-'*20:^20} | {'-'*9:^9} | {'-'*8:^8} | {'-'*9:^9} | {'-'*8:^8} | {'-'*9:^9} | {'-'*8:^8} | {'-'*9:^9} | {'-'*8:^8} |"
    print(dividing_line1)
    print(
        f"| {'Алгоритм пошуку':^20} | {'Стаття1 vs Паттерн1':^20} | {'Стаття1 vs Паттерн2':^20} | {'Стаття2 vs Паттерн2':^20} | {'Стаття2 vs Паттерн1':^20} |"
    )
    print(
        f"| {' '*20:^20} | {'-'*20:^20} | {'-'*20:^20} | {'-'*20:^20} | {'-'*20:^20} |"
    )
    print(
        f"| {' '*20:^20} | {'Позиція':^9} | {'Час':^8} | {'Позиція':^9} | {'Час':^8} | {'Позиція':^9} | {'Час':^8} | {'Позиція':^9} | {'Час':^8} |"
    )
    print(dividing_line1)
    print(
        f"| {'Боєра-Мура':^20} | {bm_pattern1_t1_pos:^9} | {bm_pattern1_t1:^8.6f} | {bm_pattern2_t1_pos:^9} | {bm_pattern2_t1:^8.6f} | {bm_pattern2_t2_pos:^9} | {bm_pattern2_t2:^8.6f} | {bm_pattern1_t2_pos:^9} | {bm_pattern1_t2:^8.6f} |"
    )
    print(
        f"| {'Кнута-Морріса-Пратта':^20} | {kmp_pattern1_t1_pos:^9} | {kmp_pattern1_t1:^8.6f} | {kmp_pattern2_t1_pos:^9} | {kmp_pattern2_t1:^8.6f} | {kmp_pattern2_t2_pos:^9} | {kmp_pattern2_t2:^8.6f} | {kmp_pattern1_t2_pos:^9} | {kmp_pattern1_t2:^8.6f} |"
    )
    print(
        f"| {'Рабіна-Карпа':^20} | {rk_pattern1_t1_pos:^9} | {rk_pattern1_t1:^8.6f} | {rk_pattern2_t1_pos:^9} | {rk_pattern2_t1:^8.6f} | {rk_pattern2_t2_pos:^9} | {rk_pattern2_t2:^8.6f} | {rk_pattern1_t2_pos:^9} | {rk_pattern1_t2:^8.6f} |"
    )
    print(dividing_line2)

    # Висновок
    print(
        """Висновок:
          З результатів виконання програми видно, що алгоритм Боєра-Мура швидше за інші впорався з пошуком підрядків в обох статтях.
          Це пов'язано з тим, що алгоритм Боєра-Мура має складність: у найкращому випадку O(n), а у найгіршому випадку O(n*m).
          Серед інших двох алгоритмів, швидше працює алгоритм Кнута-Морріса-Пратта.
          Алгоритм Кнута-Морріса-Пратта має складність O(n+m), а алгоритм Рабіна-Карпа має складність: у середньому та найкращому випадку O(n+m), а у найгіршому випадку O(n*m).
          Таким чином, алгоритм Боєра-Мура виявився найефективнішим для пошуку підрядка в тексті."""
    )
