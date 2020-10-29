is_male = False
is_tall = True

# if one of the value is true then or operator will produce true
if is_male or is_tall:
    print("You are a male or the tall one or both")
else:
    print("You neither male nor tall")

# if both of them is true then and will produce true
if is_male and is_tall:
    print("you're a complere package")
else:
    print("Everyone is not a movie hero")

# elif is similer to else if.

if is_male and is_tall:
    print("You're a wonderfull creation of almighty god.")
elif is_male and not is_tall:
    print("Being short has lot of advantage, like be same as always")
elif not is_male and is_tall:
    print("You beauty and proud!")
else:
    print("Being in this world matter, not any feature special")