def scissionEquilibree(values):
    def _recursion(values, list1, list2):
        if len(values) == 0:
            return list1, list2
        r1, r2 = _recursion(values[1:], list1 + [values[0]], list2)
        s1, s2 = _recursion(values[1:], list1, list2 + [values[0]])
        if abs(sum(r1) - sum(r2)) < abs(sum(s1) - sum(s2)):
            return r1, r2
        return s1, s2

    return _recursion(values, [], [])

values = [3, 7, 4, 15, 17, 21, 24, 15, 31, 21]
s1, s2 = scissionEquilibree(values)
print(sum(s1), sum(s2))
print(s1)
print(s2)