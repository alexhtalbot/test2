def vowel_counter(my_variable):
  counter = 0
  vowels = "aeiou"
  for character in my_variable:
      if character.lower() in vowels:
          counter += 1
  return counter