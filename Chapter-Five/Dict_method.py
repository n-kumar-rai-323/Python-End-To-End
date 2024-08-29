# Dictionary Method
marks = {
    "Nishan" : 100,
    "Kali" : 45,
    "Gita" : 89
}

print(marks.items())

print(marks.keys())

print(marks.values())

marks.update({"Gita": 100})
print(marks)

print(marks.get("Nikita")) # if you have no data GET method return Non 
# print(marks['Misson'])  # if you have no data retrun error 