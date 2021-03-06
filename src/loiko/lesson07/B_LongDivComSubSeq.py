task = '''
Задача на дин. программирование: наибольшая кратная подпоследовательность

Дано:
    целое число 1≤n≤1000
    массив A[1…n] натуральных чисел, не превосходящих 2E9.

Необходимо:
    Выведите подпоследовательность индексов i[1]<i[2]<…<i[k] <= длины k,
    для которой каждый элемент A[i[j]] где 2<=j<k делится на предыдущий
    A[i[j-1]] без остатка.
    
    Найдите решение за время O(n*n) и восстановите подпоследовательность за время O(n) 
    не используя запоминание предыдущих элементов в оптимальном решении. 
    
    Индексы начинаются с 1.

Решить задачу МЕТОДАМИ ДИНАМИЧЕСКОГО ПРОГРАММИРОВАНИЯ

    Sample Input:
    4
    3 6 7 12

    Sample Output:
    1 2 4
'''

def getSeqIndexses(filename):
    # тут реализуйте логику задачи методами динамического программирования (!!!)
    # рекомендуется создать массив для найденных максимальных значений длины последовательности.
    # число в массиве означает достигнутую длину к этой точке.
    # индексы в обоих массивах при этом совпадают.
    # !!!!!!!!!!!!!!!!!!!!!!!!!     НАЧАЛО ЗАДАЧИ     !!!!!!!!!!!!!!!!!!!!!!!!!
    f = open(filename)
    n = int(f.readline().replace("\n", ''))
    array = list(map(int, f.readline().replace("\n", '').split(" ")))
    assert (n == len(array))
    d = [1] * len(array)
    ans = 0
    ians = -1
    for i in range(0, n):
        for j in range(0, i):
            if array[i] > array[j] and d[j] + 1 > d[i] and array[i] % array[j] == 0:
                d[i] = d[j] + 1
                if ans < d[i]:
                    ans = d[i]
                    ians = d[i]
    res = [0] * ans
    ires = ans - 1
    for i in range(ians, -1, -1):
        if d[ians] == d[i] + 1 and array[ians] % array[i] == 0 and array[ians] > array[i]:
            res[ires] = ians + 1
            ians = i
            ires -= 1
    res[0] = ians + 1
    return res
    # !!!!!!!!!!!!!!!!!!!!!!!!!     КОНЕЦ ЗАДАЧИ     !!!!!!!!!!!!!!!!!!!!!!!!!


def main():
    filename = "dataB.txt"
    answer = getSeqIndexses(filename)
    for i in answer: print(i,end=" ")


# Для ручной проверки нажмите Ctrl+Shift+F10
# установив курсор на  main
# или создайте конфигурацию Run-Edit configuration
if __name__ == "__main__":
    main()
