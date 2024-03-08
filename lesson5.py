palindrome_input = input("Let's check if your word or phrase is a palindrome, please enter your word or phrase: ")
characters_without_spaces = list(palindrome_input.replace(" ", ""))
characters_without_spaces_reversed = characters_without_spaces[::-1]
if characters_without_spaces == characters_without_spaces_reversed:
  print("True: this is a palindrome")
else: 
  print("False: this is not a palindrome")