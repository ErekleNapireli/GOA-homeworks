#  3) დაწერეთ მეორე დავალება პითონის კოდითაც და შემდეგ შეადარეთ js'ით დაწერილ კოდს, ამოწერეთ სინტაქსური განსხვავებები
# // 2) მომხმარებელს შემოატანინეთ საკუთარი ასაკი, თუ იქნება 13 წელზე ნაკლების გამოუტანეთ You are kid, თუ იქნება 18 წელზე ნაკლების მაგრამ 13'ზე მეტის გამოუტანეთ You are not adult yet და თუ იქნება 18 წელზე მეტის გამოუტანეთ You are adult

age = int(input("Enter your age: "))

if age < 13:
    print("You are a kid")
elif age < 18:
    print("You are not an adult yet")
else:
    print("You are an adult")
