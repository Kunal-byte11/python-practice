# : A student scored marks in 3 subjects. Take all three as input,
# calculate the total and average, and print both using an f-string

sub1 = int(input("subject 1 "))
sub2 = int(input("subject 2 "))
sub3 = int(input("subject 3 "))

total = sub1 + sub2 + sub3 

avg = sub1 + sub2 + sub3 / 3 

print(f"the total marks obtain {total} , and averge is {avg}")