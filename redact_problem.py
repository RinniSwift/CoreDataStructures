import unittest

from set import Set

def redact_words(words, banned_words):
	banned_words_set = Set(banned_words)

	result = []
	for word in words:
		if banned_words_set.contains(word) is False:
			result.append(word)

	return result

if __name__ == '__main__':
    print(redact_words(["hello", "my", "name", "is", "not", "Rinni"], ["not"]))



class test_redact_problem(unittest.TestCase):

	def test_words(self):
		assert redact_words(["hello", "my", "name", "is", "not", "Rinni"], ["not"]) == ["hello", "my", "name", "is", "Rinni"]
		assert redact_words(["The", "sky", "is", "beautiful", "but", "dark"], ["dark", "but", "not"]) == ["The", "sky", "is", "beautiful"]
		assert redact_words(["I", "like", "22", "but", "not", "33", "or", "43"], ["not", "33", "43"]) == ["I", "like", "22", "but", "or"]
