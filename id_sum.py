def id_sum(id):
    result = 0
    while id > 0:
        result += id % 10
        id //= 10
    return result


def customers_in_groups(n_customers, n_first_id = 0):
    groups = {}
    for i in range(n_first_id, n_first_id+n_customers):
        i = id_sum(i)
        if groups.get(i): groups[i] += 1
        else: groups[i] = 1
    return groups