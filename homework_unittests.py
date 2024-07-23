# დავალება 67 აგუნიში
#
# შექმენით პროგრამა, რომელიც დაითვლის, თუ რამდენი გალონი საღებავია საჭირო ჭერის შესაღებად.
#  შეეკითხეთ მომხმარებელს ოთახის სიგრძე და სიგანე და ჩათვალეთ რომ
#  ერთი გალონი 350 კვადრატული ფუტის ტოლია.

# მაგალითად:
# $ Length of your room: 12
# $ Width of your room: 30
# $ You will need to purchase 2 gallons of
# $ paint to cover 360 square feet.


# აუცილებელი მოთხოვნები:

# დაწერეთ ამ დავალების შესაბამისი ტესტები, pytest-ის გამოყენებით.
# დაყავით კოდი ფუნქციებად და მოარგეთ თქვენს ტესტებს.
 

# import math
# def main():
#     inp=user_inform()
#     calc=calc_paint(inp)
#     return print(f"You need {calc} galons")

# def user_inform():

#     while True:
#         Length_room =input("Length of your room: ")
#         Width_room =input("Width of your room: ")
#         if Length_room.isdigit() and Width_room.isdigit():
#             return float (Length_room) * float (Width_room)
#         else:
#             print("Please enter current number: ")
#             continue

# def calc_paint(sum_multiplai):
        
#     if sum_multiplai > 350:
#         ssm=sum_multiplai / 350
#         numb=math.ceil(ssm)
#     return numb



# if __name__=="__main__":
#     main()



# tests _ ების გვერდი

# from unittest.mock import patch
# from homework_unittests import calc_paint, user_inform

# def test_calc_paint():
#     assert calc_paint(360)==2

# @patch('builtins.input', side_effect=['12', '30'])
# def test_user_inform_valid_input(mock_input):
#     assert user_inform() == 360
    



# davaleba 68
#შექმენით პროგრამა, რომელიც მომხმარებელს შეეკითხება სამი სხვადასხვა
#  ნივთის ფასს და რაოდენობას. დაითვალეს მომხმარებლის მიერ
#  შეყვანილი ნივთების საერთო ფასი (გაითვალისწინეთ,
#  რომ თუ პირველი ნივთის რაოდენობა არის 2, 
# მაშინ მისი ფასი უნდა გაამრავლოთ 2-ზე და ისე მიუმატოთ საერთო ფასს).
#  დამატებით გამოთვალეთ საერთოდ ფასის 5.5%-იანი გადასახადი და მთლიანი ფასი გადასახადთან ჩათვლით. 
# საბოლოო ჯამში, პროგრამამ უნდა გამოიტანოს ნივთების საერთო ფასი,
#  გადასახადის ფასი და ჯამური ფასი გადასახადიანა.

# მაგალითად:

# $ Enter the price of item 1: 25
# $ Enter the quantity of item 1: 2
# $ Enter the price of item 2: 10
# $ Enter the quantity of item 2: 1
# $ Enter the price of item 3: 4
# $ Enter the quantity of item 3: 1
# $ Subtotal: $64.00
# $ Tax: $3.52
# $ Total: $67.52


# აუცილებელი მოთხოვნები:

# დაწერეთ ამ დავალების შესაბამისი ტესტები, pytest-ის გამოყენებით.
# დაყავით კოდი ფუნქციებად და მოარგეთ თქვენს ტესტებს. 


# def use_cost():
#     numb=0   
#     item_qty=0
#     item_prc=0
#     i=0
#     while i < 3:
#         numb+=1
#         i+=1

#         user=input(f"Enter the price of item {numb}: ")
#         user_qty=input(f"Enter the quantity of item {numb}: ")
#         if user.isdigit() and user_qty.isdigit():
#             item_qty += float(user_qty)
#             item_prc += float(user_qty) * float(user)
#             print(item_prc)
#         else:
#             print("Please enter current number: ")
#             numb-=1
#             i-=1
#             continue
#     fin_sum_pc=item_prc*5.5
#     fin_sum_cost=item_prc+fin_sum_pc
#     print(f"Subtotal: {item_prc}$\nTax: {fin_sum_pc}$ \nTotal: {fin_sum_cost}$")
#     return item_prc
# use_cost()



# test page
# from unittest.mock import patch
# from homework_unittests import use_cost



# @patch('builtins.input', side_effect=["2", "3","2","3","2","3"])
# def test_user_inform_valid_input(mock_input):
#     assert use_cost() == 18
    
    
# davaleba 68v2

# def main():
#     us_cst=use_cost()
#     return tax_calc(us_cst)


# def tax_calc(us_cst):
#     fin_sum_pc=us_cst*5.5
#     fin_sum_cost=us_cst+fin_sum_pc
#     return us_cst,fin_sum_pc,fin_sum_cost



# def use_cost():
#     numb=0   
#     item_qty=0
#     item_prc=0
#     i=0
#     while i < 3:
#         numb+=1
#         i+=1

#         user=input(f"Enter the price of item {numb}: ")
#         user_qty=input(f"Enter the quantity of item {numb}: ")
#         if user.isdigit() and user_qty.isdigit():
#             item_qty += float(user_qty)
#             item_prc += float(user_qty) * float(user)
#         else:
#             print("Please enter current number: ")
#             numb-=1
#             i-=1
#             continue
#     return item_prc


    

# test page
# import pytest

# def test_tax_calc():
#     us_cst = 100
#     subtotal, tax, total = tax_calc(us_cst)
#     assert subtotal == 100
#     assert tax == 550
#     assert total == 650

# def test_tax_calc_zero():
#     us_cst = 0
#     subtotal, tax, total = tax_calc(us_cst)
#     assert subtotal == 0
#     assert tax == 0
#     assert total == 0

# def test_tax_calc_negative():
#     us_cst = -100
#     subtotal, tax, total = tax_calc(us_cst)
#     assert subtotal == -100
#     assert tax == -550
#     assert total == -650

# def test_tax_calc_float():
#     us_cst = 100.5
#     subtotal, tax, total = tax_calc(us_cst)
#     assert subtotal == 100.5
#     assert tax == 552.75
#     assert total == 653.25





# davaleba 69
#შექმენით პროგრამა, რომელიც გარდაქმნის თანხას ევროდან ამერიკულ დოლარებში.
#  შეეკითხეთ მომხმარებელს ის თანხა, რომელიც მას აქვს 
# ევროებში და ასევე ამჟამინდელი გადაცვლის კურსი. 
# გამოიტანეთ თანხა დოლარებში. ფორმულა:

# amount_to = amount_from * rate_from / rate_to
# სადაც amount_to არის თანხის რაოდენობა დოლარებში.
# amount_from არის თანხის რაოდენობა ევროებში.
# rate_from არის ამჟამინდელი კურსი ევროებში.
# rate_to არის ამჟამინდელი კურსი დოლარებში.

# მაგალითად:
# $ How many euros are you exchanging? 81
# $ What is the exchange rate? 137.51
# $ 81 euros at an exchange rate of 137.51 is
# $ 111.38 U.S. dollars.


# აუცილებელი მოთხოვნები:

# დაწერეთ ამ დავალების შესაბამისი ტესტები, pytest-ის გამოყენებით.
# დაყავით კოდი ფუნქციებად და მოარგეთ თქვენს ტესტებს.
# დაამრგვალეთ ცენტები ათეულებამდე.

# დამატებითი გამოწვევები:

# იმის მაგივრად, რომ გაცვლის კურსი მომხმარებელს შეეკითხოთ, 
# წამოიღეთ ეს ინფორმაცია რომელიმე API-დან. 



# def inp():
#     while True:
#         try:
#             us_eu_inp=float(input("How many euros are you exchanging?: "))
#             us_chng_inp=float(input("What is the exchange rate?: "))
#             if us_eu_inp > 0 and us_chng_inp > 0:
#                 return us_eu_inp,us_chng_inp
#             else:
#                 raise ValueError
#         except ValueError:
#             print("Please enter a positive number")
#             continue


# def sum_inp(um,ex):
#     us_sum=um*ex
#     return us_sum
    # return print(f"{um} euros at an exchange rate of {ex} is $ {us_sum} U.S. dollars.")

# test page
# from homework_unittests import sum_inp, inp
# from unittest.mock import patch



# @patch('builtins.input', side_effect=[81, 1.3751])
# def test_user_inform_valid_input(mock_input):
#     assert inp() == (81,1.3751)

# def test_sum():
#     assert sum_inp(2,2) == 4




#DAVALEBA 70
# მარტივი ინტერესის დათვლის მეთოდი არის სწრაფი და ეფექტური გზა,
#  რომ დაითვალოთ აქვს თუ არა ინვესტიციას ღირებულება. შექმენით პროგრამა,
#  რომელიც დაითვლის მარტივ ინტერესს. 
# შეეკითხეთ მომხმარებელს მიღებული ინვესტიციის რაოდენობა (Principal Amount), 
# საპროცენტო განაკვეთი და დრო.

# ფორმულა:


# სადაც P არის მიღებული ინვესტიციის რაოდენობა (Principal Amount)
# r არის საპროცენტო განაკვეთი
# t არის წლების რაოდენობა

# მაგალითად:

# $ Enter the principal: 1500
# $ Enter the rate of interest: 4.3
# $ Enter the number of years: 4
# $ After 4 years at 4.3%, the investment will
# $ be worth $1758.

# def main():
#     p,r,t=inp()
#     a=multip(p,r,t)
#     return print(f"After {t} years at {r}, the investment will be worth ${a}")

# def inp():
#     while True:
#         try:
#             p=float(input("Enter the principal: "))
#             r=float(input("Enter the rate of interest: "))
#             t=float(input("Enter the number of years: "))
#             return p,r,t
#         except ValueError:
#             print("Please enter a positive number")
#             continue

# def multip(p,r,t):
#     a=(p*r/100)*t+p
#     return a

# test page
# from homework_unittests import multip, inp
# from unittest.mock import patch


# @patch('builtins.input', side_effect=[1500, 4.3, 4])
# def test_mult(mock_input):
#     assert multip(1500, 4.3, 4) == 1758

# @patch('builtins.input', side_effect=[1500, 4.3, 4])
# def test_inp(mock_input):
#     assert inp() == (1500,4.3,4)
    



# davaleba 71
# რთული პროცენტი (Compound Interest) არის დეპოზიტზე,
#  სესხზე ან სხვა ფინანსურ აქტივზე პროცენტის დარიცხვის მეთოდი.
#  შექმენით პროგრამა, რომელიც დაითვლის რთულ პროცენტს დროთა განმავლობაში.
#  შეეკითხეთ მომხმარებელს საწყისი ღირებულება, წლების რაოდენობა ინვესტიციისთვის,
#  პროცენტული ინტერესი და წლის განმავლობაში მონაკვეთების რაოდენობა, როცა დაემატება
#  რთული პროცენტი. გამოიყენეთ ფორმულა:


# სადაც P არის მიღებული ინვესტიციის რაოდენობა (Principal Amount)
# r არის პროცენტული ინტერესი
# t არის წლების რაოდენობა
# n არის წლის განმავლობაში მონაკვეთების რაოდენობა, როცა დაემატება რთული პროცენტი

# მაგალითად:

# $ What is the principal amount? 1500
# $ What is the rate? 4.3
# $ What is the number of years? 6
# $ What is the number of times the interest
# $ is compounded per year? 4
# $ $1500 invested at 4.3% for 6 years
# $ compounded 4 times per year is $1938.84.

# def main():
#     p,r,t,n=inp()
#     a=calc_inp(p,r,t,n)
#     return print(f"After {t} years at {r}, the investment will be worth ${a}")

# def inp():
#     while True:
#         try:
#             p=float(input("Enter the principal: "))
#             r=float(input("Enter the rate of interest: "))
#             t=float(input("Enter the number of years: "))
#             n=float(input("Enter the number of times interest is compounded per year: "))
#             return p,r,t,n
#         except ValueError:
#             print("Please enter a positive number")
#             continue

# def calc_inp(p,r,t,n):
#     i=0
#     while i<t*n:
#         a=(p*r/100)/4
#         p+=a
#         i+=1
#     return round(p,2)

# test page
# from homework_unittests import inp, calc_inp
# from unittest.mock import patch


# @patch("builtins.input",side_effect=[1500,4.3,6,4])
# def test_inp(mock_input):
#     assert inp()==(1500, 4.3, 6, 4)

# def test_calc():
#     assert calc_inp(1500,4.3,6,4)==1938.84