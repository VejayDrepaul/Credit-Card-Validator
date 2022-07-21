
def main():
    card_no = input("Enter the credit card number: ")[::-1]
    check_card(card_no)


def check_card(card_number):
    sum = 0
    temp = 0
    product_values = []

    letters = (
        # i % n == 0 means this letter should be replaced
        "0" if i % 2 == 0 else char

        # iterate index/value pairs
        for i, char in enumerate(card_number, 1)
    )
    card_number = ''.join(letters)
    print(card_number)

    for x in card_number:
        for n in str(x):
            temp = int(n) * 2
            product_values.append(temp)

    for u in product_values:
        print(u)

    for y in product_values:
        if int(y) > 9:
            for digit in str(y):
                sum += int(digit)
        else:
            sum += int(y)

    print(sum)


if __name__ == "__main__":
    main()