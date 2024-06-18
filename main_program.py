import smtplib
from datetime import datetime
def choose_items():
    chosen_items=[]
    total_bill=0
    # Dairy product section
    def dairy_product():
        dairy_products={"milk": 12, "curd": 12, "cheese": 55, "milkshake": 25,"cone icecream": 20, "chocobar": 12, "cup icecream": 10}
        section_name="Dairy Products"
        chosen_section_items={}
        print(f"Available {section_name}:")
        for item, price in dairy_products.items():
            print(f"{item} = Rs.{price}")
        while True:
            grocery=input(f"What do you want in {section_name.lower()}? (type 'no' to finish): ").lower()
            if grocery=="no":
                break
            if grocery in dairy_products:
                try:
                    quantity=int(input(f"How many of {grocery} do you want to buy? "))
                    if quantity>0:
                        chosen_section_items[grocery]=dairy_products[grocery]*quantity
                except ValueError:
                    print("Please enter a valid number")
            else:
                print("Please choose from the available options")
        total=sum(chosen_section_items.values())
        return section_name, chosen_section_items, total
    # Cooking ingredients section
    def cooking_ingredients():
        ingredients={"sombu": 12, "venthiyam": 15, "kadugu": 13, "milagu": 23,"sugar": 34, "rice": 356, "salt": 13, "chicken masala": 20,"garam masala": 20, "mutton masala": 20, "chicken 65 masala": 20,"pepper powder": 10, "sambar powder": 10, "mr_gold oil": 55,"pasta": 33, "noodles": 20}
        section_name="Cooking Ingredients"
        chosen_section_items={}
        print(f"Available {section_name}:")
        for item, price in ingredients.items():
            print(f"{item} = Rs.{price}")
        while True:
            grocery=input(f"What do you want in {section_name.lower()}? (type 'no' to finish): ").lower()
            if grocery=="no":
                break
            if grocery in ingredients:
                try:
                    quantity=int(input(f"How many of {grocery} do you want to buy? "))
                    if quantity>0:
                        chosen_section_items[grocery] = ingredients[grocery] * quantity
                except ValueError:
                    print("Please enter a valid number")
            else:
                print("Please choose from the available options")
        total=sum(chosen_section_items.values())
        return section_name, chosen_section_items, total
    # Household and cleaning section
    def household_and_cleaning():
        products={"paste": 20, "soap": 40, "tooth brush": 25, "battery": 15,"dish soap": 10, "dishwasher detergent": 50, "fabric softener": 49,"floor cleaner": 90, "detergent powder": 25, "broom stick": 40,"door mat": 35, "face powder": 25, "shampoo": 50, "light bulbs": 50,"bottle": 56, "comb": 25, "knife": 29}
        section_name="Household and Cleaning Things"
        chosen_section_items={}
        print(f"Available {section_name}:")
        for item, price in products.items():
            print(f"{item} = Rs.{price}")
        while True:
            grocery=input(f"What do you want in {section_name.lower()}? (type 'no' to finish): ").lower()
            if grocery=="no":
                break
            if grocery in products:
                try:
                    quantity=int(input(f"How many of {grocery} do you want to buy? "))
                    if quantity>0:
                        chosen_section_items[grocery]=products[grocery]*quantity
                except ValueError:
                    print("Please enter a valid number")
            else:
                print("Please choose from the available options")
        total=sum(chosen_section_items.values())
        return section_name, chosen_section_items, total
    # Sweets and snacks section
    def sweets_and_snacks():
        products={"kitkat": 25, "dairymilk": 20, "milky bar": 10, "5star": 5,"lays": 10, "potato chips": 44, "murukku": 25, "marshmallow": 25,"candy": 10, "jelly beans": 12, "lollipop": 15}
        section_name="Sweets and Snacks"
        chosen_section_items={}
        print(f"Available {section_name}:")
        for item, price in products.items():
            print(f"{item} = Rs.{price}")
        while True:
            grocery=input(f"What do you want in {section_name.lower()}? (type 'no' to finish): ").lower()
            if grocery=="no":
                break
            if grocery in products:
                try:
                    quantity=int(input(f"How many of {grocery} do you want to buy? "))
                    if quantity>0:
                        chosen_section_items[grocery]=products[grocery]*quantity
                except ValueError:
                    print("Please enter a valid number")
            else:
                print("Please choose from the available options")
        total=sum(chosen_section_items.values())
        return section_name, chosen_section_items, total
    # Baby product section
    def baby_product():
        products={"milk powder": 359, "cerelac": 200, "diaper": 25, "baby bottle": 80,"wipes": 100, "baby powder": 120, "baby shampoo": 118, "baby soap": 130,"baby towel": 300}
        section_name="Baby Products"
        chosen_section_items={}
        print(f"Available {section_name}:")
        for item, price in products.items():
            print(f"{item} = Rs.{price}")
        while True:
            grocery=input(f"What do you want in {section_name.lower()}? (type 'no' to finish): ").lower()
            if grocery=="no":
                break
            if grocery in products:
                try:
                    quantity=int(input(f"How many of {grocery} do you want to buy? "))
                    if quantity>0:
                        chosen_section_items[grocery]=products[grocery]*quantity
                except ValueError:
                    print("Please enter a valid number")
            else:
                print("Please choose from the available options")
        total=sum(chosen_section_items.values())
        return section_name, chosen_section_items, total
    sections=[dairy_product(),cooking_ingredients(),household_and_cleaning(),sweets_and_snacks(),baby_product()]
    for section_name, section_items, total in sections:
        chosen_items.append((section_name, section_items))
        total_bill+=total
    return chosen_items, total_bill
def generate_bill(chosen_items, total_cost):
    current_datetime=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bill_content=f"Super Market Bill:\n{current_datetime}\n\n"    
    for section_name, section_items in chosen_items:
        bill_content+=f"{section_name}:\n"
        for item, price in section_items.items():
            bill_content+=f"  {item}: Rs.{price}\n"    
    bill_content+=f"\nTotal cost of all items: Rs.{total_cost}\n"  
    f=open("bills.txt", "w") 
    f.write(bill_content)    
    print("Bill generated and saved as 'bills.txt'.")
    return bill_content   
def send_email(bill_content):
    recipient_email=input("Please enter your Gmail ID: ")
    sender_email="aishwaryar0386@gmail.com"
    sender_password="sender_password"    
    subject="Super Market Bill"
    body=bill_content
    email_text=f"Subject: {subject}\n\n{body}"    
    try:
        server=smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, email_text)
        server.quit()
        print("Email sent successfully!")
    except:
        print(f"Failed to send email..")
def main():
    chosen_items, total_cost=choose_items()
    bill_content=generate_bill(chosen_items, total_cost)
    send_email(bill_content)
main()
