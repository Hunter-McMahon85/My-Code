print([list(range(3)), list(range(3))])
#   [[0, 1, 2], [0, 1, 2]]	list
print([[1, 2, 3], [4, 5, 6]][1][2])
# exp: 3 (int) got: 6
print([x % 2 for x in [0, 1, 2, 3, 4]])
# exp: [1,2,3,4] (list) got: [0, 1, 0, 1, 0]
my_list = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
print(my_list[2][2].append(7000))
# exp: [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40] (list) got:
print([i for i in [5, 20, 15, 20, 25, 50, 20] if i != 20])
# exp: [5, 15, 25, 50] (list) got: exp
print(3 * [1, 2, 3])
# exp:[1,2,3,1,2,3,1,2,3] got: exp
print(3 * [[1, 2, 3]])
# exp: [[1, 2, 3],[1, 2, 3],[1, 2, 3]] got:exp
print([x + y for x, y in zip(['Si', 'goo'], ['lly', 'se!'])])
# exp: ['Sigoo', 'llyse!'] got: ['Silly', 'goose!']
print({('Name', str): ['Bob', 'Lisa', 'Jill'], ('Age', int): [21, 19, 23]}[('Name', str)])
# exp: ['Bob', 'Lisa', 'Jill'] got: exp
print({('Name', str): ['Bob', 'Lisa', 'Jill'], ('Age', int): [21, 19, 23]}[('Age', int)])
# exp: [21, 19, 23] got: exp
print({('Name', str): ['Bob', 'Lisa', 'Jill'], ('Age', int): [21, 19, 23]}[('Name', str)][0])
# exp: 'bob'got: exp
print({'A' : {'a': [1, 2, 3], 'b': [4, 5, 6]}, 'B': 'Bananas'}['B'])
# exp: 'Bananas' got: exp
print({'A' : {'a': [1, 2, 3], 'b': [4, 5, 6]}, 'B': 'Bananas'}['A'])
# exp: {'a': [1, 2, 3], 'b': [4, 5, 6]} got: exp
print({'A' : {'a': [1, 2, 3], 'b': [4, 5, 6]}, 'B': 'Bananas'}['A']['b'])
# exp: [4, 5, 6] got: exp
print({key: [] for key in range(3)})
# exp: [] got: {0: [], 1: [], 2: []}
print({key: [] for key in zip(['a', 'b', 'c'], range(3))})
# exp: ['a', 'b', 'c']  got: {('a', 0): [], ('b', 1): [], ('c', 2): []}
print({key: [] for key in tuple(zip(['Name', 'Age'], [str, int]))})
# exp: ['Name', str, 'Age' ,int], [str, int] got: {('Name', <class 'str'>): [], ('Age', <class 'int'>): []}
print({key: val for key, val in zip(['ubi', 'ibi', 'puer'], ['where', 'there', 'boy'])})
# exp: got: {'ubi': 'where', 'ibi': 'there', 'puer': 'boy'}
print(list(enumerate(['John', 'Jane', 'Adam', 'Eva', 'Ashley'])))
# exp: got: [(0, 'John'), (1, 'Jane'), (2, 'Adam'), (3, 'Eva'), (4, 'Ashley')]
print({i: len(j) for i, j in enumerate(['cat', 'dog', 'okapi'])})
# exp: got: {0: 3, 1: 3, 2: 5}
