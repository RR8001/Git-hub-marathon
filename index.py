name = input("enter your name")
print("Are you a boy or a girl?")
gender = input("enter your gender,male or female\n888888888").lower() #.lower() helps to convert input given
# by users in lowercase
if gender == "male":
    print(f"Hello Mr.{name} :)")
elif gender == "female":
    print(f"Hello Ms.{name}")
else:
    print("enter valid answer")
print("thanks for visting our website") 
