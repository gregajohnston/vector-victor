

def shape(list_or_matrix):
    if type(list_or_matrix[0]) is not list:
        return tuple((len(list_or_matrix),))
    return tuple((len(list_or_matrix), len(list_or_matrix[0])))


def main():
    pass


if __name__ == '__main__':
    main()
