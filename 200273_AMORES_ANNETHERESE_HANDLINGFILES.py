def get_product(code):
    return products[code]

def get_property(code,property):
    return products[code][property]

def main():
    order = ""
    code_list = []

    americano=0
    brewedcoffee=0
    cappuccino=0
    dalgona=0
    espresso=0
    frappuccino=0

    while order!="/":
        order = input("Input customer's order: ")
        if order!="/":
            code = order.split(",")[0]
            if code not in code_list:
                code_list.append(code)
                code_list.sort()
            else:
                pass
            qty = order.split(",")[1]
            if code == "americano":
                americano+=int(qty)
            elif code == "brewedcoffee":
                brewedcoffee+=int(qty)
            elif code == "cappuccino":
                cappuccino+=int(qty)
            elif code == "dalgona":
                dalgona+=int(qty)
            elif code == "espresso":
                espresso+=int(qty)
            elif code == "frappuccino":
                frappuccino+=int(qty)
        else:
            pass

    with open("receipt.txt","w") as f:
        f.write(f"""==
CODE\t\t\tNAME\t\t\tQUANTITY\t\t\tSUBTOTAL\n""")

        total=0
        for code in code_list:
            if code == "americano":
                quantity=americano
            elif code == "brewedcoffee":
                quantity=brewedcoffee
            elif code == "cappuccino":
                quantity=cappuccino
            elif code == "dalgona":
                quantity=dalgona
            elif code == "espresso":
                quantity=espresso
            elif code == "frappuccino":
                quantity=frappuccino

            name = get_product(code)["name"]
            subtotal = quantity*get_property(code,"price")
            total+=subtotal
            if code=="dalgona":
                f.write(f"""{code}\t\t\t{name}\t\t\t{quantity}\t\t\t\t{subtotal}\n""")
            else:
                f.write(f"""{code}\t\t{name}\t\t{quantity}\t\t\t\t{subtotal}\n""")
        f.write("""
""")
        f.write(f"""Total:\t\t\t\t\t\t\t\t\t\t{total}
==""")

    with open("receipt.txt","r") as f:
        fcontents = f.read()
        print (fcontents)

main()
