from functools import reduce

def main():
    with open('./resources/unit1-names.txt', 'r') as file:
        # question 1 - i thought of 2 solutions and they both work (i used read().split('\n') and not readline() to avoid the \n)
        print(sorted(file.read().split('\n'), key=len, reverse=True)[0])
        
        file.seek(0)
        # or
        print(reduce(lambda x, y: x if len(x)>len(y) else y, file.read().split('\n')))

        file.seek(0)
        # question 2
        print(reduce(lambda x, y: x+len(y) , file.read().split('\n'), 0))

        file.seek(0)
        # question 3
        lines = sorted(file.read().split('\n'), key=len)
        print('\n'.join(filter(lambda x: len(x) == len(lines[0]), lines)))

        file.seek(0)
        # question 4
        with open('./resources/unit1-name_length.txt', 'w') as resfile:
            resfile.write('\n'.join([str(len(name)) for name in file.read().split('\n')]))
        
        file.seek(0)
        # question 5
        length = input('Enter name length: ')
        print('\n'.join(filter(lambda x: len(x) == int(length), file.read().split('\n'))))
        


if __name__ == '__main__':
    main()
