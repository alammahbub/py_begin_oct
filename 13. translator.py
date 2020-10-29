def translate(pharase):
    translation = ""
    for letter in pharase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += letter
    return translation

print(translate("Aahbub"))
