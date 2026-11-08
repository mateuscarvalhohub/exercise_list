"""
Exercise 01

Goal:
Analyze a sentence and identify words that appear
more than once.

Concepts Practiced:
- Input handling
- String manipulation
- Dictionaries
- Lists
- Loops
- Conditional statements
- Word frequency analysis

Tests:
✓ Repeated word ("hello hello world" → ['hello']: 2)
✓ Multiple repeated words ("python is great and python is fun" → ['python']: 2, ['is']: 2)
✓ No repeated words ("python is awesome" → No output)
✓ Punctuation handling ("hello, hello. world" → ['hello']: 2)
✓ Mixed case input ("Python python" → ['python']: 2)
✓ Empty input ("" → No output)
"""

sentence = input("Please, enter any sentence: ").lower().replace(",", "").replace(".", "")

word_count ={}

for word in sentence.split():
	word_count[word] = word_count.get(word, 0) + 1
repeated_words = []

for word, count in word_count.items():
	if count > 1:
		repeated_words.append(word)
		
		print(f"{repeated_words}: {count}")