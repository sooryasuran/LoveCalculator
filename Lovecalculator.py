name1=input("Enter the first name: ")
name2=input("Enter the second name: ")
combname=name1+name2
lcombname=combname.lower()
a=lcombname.count("t")
b=lcombname.count("r")
c=lcombname.count("u")
d=lcombname.count("e")
true=a+b+c+d
e=lcombname.count("l")
f=lcombname.count("o")
g=lcombname.count("v")
h=lcombname.count("e")
love=e+f+g+h
score=str(true)+str(love)
scorenew=int(score)
print(scorenew)
if scorenew < 10 or scorenew >90:
  print("Your score is", scorenew,", you go togather like coke and mentos")
elif scorenew>40 and scorenew<50:
  print("Your score is", scorenew,", you are alright togather")
else:
  print("Your score is", scorenew)
