"""
# List Functions
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(list1 + list2, '\n',
      list1 * 3, "\n",
      list1 == list2, "\n",
      5 in list1, "\n",
      len(list1), "\n",
      sum(list1), "\n",
      any(list1), "\n",
      sorted(list1), "\n",
      list1.sort(), "\n",
      reversed(list1), "\n",
      list1.reverse(), "\n", )

# if-else
score = float(input("Enter your score between 0 and 1 here = "))
if score > 1 or score < 0:
    print("Incorrect Output")
elif score >= 0.9:
    print('Your Grade is "A"')
elif score >= 0.8:
    print('Your Grade is "B')
elif score >= 0.7:
    print('Your Grade is "C"')
elif score >= 0.6:
    print('Your Grade is "D"')
else:
    print('Your Grade is "F"')

# string traversal
new_str = input("Enter String - ")
if new_str == new_str[::-1]:
    print("Entered String is Palindrome")
else:
    print("Entered String is not Palindrome")

# Leap Year
year = int(input("Enter year - "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print(str(year) + "is a leap year")
else:
    print(str(year) + "is a leap year")

for each_character in "USAR Delhi":
    print(f'Traversing characters - {each_character}')
"""
nterms=int(input("How much Fibonacci Numbers you want ? - "))
list=[]
n1,n2=0,1
count=0
if nterms<0:
    print("Enter a +ve integer")

