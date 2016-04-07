

class ShapeError(Exception):
    pass


def shape(vector):

    return tuple((len(vector),))


def vector_add(first_vector, second_vector):

    if type(first_vector) and type(second_vector) is not list:
            return list(first_vector) + list(second_vector)

    if len(list(first_vector)) != len(list(second_vector)):
        raise ShapeError

    if type(first_vector[0]) is not list:
        return [first_vector[index] + value for index, value in enumerate(second_vector)]


def vector_sub(first_vector, second_vector):

    if type(first_vector) and type(second_vector) is not list:
            return first_vector - second_vector

    if len(list(first_vector)) != len(list(second_vector)):
        raise ShapeError

    if type(first_vector[0]) is not list:
        return [first_vector[index] - value for index, value in enumerate(second_vector)]


def vector_sum(*args):

    if len(args) == 1:
        return args[0]

    else:
        return vector_add(args[-1], vector_sum(*args[:-1]))


def dot(first_vector, second_vector):

    if len(list(first_vector)) != len(list(second_vector)):
        raise ShapeError

    if type(first_vector[0]) is not list:
        return sum([first_vector[index] * value for index, value in enumerate(second_vector)])

    if type(first_matrix[0]) and type(second_matrix[0]) is list:
        uneven_list_check = [index for index in range(len(first_matrix[0]))
                            if len(first_matrix[index]) != len(second_matrix[index])]
        if uneven_list_check != []:
            raise ShapeError


def vector_multiply(vector, scalar):

    return [vector[index] * scalar for index in range(len(vector))]


def vector_mean(first_vector, *args):

    return vector_multiply(vector_sum(first_vector, *args), 1/(len(args)+1))


def magnitude(vector):

        return (sum([vector[index]**2 for index in range(len(vector))]))**.5


def main():
    pass


if __name__ == '__main__':
    main()
