class ShapeError(Exception):
    pass



def shape(list_or_matrix):
    if type(list_or_matrix[0]) is not list:
        return tuple((len(list_or_matrix),))
    return tuple((len(list_or_matrix), len(list_or_matrix[0])))

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


def main():
    pass


if __name__ == '__main__':
    main()
