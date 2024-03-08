palindrome_word = input("Please enter a word to see if it's a palindrome: ")
palindrome_word_list = list(palindrome_word)
palindrome_word_list_reversed = palindrome_word_list[::-1]

if palindrome_word_list == palindrome_word_list_reversed:
  print("True: this is a palindrome")

else:
  print("False: this is not a palindrome, try again")