# # Goal: Write a function that takes a list of integers l and returns the sum of all even numbers. Constraint: If an even number appears multiple times, only add it to the sum once.
# # Example:
# # Input: [2, 2, 4, 1, 5, 4]
# # Logic:
# # Even numbers are: 2, 2, 4, 4
# # Distinct even numbers are: 2, 4
# # Sum: 2 + 4 = 6
# # Output: 6

# def listnum(l):
#     seen = []
#     eSum = 0
#     for num in l :
#         if num not in seen :
#             seen.append(num)
#             if num % 2 == 0 :
#                 eSum += num
#     return eSum

#     # s = set(l) #{1,2,4,5}
#     # eSum = 0
#     # for num in s :
#     #     if num % 2 == 0:
#     #         eSum += num
#     # return eSum
    
# print(listnum([2, 2, 4, 1, 5, 4]))


# def triangle_swap(t: tuple) -> tuple:
#     # Your code here
#     l = len(t)
#     mid = l//2
#     firstt = (t[0],)
#     midt = (t[mid],)
#     endt = (t[-1],)
#     return midt + t[1:mid] + endt + t[mid+1:-1] + firstt
# print(triangle_swap((1, 2, 3, 4, 5))) #(3, 2, 5, 4, 1)

# def center_switch(t: tuple, val: int) -> tuple:
#     # Your code here 
#     l = len(t)
#     mid = l//2
#     if l%2 == 0:
#         return t[:mid] + (val,) + t[mid:]
#     else :
#         return t[:mid] + (val,) + t[mid+1:]
# print(center_switch((1, 2, 3),99))

# "apple banana orange", order = (0, 2, 1) -> "apple orange banana"

# def reorder(s,t):
#     lst = []
#     words = s.split()
#     for idx in t :
#         lst.append(words[idx])
#     return " ".join(lst)
# print(reorder("apple banana orange",(0, 2, 1)))

# n = int(input())
# res = []
# for i in range(n):
#     fullname = input()
#     name = fullname.lower().split()
#     # Albus Percival Wulfric Brian Dumbledore
#     lstName = name[-1]
#     othName = name[:-1]
#     initials = ""
#     for j in othName:
#         letters = othName[0]
#         initials = initials + letters + "."

#     res.append(finall)
# res.sort()
# print(res)

# Description Write a function remove_middle(s) that removes the "middle" of the string.
# If the string length is Odd, remove the 1 middle character.
# If the string length is Even, remove the 2 middle characters.
# Assumptions

# def removemiddle(s):
#     n = len(s)
#     m = n//2
#     if n % 2 == 0: #[a,b,c,d]
#         return s[:m-1]+s[m+1:] #[a,d]
#     else : #[a,b,c,d,e]
#         return s[:m]+s[m+1:]
# print(removemiddle("code")) 

# Practice Question: The Word Length Grouper

# Description Write a Python program that reads a single line of text containing words separated by spaces. Your task is to group these words based on their length (number of characters).
# Requirements:
# Grouping: Create a dictionary where the Key is the length of the word, and the Value is a list of words that have that length.
# Case Insensitivity: Convert all words to lowercase before grouping.
# Sorting:
# Print the lengths (Keys) in ascending order (smallest length first).
# Sort the words inside each list (Values) alphabetically.
# Formatting: Print the output as Length : word1, word2, ...
# Input Format A single line of text with words separated by spaces.
# Output Format Lines showing the length and the sorted words associated with that length.
# Example
# Input:
# Apple bat Cat ant Dog banana
# Output:
# 3 : ant, bat, cat, dog
# 5 : apple
# 6 : banana

#key -->lenght  values -->list of len

# lst = input()
# words = lst.split(" ")
# resdict = {}
# for word in words :
#     l = len(word) #key
#     if l not in resdict :
#         resdict[l] = []
#     resdict[l].append(word)
# for r in sorted(resdict.keys()):
#     w = resdict[r]
#     w.sort()
#     wr = ",".join(w)
#     print(f"{r} : {wr}")




# Question: Check for All Vowels
# Write a function has_all_vowels(text) that takes a string text as input and returns True if the string contains all the vowels (a, e, i, o, u), and False otherwise.
# The check should be case-insensitive (e.g., 'A' counts as 'a').

# def checkvowels(text):
#     vowels = "aeiou"
#     #text = "sumith kumar is a bad boy"
#     lowertext = text.lower()
#     for vols in vowels:
#         if vols not in lowertext:
#             return False
#     return True

def courses_sorted_by_enrollment(student_courses: dict) -> list:
    sub_count = {}
    for lst in student_courses.values():
        for i in lst:
            if i in sub_count :
                sub_count[i] += 1
            else :
                sub_count[i] = 1
    sub_countlst = sub_count.items()
    sorted_count = sorted(sub_countlst,key= lambda x:x[1],reverse=True)
    res = []
    for i in sorted_count:
        res.append(i[0])
    return res





'''
    Given a dictionary of student roll numbers 
    with the list of courses they chose, 
    find the courses sorted from the 
    most number of enrollments to the least.

    Assume no courses will have the same number of students enrolled.

    Args:
    student_courses (dict): 
        a dictionary where keys are student roll numbers and 
        values are lists of courses they chose

    Returns:
    list: 
        a list of courses sorted by the number of students enrolled 
        in descending order
        
    1. Make a course count dictionary - 
    {course1 : no. of enrollments, course2 : no. of enrollments}
    
    2. Iterate over each value in the student_courses dictionary.
    3. For each value(['Math', 'Science']), 
        i. Iterate over all the subjects,
        ii. For each subject, check if the subject is present in the CCD.
        iii. If yes, increase the count,
        iv. If no, Add the subject in the CCD.
'''

# Input:

# 2
# one,two,order,real,long,tight,tree,cool,lot,trouble
# ant,tree,ear,rat,tower,retail
# Output:

# 4
# 6

def antaskshari(words):
    n = int(input())
    currentlen = 1
    maxlen = 1
    for i in range(n):
        song = input().split(",")
        count = 0
        for j in range(len(song)-1):
            current = song[j]
            next = song[j+1]
        
