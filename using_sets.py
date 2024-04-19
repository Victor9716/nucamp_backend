numbers_set = {1,2,3,4,4.5}
# print(numbers_set)  # Output: set([1, 2, 3, 4, 5])

# # numbers_set = {1,2,3,4,[5,6]}
# # numbers_set = {1,2,3,4,(5,6)}
print(numbers_set)

words_set = {"Alpha", "Bravo", "Charlie"}

# abcd = ""
# for word in words_set:
#     abcd += word
# print(abcd)   # Output: AlphaBra

words_set.add("Delta")
print(words_set)    # Output: {'Alpha', 'Bravo', 'Charlie', 'Delta'}
words_set.discard("Alpha")
print(words_set)    # Output: