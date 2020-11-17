import synthetic
from hash import HashTable, LinkedList

words = synthetic.words('training_data.txt', 100, 1)
print(words)

hash_table = HashTable(10)
hash_table.add_all(words)

hash_table.delete_first("o")
hash_table.delete_all("o")

print(hash_table.array)



