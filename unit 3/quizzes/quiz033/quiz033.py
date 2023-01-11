def mystery(list1, list2):
    output = []

    for i in list1:
        for n in list2:
            if i == n:
                output.append(i)

    return output
    