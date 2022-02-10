def Cholesterol():
    cholesterol = float(input("\nEnter cholesterol (in mg/dl): "))
    if cholesterol < 200:
        print("\nCongratulations! your cholesterol is in safe range. Be Healthy, Be Safe!\n")
    elif cholesterol >= 200:
        print("\nYour cholesterol is out of safe range\n")
        print("""What to Eat: Whole grain breads, pulses (such as chickpeas,lentils,split peas), beans(kidney beans ,
             baked beans),healthy oils(canola , sunflower , olive , sesame) , Eggs""")
        print("What to Avoid: Full-fat dairy products(such as milk,curd), Read meat, Fried/Oily items, sweet items\n")


def LDL():
    ldl = float(input("\nEnter LDL Cholesterol (in mg/dl): "))
    if ldl < 100:
        print("\nCongratulations! your LDL cholesterol is in safe range. Be Healthy, Be Safe!\n")
    elif ldl>=100:
        print("\nYour LDL cholesterol is out of safe range\n")
        print("""What to Eat: Oats , Barley and whole grain products, beans , Eggplant ,   nuts , Apples , grapes , 
             strawberries , citrus fruits , soy , fatty fishes.""")
        print("What to Avoid: Full-fat dairy products(such as milk,curd), Read meat, Fried/Oily items, sweet items\n")

def VLDL():
    vldl = float(input("\nEnter VLDL Cholesterol (in mg/dl): "))
    if vldl < 30:
        print("\nCongratulations! your VLDL cholesterol is in safe range. Be Healthy, Be Safe!\n")
    elif vldl >= 30:
        print("\nYour VLDL cholesterol is out of safe range\n")
        print("What to Eat: Whole grain items , low fat dairy products , Eggs , fish , nuts.")
        print("What to Avoid: Full-fat dairy products(such as milk,curd), Read meat, Fried/Oily items, sweet items\n")

def HDL():
    hdl = float(input("\nEnter HDL Cholesterol (in mg/dl): "))
    if hdl > 50:
        print("\nCongratulations! your HDL cholesterol is in safe range. Be Healthy, Be Safe!\n")
    elif 0 <= hdl <= 50:
        print("\nYour HDL cholesterol is out of safe range\n")
        print("What to Eat: citrus fruits , Chia seeds , Avocado , Coconut oil/water.")
        print("What to Avoid: Full-fat dairy products(such as milk,curd), Read meat, Fried/Oily items, sweet items\n")

def NonHDL():
    nhdl = float(input("\nEnter Non-HDL Cholesterol(in mg/dl): "))
    if nhdl > 130:
        print("\nCongratulations! your Non-HDL cholesterol is in safe range. Be Healthy, Be Safe!\n")
    elif nhdl <= 130:
        print("\nYour Non-HDL cholesterol is out of safe range\n")
        print("What to Eat: Whole grain items , low fat dairy products , Eggs , fish , nuts.")
        print("What to Avoid: Full-fat dairy products(such as milk,curd), Read meat, Fried/Oily items, sweet items\n")

def Triglyceride():
    tgl = float(input("\nEnter Triglyceride (in mg/dl): "))
    if tgl < 150:
        print("\nCongratulations! your triglyceride is in safe range. Be Healthy, Be Safe!\n")
    elif tgl >= 150:
        print("\nYour triglyceride is out of safe range\n")
        print("What to Eat: Whole grain items , low fat dairy products , Eggs , fish , nuts.")
        print("What to Avoid: Full-fat dairy products(such as milk,curd),Alcohol , Coconut , Baked items.")

ans = True
while ans:
    print("""\tWelcome to Nutrition Checker 
        Be Healthy, Be Safe!""")

    print("""\n\t\t\t**MENU**
        1.Cholesterol
        2.LDL Cholesterol
        3.VLDL Cholesterol
        4.HDL Cholesterol
        5.Non-HDL Cholesterol
        6.Triglyceride""")
    ans = int(input("\tEnter your choice: "))
    if ans == 1:
        Cholesterol()
    elif ans == 2:
        LDL()
    elif ans == 3:
        VLDL()
    elif ans == 4:
        HDL()
    elif ans == 5:
        NonHDL()
    elif ans == 6:
        Triglyceride()
    elif ans != "":
        print("\nNot a valid choice, Try again!\n")