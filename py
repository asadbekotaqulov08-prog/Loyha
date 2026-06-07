malumotlar = []

while True:
    print("\n1 - Qoshish")
    print("2 - Korish")
    print("3 - Chiqish")
    
    tanlov = input("Tanlang: ")
    
    if tanlov == "1":
        ism = input("Ism: ")
        yosh = input("Yosh: ")
        malumotlar.append({"ism": ism, "yosh": yosh})
        print("Qoshildi!")
    
    elif tanlov == "2":
        for i, m in enumerate(malumotlar):
            print(f"{i+1}. {m['ism']} - {m['yosh']}")
    
    elif tanlov == "3":
        break
