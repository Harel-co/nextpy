from functools import reduce

def mul_and_reduce(digit):
    digit = int(digit) * 2
    return digit - 9 if digit > 9 else digit

def check_id_valid(id_number):
    """
    function checks if the id is valid (sum of digits can be divided by 10)
    returns boolean
    """
    sum = reduce(lambda x, y: x+y, [(mul_and_reduce(id_number[i]) if (i+1) % 2 == 0 else int(id_number[i])) for i in range(0, len(id_number))])
    return sum % 10 == 0 


class IDIterator():
    def __init__(self, id):
        self._id = int(id)

    def __iter__(self):
        return self

    def __next__(self):
        """
        iterates to the next valid id
        raises StopIteration if the next valid id is bigger than 999,999,999
        """
        self._id += 1
        if self._id > 999_999_999:
            raise StopIteration()
        while not check_id_valid(str(self._id)):
            self._id += 1
            if self._id > 999_999_999:
                raise StopIteration()
        return self._id


def id_generator(id):
    """
    yields the next valid id
    raises StopIteration if the next valid id is bigger than 999,999,999
    :param id: the id to start from
    :type id: int (smaller than 999,999,999)
    """
    while True:
        id += 1
        if id > 999_999_999:
            raise StopIteration()
        while not check_id_valid(str(id)):
            id += 1
            if id > 999_999_999:
                raise StopIteration()
        yield id


def main():
    id = int(input('Enter ID: '))
    iterator = IDIterator(id)
    gen = id_generator(id)
    if 'it' == input('Generator or Iterator? (gen/it)? '):
        for i in range(10):
            print(next(iterator))
    else:
        for i in range(10):
            print(next(gen))


if __name__ == "__main__":
    main()