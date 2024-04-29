import tkinter as tk

root = tk.Tk()

label = tk.Label(root, text="Alex's palindrome checker app")
label.pack()


def check_palindrome():
  entry_text = entry.get()
  palindrome_word_list = list(entry_text.lower())
  palindrome_word_list_reversed = palindrome_word_list[::-1]

  if palindrome_word_list == palindrome_word_list_reversed:
    result_label.config(text="Hooray: this is a palindrome", fg="blue")
  else:
    result_label.config(
        text="Uh oh: this is not a palindrome, please try again", fg="red")


entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Check", command=check_palindrome)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
