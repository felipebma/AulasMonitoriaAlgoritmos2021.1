def hash(x, n):
    return (x*x) % n


def insert(hash_table, x):
    pos = hash(x, len(hash_table))
    for i in hash_table[pos]:
        if i == x:
            return False
    hash_table[pos].append(x)
    return True


def search(hash_table, x):
    pos = hash(x, len(hash_table))
    for i in hash_table[pos]:
        if i == x:
            return True
    return False


def remove(hash_table, x):
    pos = hash(x, len(hash_table))
    for i in range(len(hash_table[pos])):
        if hash_table[pos][i] == x:
            hash_table[pos].pop(i)
            return True
    return False


def resize(hash_table, new_size):
    new_table = []
    for _ in range(new_size):
        new_table.append([])
    for lista in hash_table:
        for elemento in lista:
            insert(new_table, elemento)
    return new_table


hash_table = []
n = 10
for _ in range(n):
    hash_table.append([])
print(hash_table)
insert(hash_table, 3)
print(hash_table)
insert(hash_table, 3)
print(hash_table)
insert(hash_table, 7)
print(hash_table)
insert(hash_table, 4)
print(hash_table)
print(search(hash_table, 4))
print(remove(hash_table, 4))
print(search(hash_table, 4))
print(remove(hash_table, 4))
print(hash_table)
print(search(hash_table, 3))
print(search(hash_table, 7))
hash_table = resize(hash_table, 30)
print(hash_table)
print(search(hash_table, 3))
print(search(hash_table, 7))
