numbers = {
    5993: {"name": "Abhiram R", "mn": "'9538753850'", "fn": "'9845091985'"},
    5991: {"name": "Ved K C", "mn": "'8380077822'", "fn": "'9158033277'"},
    6002: {"name": "Nishant M Y", "mn": "'8217304727'", "fn": "'9844072801'"},
    5989: {"name": "Abhinav P K", "mn": "'9740688755'", "fn": "'9880488455'"},
    5976: {"name": "Chaitanya B A", "mn": "'6362421023'", "fn": "'8686751986'"},
    6036: {"name": "Ningaraj", "mn": "'9845874584'", "fn": "'9901402366'"},
    5969: {"name": "Prajwal K", "mn": "'6360296078'", "fn": "'7829528767'"},

}

def entcod():
    no = input("Please enter your roll no. - ")
    try:
        no = int(no)
    except ValueError:
        print("Invalid input! Please enter a numeric roll number.")
        return entcod()

    if no in numbers:
        print(f"Hello, {numbers[no]['name']}!")
        call(no)
    else:
        print("Please enter a valid code!")
        return entcod()

def call(no):
    c = input("Dial 1 (Mom) or 2 (Dad): ")
    if c == "1":
        print(f"Dialling {numbers[no]['mn']} - 📞")
    elif c == "2":
        print(f"Dialling {numbers[no]['fn']} - 📞")
    else:
        print("Please enter a valid input!")
        return call(no)

print("Hello user!")    
entcod()
