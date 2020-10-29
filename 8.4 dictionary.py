# Dictionary can hold item with key value pair and value can be accessed through key
monthConversion = {
    "jan" : "January",
    "feb" : "February",
    "mar" : "March",
    "apr" : "April",
    "may" : "May",
    "jun" : "June",
    "jul" : "July",
    "aug" : "August",
    "sep" : "September",
    "oct" : "October",
    "nov" : "November",
    "dec" : "December"
}

print(monthConversion["oct"])
print(monthConversion.get("boishakh","Not found"))