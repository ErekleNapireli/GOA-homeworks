# 1) მიმოიხედეთ ოთახში, აირჩიეთ რაიმე ობიექტი და შექმენით მისი dictionary (მინიმუმ 5 key:value pair უნდა ჰქონდეს)
laptop ={
    "name": "Lenovo",
    "model": "LOQ",
    "processor": "Intel",
    "lights": True,
    "graphics_card": "RTX",
}

# 2) for loop'ის მეშვეობით გამოიტანეთ ამ dictionary'ს key'ები
for key in laptop.keys():
    print(key)
# 3) for loop'ის მეშვეობით გამოიტანეთ ამ dictionary'ს value'ები
for value in laptop.values():
    print(value)
# 4) for loop'ის მეშვეობით გამოიტანეთ ამ dictionary'ს key'ები და value'ები ერთად
for key,value in laptop.items():
    print(key,value)