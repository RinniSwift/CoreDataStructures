
'''visual syntax of how to create different permuations. lock the first item in the list and do that for the next item that comes after until we hit the last loop'''

def all_permutations(word):
	# length of list must be 4 (3 inner loops within the large loop)
	for i in word:
		split_word = []
		split_word.extend(word)
		split_word.remove(i)	
		for n in split_word:
			new_split_word = []
			new_split_word.extend(split_word)	# to create a new copy of the original list
			new_split_word.remove(n)
			for z in new_split_word:
				new_new_split_word = []
				new_new_split_word.extend(new_split_word)
				new_new_split_word.remove(z)
				for j in new_new_split_word:
					print(i , n , z, j)



def all_permutations_recursive(lst):
	# only one possible result 
	if len(lst) < 2:
		return lst
	# only two possible results
	if len(lst) == 2:	
		return [lst, [lst[1], lst[0]]]


	all_permutations = []
	for i in lst:
		new_lst = []
		new_lst.extend(lst)
		new_lst.remove(i)

		extensions = all_permutations_recursive(new_lst)
		for extension in extensions:
			extension.insert(0, i)
		all_permutations.extend(extensions)

	return all_permutations

def number_of_permutations(arr):
	return factorial(len(arr))

def factorial(number):
	res = 1
	for i in range(1, number + 1):
		res *= i
	return res


word = [1,2,3, 4]
# print(all_permutations(word))
print(number_of_permutations(["R", "I", "N", "I"]))
print(all_permutations_recursive(["H", "E", "L", "P"]))