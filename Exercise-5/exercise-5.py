def first_last_same(list):
    print(f"Given list: {list}")

    if (list[0] == list[-1]):
        return "The result is TRUE."

    else :
        return "The result is FALSE."


numbers_x = [10, 20, 30, 40, 10]
print(first_last_same(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print(first_last_same(numbers_y))
