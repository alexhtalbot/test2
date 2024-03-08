palindrome_word = input("Please enter a word: ")
palindrome_word_list = list(palindrome_word)
palindrome_word_list_reversed = palindrome_word_list[::-1]

if palindrome_word_list == palindrome_word_list_reversed:
  print("This is a palindrome")

else:
  print("This is not a palindrome")