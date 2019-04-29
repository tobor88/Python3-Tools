# Reverse a sentence | Sentence a reverse

def reverse(a):
    b = a.split(" ")
    c = b[::-1]
    d = " ".join(c)
    return d

sentence = input("Write a sentence: ")

print(reverse(sentence))
