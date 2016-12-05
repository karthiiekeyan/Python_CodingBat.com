# String-1 > hello_name
# Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".

def hello_name(name):
  name = "Hello" " " + name + "!"  
  return name


# String-1 > make_abba
# Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and 
# "Bye" returns "HiByeByeHi".

def make_abba(a, b):
  a = str (a)
  b = str(b)
  return a + b + b + a
    

# String-1 > make_tags
# The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the 
# "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML 
# string with tags around the word, e.g. "<i>Yay</i>".

def make_tags(tag, word):
  tag = str(tag)
  a = "<"
  b = ">"
  word = str(word)
  c = "</"
  d = ">"
  return a + tag + b + word + c + tag + d

# String-1 > make_out_word
# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the 
# middle of the out string, e.g. "<<word>>". 

def make_out_word(out, word):
  out = out[:2] + word + out[2:]
  return out
  

# String-1 > extra_end
# Given a string, return a new string made of 3 copies of the last 2 chars of the original string. The string
# length will be at least 2.

def extra_end(str):
  return 3 *  str[-2:]
  
  
# String-1 > first_two
# Given a string, return the string made of its first two chars, so the String "Hello" yields "He". If the string 
# is shorter than length 2, return whatever there is, so "X" yields "X", and the 
# empty string "" yields the empty string "".   
  
def first_two(str):
  if str < 2:
    return x
  else:
    a = str[0:2]
    return a


# String-1 > first_half
# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

def first_half(str):
  a = str[0:len(str) / 2]
  return a


# String-1 > without_end  
# Given a string, return a version without the first and last char, so "Hello" yields "ell". The string length will
# be at least 2.

def without_end(str):
  a = str[1:-1]
  return a


# String-1 > combo_string
# Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the 
# outside and the longer string on the inside. The strings will not be the same length, but they may be
# empty (length 0). 

def combo_string(a, b):
  if len(a) > len(b):
    return b + a + b
  if len(b) > len(a):
    return a + b + a
    
    
# String-1 > non_start 
# Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at
# least length 1.
    
def non_start(a, b):
  a = str(a)[1:]
  b = str(b)[1:]
  return a + b


# String-1 > left2
# Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end. The string
# length will be at least 2.

def left2(str):
  a = str[2:] + str [0:2]
  return a
