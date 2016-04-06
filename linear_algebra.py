class ShapeError(Exception):
    pass


def shape(matrix):
    if type(matrix[0]) is not list:
        return tuple((len(matrix),))
    return tuple((len(matrix), len(matrix[0])))


def vector_add(first_matrix, second_matrix):
    if len(first_matrix) != len(second_matrix):
        raise ShapeError


    if type(first_matrix[0]) is list and type(second_matrix[0]) is list:
        for index in range(len(first_matrix[0])):
            if len(first_matrix[index]) != len(second_matrix[index]):
                raise ShapeError

    if type(first_matrix[0]) is not list:
        return [x + y for x, y in zip(first_matrix, second_matrix)]

    # return_value = [zip(x, y) for x, y in zip(first_matrix, second_matrix)]
    # for index in range(len(return_value)):
    #     a = list[return_value[index]]
    # for index in range(len(return_value)):
    #     return_value[index] = sum(return_value[index])
    # return return_value


def vector_sub(first_matrix, second_matrix):
    if len(first_matrix) != len(second_matrix):
        raise ShapeError

    if type(first_matrix[0]) is list and type(second_matrix[0]) is list:
        for index in range(len(first_matrix[0])):
            if len(first_matrix[index]) != len(second_matrix[index]):
                raise ShapeError

    if type(first_matrix[0]) is not list:
        return [x - y for x, y in zip(first_matrix, second_matrix)]


def vector_sum(first_matrix, *args):
    return_value = first_matrix
    for arg in args:
        return_value = vector_add(return_value, arg)
    return return_value


def dot(first_matrix, second_matrix):
    if len(first_matrix) != len(second_matrix):
        raise ShapeError

    if type(first_matrix[0]) is list and type(second_matrix[0]) is list:
        for index in range(len(first_matrix[0])):
            if len(first_matrix[index]) != len(second_matrix[index]):
                raise ShapeError

    if type(first_matrix[0]) is not list:
        return sum([x * y for x, y in zip(first_matrix, second_matrix)])


def vector_multiply(matrix, scalar):
    return_value = matrix[:]
    for index in range(len(matrix)):
        return_value[index] = matrix[index] * scalar
    return return_value


def vector_sum_for_mean(first_matrix, *args):
    return_value = first_matrix
    count = 1
    for arg in args:
        return_value = vector_add(return_value, arg)
        count += 1
    return return_value, count


def vector_mean(first_matrix, *args):
    return_value, count = vector_sum_for_mean(first_matrix, *args)
    return_value = vector_multiply(return_value, 1/count)
    return return_value


def main():
    pass


if __name__ == '__main__':
    main()
