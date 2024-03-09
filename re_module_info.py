# https://chat.openai.com/c/bd24a255-f774-4068-b6cb-f5d1c891bc73
# https://chat.openai.com/c/fde69d5f-2576-4b63-a071-0bb822c20306

# import re
# txt = "abc"
# if re.fullmatch("[a-z]+", txt):
#     print("fullmatch")
# else:
#     print("not fullmatch")
#
# import re
# txt = "abc"
# if re.match("^[a-z]+$", txt):
#     print("fullmatch")
# else:
#     print("not fullmatch")
#
# import re
# txt = "abc"
# if re.fullmatch("[a-z]+", txt):
#     print("fullmatch")
# else:
#     print("not fullmatch")
#
# import re
# txt = "abc"
# if re.fullmatch("^[a-z]+$", txt):
#     print("fullmatch")
# else:
#     print("not fullmatch")

# import re
# email = "someemail123@email.com"
# pattern = '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# if re.fullmatch(pattern, email):
#     print("it is email")
# else:
#     print("definetly not email")

# import re
#
# if re.fullmatch("[a-z]* [a-z]*", "somete xt"):
#     print(True)
# else:
#     print(False)

# import re
#
# if re.fullmatch("^[0-9][a-z]+", "1sometext"):
#     print(True)
# else:
#     print(False)

### REGULAR EXPRESSIONS || REGEX ###
# https://www.w3resource.com/python-exercises/re/
# match - перевіряє початок рядка на співпадіння з паттерном    (після патерна може бути будь-що)
# fullmatch - перевіряє рядок на повне співпадіння з патерном   (повне спіпадіння з паттерном)
# search - просто шукає в рядку будь-де співпадіння
# [] - дужки для формули
# -  - діапазон     [a-z]
# +  - повтор елемента, або формули 1 або більше разів
# *  - повтор елемента, або формули 0 або більше разів
# ?  - повтор елемента, або формули 0 або 1 раз
# .  - будь який елемент
# \  - показує що наступний елемент - це просто текст
# |  - вибір із декількох (логічне або) (a|bb|c) - шукає a або bb або c
# {} - використовується для указування кількості повторів елементу або формули
# $  - позначає кінець рядка

# import re
# txt = "abc"
# if re.fullmatch("[a-z]+", txt):
#     print("matched")
# else:
#     print("not matched")

# import re
# txt = "somemail@"
# if re.fullmatch("[a-z]+@", txt):
#     print("matched")
# else:
#     print("not matched")


# 1. Write a Python program to check that a string contains only a certain set of characters
# (in this case a-z, A-Z and 0-9).
# import re
# def check(string):
#     if re.fullmatch("[a-zA-Z0-9]+", string):
#         return True
#     else:
#         return False
# print(check("1"))

# # 2. Write a Python program that matches a string that has an a
# # followed by zero or more b's.
# import re
#
# test_strings = ["a", "ab", "abb.", "cabbb", "ac", "abc", "b"]
# # Iterate over test strings and check for matches
# for test_string in test_strings:
#     if re.search("ab*", test_string):
#         print(f"'{test_string}' matches the pattern.")
#     else:
#         print(f"'{test_string}' does not match the pattern.")

# # 3. Write a Python program that searches a string for pattern that has an a followed by one or more b's.
# # Click me to see the solution
# import re
# pattern = "ab*"
# test_strings = ["a", "ab", "abb.", "cabbb", "ac", "abc", "b", '.']
# # Iterate over test strings and check for matches
# for test_string in test_strings:
#     if re.search(pattern, test_string):
#         print(f"'{test_string}' matches the pattern.")
#     else:
#         print(f"'{test_string}' does not match the pattern.")


# # 4. Write a Python program that matches a string that has an a followed by zero or one 'b'.
# import re
# pattern = "ab{0,1}"
# test_strings = ["a", "ab", "abb", "cabbb", "ac", "abc", "b", '.']
# # Iterate over test strings and check for matches
# for test_string in test_strings:
#     if re.search(pattern, test_string):
#         print(f"'{test_string}' matches the pattern.")
#     else:
#         print(f"'{test_string}' does not match the pattern.")

# # 5. Write a Python program that matches a string that has an a followed by three 'b'.
# import re
# pattern = "ab{3}"
# test_strings = ["a", "ab", "abb", "cabbb", "ac", "abc", "b", '.']
# # Iterate over test strings and check for matches
# for test_string in test_strings:
#     if re.search(pattern, test_string):
#         print(f"'{test_string}' matches the pattern.")
#     else:
#         print(f"'{test_string}' does not match the pattern.")

# 6. Write a Python program that matches a string that has an a followed by two to three 'b'.
# дз

# # 7. Write a Python program to find sequences of lowercase letters joined by an underscore.
# import re
# pattern = "[a-z]+_"  # [a-z]{1,99999}
# test_strings = ["a_b", "ab", "abb", "cabbb_", "ac__", "Abc_", "b", '.']
# # Iterate over test strings and check for matches
# for test_string in test_strings:
#     if re.search(pattern, test_string):
#         print(f"'{test_string}' matches the pattern.")
#     else:
#         print(f"'{test_string}' does not match the pattern.")

# 8. Write a Python program to find the sequences of one upper case letter followed by one or more lower case letters.
# дз

# # 9. Write a Python program that matches a string that has an 'a' followed by anything ending in 'b'.
# import re
# pattern = "a.*b$"
# test_strings = ["a_b", "ab", "abb", "cabbb_", "ac__", "Abc_", "b", '.']
# # Iterate over test strings and check for matches
# for test_string in test_strings:
#     if re.search(pattern, test_string):
#         print(f"'{test_string}' matches the pattern.")
#     else:
#         print(f"'{test_string}' does not match the pattern.")

# 10. Write a Python program that matches a word at the beginning of a string.
# дз

# 11. Write a Python program that matches a word at the end of a string, with optional punctuation.
# дз

# # 1. Matching digits
# # Write a regular expression to match any sequence of digits in a string.
# import re
# txt = "some_row_with123"
# print(re.search(r"\d+", txt).group())

# # 2. Matching Email Addresses
# # Write a regular expression to match email addresses in a string. Consider the basic format of an email address: username@example.com.
# import re
# emails = ["username@example.com", "username123@example.com", "user.name@example.com", "user.name123@example.com",
#           "username@example.", "username@.com", "username@examplecom", "user_name444@gmail.com",]
#
# for email in emails:
#     if re.fullmatch(r"\w+[\w.!#$%&'*+/=?^_`{|}~-]*@\w+\.\w+", email):
#         print(f"{email} is match")

# # 3. Phone number
# # Write a regular expression to match phone numbers in a string. Consider standard formats such as (123) 456-7890 or 123-456-7890.
# import re
# numbers = ["(123) 456-7890", "(12) 456-7890", "(123) -7890", "123-456-7890", "12-456-7890", "123-46-7890", "123_456_7890",
#            " ", "", "*"]
# for num in numbers:
#     if re.fullmatch(r"\(?\d{3}\)? ?-?\d{3}-\d{4}", num):
#         print(num, "matches")
#     else:
#         print(num, "does not match")


# # 4. Matching Dates:
# # Write a regular expression to match dates in the format YYYY-MM-DD (e.g., 2024-02-06).
# import re
# dates = ["2000-01-01", "0000-00-00", "0000-01-01", "2000-00-00", "20000000", "2000 00 00", "2000.00.00", "2024-02-06",
#            " ", "", "*"]
# for date in dates:
#     if re.fullmatch(r"[1-9][0-9]{3}-(0[1-9]|[10-12])-(0[1-9]|[1-2][0-9]|3[01])", date):
#         print(date, "matches")
#     else:
#         print(date, "does not match")

# # match any year 1-99999
# import re
# dates = ["0", "1", "10", "100", "100", "10000", "01", "001"]
# for date in dates:
#     if re.fullmatch(r"([0-9]|[1-9][0-9]{1,5})", date):
#         print(date, "matches")
#     else:
#         print(date, "does not match")

# # 5. Matching Words Starting with a Specific Prefix:
# # Write a regular expression to match words in a string that start with a specific prefix, such as "pre-".
# import re
#
# prefix = input("Type in the prefix the word should start with: ")  # checking for pre-
# words = ["preword", "pre", "pre1", "pre", "pre.", "word", "wpred", "p.re", "preword prewordd"]
# pattern = rf"\b{prefix}\w+"
#
# for word in words:
#     matches = list(re.finditer(pattern, word))
#     if matches:
#         print(f"word: {word}. Found match.")
#         for match in matches:
#             print(f"  Match: {match.group()}")
#     else:
#         print(f"word: {word}. No match.")

# # Substitution (optional)
# # The re.sub(pat, replacement, str) function searches for all the instances of pattern in the given string, and replaces them.
# # The replacement string can include '\1', '\2' which refer to the text from group(1), group(2), and so on from the original matching text.
# import re
# str = 'purple alice@google.com, blah monkey bob@abc.com blah dishwasher'
# ## re.sub(pat, replacement, str) -- returns new string with all replacements,
# ## \1 is group(1), \2 group(2) in the replacement
# print(re.sub(r'([\w.-]+)@([\w.-]+)', r'\1@yo-yo-dyne.com', str))
# ## purple alice@yo-yo-dyne.com, blah monkey bob@yo-yo-dyne.com blah dishwasher

# get it on yield, iter, tasks
### YIELD ###
# Allow to generate a sequence of values while working with it, rather than all at once.
# Inside a function it works like return without terminating the function.
# Instead, it saves the state of function, so the next time it is called, it returns the next element.

# def back_counting(n):
#     if n > 0:
#         yield n
#         n -= 1
#         print("it reaches it!", n)
#
# for i in back_counting(5):
#     print(i)

# # Range Generator: Implement a generator function that mimics the behavior of Python's built-in range() function.
# def custom_range(start, stop=None, step=1):
#     if stop is None:
#         stop = start
#         start = 0
#     while (step > 0 and start < stop) or (step < 0 and start > stop):
#         yield start
#         start += step
#
# # Test the custom_range generator
# for i in custom_range(1, 10, 2):
#     print(i)
#
# print("")
#
# for i in custom_range(10, 1, -2):
#     print(i)
#
# print("")
#
# for i in custom_range(10):
#     print(i)

# # Squared Numbers Generator: Create a generator function that yields the squares of numbers from 1 to n.
# def squares(n):
#     start = 1
#     while start <= n:
#         yield start ** 2
#         start += 1
# for elem in squares(-10):
#     print(elem)
# print()
# for elem in squares(10):
#     print(elem)

# get it on iter, tasks
# get it on wrappers and functools.wraps, tasks
# difference with decorators, tasks
# https://roadmap.sh/python


