def split(list, delimiter):
    group = []
    for item in list:
        if item == delimiter:
            yield group
            group = []
        else:
            group.append(item)
    yield group
