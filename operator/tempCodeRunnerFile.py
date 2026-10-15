# 3: Take the user age as input. Check and print whether they are eligible
# to vote (age >= 18) and whether they are a senior citizen (age >= 60).
# Print both results

age = int(input("Enter age "))

if age >=18 :
    print("  eligible to vote ")

elif age >=60:
    print("senior citizen ")

else:
    print("Minors")

