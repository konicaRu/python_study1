def BalancedParentheses(n):
    n *= 2
    arr = ['(' for _ in range(n // 2)] + [')' for _ in range(n // 2)]  # печатаем нулевую последовательность
    line = ''
    while True:
        for j in arr:
            line += j
        line += ' '
        ind = n - 1  # разница между скобками
        cnt = 0  # индекс, по которому кладем скобку в список
        # находим откр. скобку, которую можно заменить
        while ind >= 0:
            if arr[ind] == ')':
                cnt -= 1
            if arr[ind] == '(':
                cnt += 1
            if cnt < 0 and arr[ind] == '(':
                break
            ind -= 1
        # если не нашли, то алгоритм заканчивает работу
        if ind < 0:
            break
        # заменяем на закр. скобку
        arr[ind] = ')'
        # заменяем на самую лексикографическую минимальную
        for i in range(ind + 1, n):
            if i <= (n - ind + cnt) / 2 + ind:
                arr[i] = '('
            else:
                arr[i] = ')'
    return line
