#program that takes a user input (string) and outputs every second letter in reverse order.

#Please enter a sentence: The quick brown fox jumps over the lazy dog.
#expected results:.o zletrv pu o wr cu h

s = input("Please enter a sentence:")
s_reverse = s[::-1]
s_rev_jump = s_reverse[::2]
print(s_rev_jump)


