year_age=int(input("enter your Age/year of birth"))
isYear=False
birth_yr=False

if len(str(year_age))==4:
    isYear=True

else:
    birth_yr=True

    
if year_age>2023:
    print("You are not born yet")
    exit()

if year_age<=1900 and isYear:
    print("you seem to be the oldest person alive of age:-",2023-year_age)
    exit()

if 1900<year_age<=2023 and isYear:
    a=2023-year_age
    print(f"you are {a} years old")

elif birth_yr:
    year_age=2023-year_age
    print(f"you were born in {year_age}")
else:
    print("please enter valid age")
    exit()

print(f"you will be of 100 years old in {year_age+100}\n")
interested_yr=int(input("enter year u want to know your age in:-"))
print(f"you will be of \"{interested_yr-year_age}\" years old in \"{interested_yr}\"")
