class FlatIterator:
    def __init__(self, collection):
        self.collection = sum(collection, [])

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.collection):
            raise StopIteration
        element = self.collection[self.cursor]         
        return element

def flat_generator(collection):
    for el in sum(collection, []):
        yield el


nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	['g', 'h', 'i'],
]

# Задача 1
for item in FlatIterator(nested_list):
	print(item)

print('-'*70)

# Задача 2
for item in  flat_generator(nested_list):
	print(item)