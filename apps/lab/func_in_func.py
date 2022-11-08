
my_bands = [
    ("Spanish", 2, ["El Cuarteto de Nos", "La Vela Puerca"]),
    ("English", 2, ["Queen", "Imagine Dragons"]),
    ("German", 1, ["Rammstein"])
]

bands_with_s = []

for i in  my_bands:
    for j in i[2]:
        if 's' in j and i[1] > 1: # Conditionals
            bands_with_s.append(j) # What i keep

bands_with_s_comprenhension = [
    j # What i keep
    for i in my_bands
    for j in i[2]
    if 's' in j and i[1] > 1 # Conditionals
]

if __name__ == '__main__':
    print(bands_with_s)
    print(bands_with_s_comprenhension)

# Output
# ['El Cuarteto de Nos', 'Imagine Dragons']
# ['El Cuarteto de Nos', 'Imagine Dragons']
