# 3: Take the user age as input. Check and print whether they are eligible
# to vote (age >= 18) and whether they are a senior citizen (age >= 60).
# Print both results

age = int(input("Enter age "))

if age >=18:
    print("Eligible to vote")

else:
    print("Not eligible to vote ")
    
if age >=60 :
    print("  senior citizen ")
else:
    print("Not a senior citizen")
