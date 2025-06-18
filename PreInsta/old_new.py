def old_new(s,old,new):
    return s.replace(old, new)
text= "hello python"
new_text=old_new(text, "hello" , "hi")
print("replaces old text with new text" , new_text)



# dynamic input
def old_new(s, old, new):
    return s.replace(old, new)  


text = input("Enter your original text: ")
old = input("Enter the word to replace: ")
new = input("Enter the new word: ")

new_text = old_new(text, old, new)
print("Replaced text:", new_text)