def LineAnalysis(line):
    arr_dot = []
    arr_star = []
    elem_dot = ''
    elem_star = ''
    for i in range(len(line)):
        if line[i] == '*':
            elem_star += '*'
        if line[i] == '.' and elem_star != '':
            arr_star.append(elem_star)
            elem_star = ''
        if line[i] == '.':
            elem_dot += '.'
        if line[i] == '*' and elem_dot != '':
            arr_dot.append(elem_dot)
            elem_dot = ''
        if i == len(line) - 1:
            arr_star.append(elem_star)
    if arr_star[1:] == arr_star[:-1] and arr_dot[1:] == arr_dot[:-1] and line[0] == '*' and line[-1] == '*':
        return True
    else:return False

