# String-2 > double_char
"""""
Given a string, return a string where for every char in the original, there are two chars.
"""""
def double_char(str):
  a =""
  for i in str:
    a += i * 2
  return a
  
  
# String-2 > count_hi
"""""
Return the number of times that the string "hi" appears anywhere in the given string.
"""""
def count_hi(str):
  count = 0
  for i in range (len(str)-1):
    if str[i:i+2] == "hi":
      count += 1
  return count
  
  
# String-2 > cat_dog
"""""
Return True if the string "cat" and "dog" appear the same number of times in the given string.
"""""
def cat_dog(str):
  if str.count("cat")  == str.count("dog"):
    return True
  else:
    return False


# String-2 > count_code
"""""
Return the number of times that the string "code" appears anywhere in the given string, except we'll 
accept any letter for the 'd', so "cope" and "cooe" count.
"""""
def count_code(str):
  count = 0
  while count <= len(str):
    for i in range(len(str)-3):
      if str[i:i+2] =="co" and str[i+3]== "e":
        count += 1
    return count
    
    
# String-2 > end_other
"""""
Given two strings, return True if either of the strings appears at the very end of the other string, 
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive"). 
Note: s.lower() returns the lowercase version of a string.
"""""
def end_other(a, b):
    a = a.lower()
    b = b.lower()
    return True if a.endswith(b) or b.endswith(a) else False


# String-2 > xyz_there
"""""
Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded 
by a period (.). So "xxyz" counts but "x.xyz" does not.
"""""
def xyz_there(str):
  a = str.count("xyz")
  b = str.count(".xyz")
  return True if a != b else False