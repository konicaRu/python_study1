def SynchronizingTables(N, ids, salary):
    ids_sort = sorted(ids)
    salary_sort = sorted(salary)
    ids_sal = dict(zip(ids_sort, salary_sort))
    salary_fin = []
    for i in ids:
        salary_fin.append(ids_sal[i])
    return salary_fin
