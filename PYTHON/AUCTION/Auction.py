logo = '''
                         _____
                         \         /
                          )___(
                          |"""""""|.-.,.---------.,.-.
                          |       | | |               | | ''-.
                          |       || |             | |..-'
                          |___| '-' `'---------'` '-'
                          )"""""""(
                         /___\\
                       .-------------.
                      /_____\\
'''
print(logo)
name_bid = {}


def fn():
    name = input("Enter your name?\n")
    bid = input("Please enter your bid amount in ₹\n")
    name_bid[name] = bid


fn()
while input("do u want to enter the bid again: Yes or No:\n") == "Yes":
    fn()
bid_amount = 0
print("\n\nAll bids are as following:")
for x in name_bid:
    if int(name_bid[x]) > bid_amount:
        bid_amount = int(name_bid[x])
    print(x, name_bid[x])
print(f"\n\n{x} won the bid\nHis bid was {name_bid[x]}")
