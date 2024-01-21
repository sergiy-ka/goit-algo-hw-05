## Результати порівняння ефективності алгоритмів пошуку підрядка: Боєра-Мура, Кнута-Морріса-Пратта та Рабіна-Карпа на основі двох текстових файлів ([стаття 1](https://drive.google.com/file/d/18_R5vEQ3eDuy2VdV3K5Lu-R-B-adxXZh/view), [стаття 2](https://drive.google.com/file/d/13hSt4JkJc11nckZZz2yoFHYL89a4XkMZ/view)).

### Підрядки, використані у пошуку

    pattern1 = "Інтерполяційний пошук використовується для пошуку елементів у відсортованому масиві"
    pattern2 = "В статті проведено дослідження різних структур даних, які можна використати"

### Порівняльна таблиця з результатами пошуку

    | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
    |   Алгоритм пошуку    | Стаття1 vs Паттерн1  | Стаття1 vs Паттерн2  | Стаття2 vs Паттерн2  | Стаття2 vs Паттерн1  |
    |                      | -------------------- | -------------------- | -------------------- | -------------------- |
    |                      |  Позиція  |   Час    |  Позиція  |   Час    |  Позиція  |   Час    |  Позиція  |   Час    |
    | -------------------- | -------------------- | -------------------- | -------------------- | -------------------- |
    |      Боєра-Мура      |   5938    | 0.002176 |    -1     | 0.002431 |   5714    | 0.001473 |    -1     | 0.003167 |
    | Кнута-Морріса-Пратта |   5938    | 0.012105 |    -1     | 0.021337 |   5714    | 0.011298 |    -1     | 0.031287 |
    |     Рабіна-Карпа     |   5938    | 0.024760 |    -1     | 0.054511 |   5714    | 0.029537 |    -1     | 0.075937 |
    | -------------------- | --------- | -------- | --------- | -------- | --------- | -------- | --------- | -------- |

## Висновки

    З результатів виконання програми видно, що алгоритм Боєра-Мура швидше за інші впорався з пошуком підрядків в обох статтях.
    Це пов'язано з тим, що алгоритм Боєра-Мура має складність: у найкращому випадку O(n), а у найгіршому випадку O(n*m).
    Серед інших двох алгоритмів, швидше працює алгоритм Кнута-Морріса-Пратта.
    Алгоритм Кнута-Морріса-Пратта має складність O(n+m), а алгоритм Рабіна-Карпа має складність: у середньому та найкращому випадку O(n+m), а у найгіршому випадку O(n*m).
    Таким чином, алгоритм Боєра-Мура виявився найефективнішим для пошуку підрядка в тексті.