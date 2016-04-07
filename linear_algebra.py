

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

    return_value = vector[:]
    #return_value[] = [matrix[index] * scalar for index in range(len(matrix))]
    for index in range(len(vector)):
        return_value[index] = vector[index] * scalar
    return return_value


    # total_vector = vector_add(first_vector, second_vector)
    # total_vector = [vector_add(total_vector, arg) for arg in args]
    # return total_vector

    # for arg in args:
    #     return_value = vector_add(return_value, arg)
    #return_value = [vector_add(x,y) for x,y in zip(return_value, args)]




# def shape(matrix):
#
#     if type(matrix[0]) is not list:
#         return tuple((len(matrix),))
#
#     return tuple((len(matrix), len(matrix[0])))
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# def vector_add(first_matrix, second_matrix):
#     if type(first_matrix) and type(second_matrix) is not list:
#             return first_matrix + second_matrix
#
#     if len(first_matrix) != len(second_matrix):
#         raise ShapeError
#
#     if type(first_matrix[0]) is not list:
#         return [x + y for x, y in zip(first_matrix, second_matrix)]
#
#     if type(first_matrix[0]) and type(second_matrix[0]) is list:
#         uneven_list_check = [index for index in range(len(first_matrix[0]))
#                             if len(first_matrix[index]) != len(second_matrix[index])]
#         if uneven_list_check != []:
#             raise ShapeError
#
####################################
# def vector_sub(first_matrix, second_matrix):
#     if len(first_matrix) != len(second_matrix):
#         raise ShapeError
#
#     if type(first_matrix[0]) is not list:
#         return [x - y for x, y in zip(first_matrix, second_matrix)]
#
#     if type(first_matrix[0]) and type(second_matrix[0]) is list:
#         uneven_list_check = [index for index in range(len(first_matrix[0]))
#                             if len(first_matrix[index]) != len(second_matrix[index])]
#         if uneven_list_check != []:
#             raise ShapeError
#
####################################
# def vector_sum(first_matrix, *args):
#     return_value = first_matrix[:]
#     for arg in args:
#         return_value = vector_add(return_value, arg)
#     #return_value = [vector_add(x,y) for x,y in zip(return_value, args)]
#     return return_value

# def vector_multiply(matrix, scalar):
#
#     return_value = matrix[:]
#     #return_value[] = [matrix[index] * scalar for index in range(len(matrix))]
#     for index in range(len(matrix)):
#         return_value[index] = matrix[index] * scalar
#     return return_value







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

# def magnitude():
#     pass

def main():
    pass


if __name__ == '__main__':
    main()
