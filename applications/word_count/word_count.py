import re

def word_count(s):
    # Your code here
    dict = {}

    lower = s.lower()
    words = lower.split()

    for n in words:
        n = re.sub(r'[^\w\']', '', n)
        if n in dict:
            dict[n] += 1
        elif n != '':
            dict[n] = 1
        
    return dict

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))