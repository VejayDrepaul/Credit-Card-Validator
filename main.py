import array as arr

from numpy import number 

def main():
    #Driver code
    cc = input("Enter your credit card number: ")
    validate_card(cc)

def validate_card(card_number):
    numbers = []
    for x in card_number: 
        numbers.append(x)


    numbers.reverse()

    
    for element in numbers[1::2]:
        print(element)
        

main()