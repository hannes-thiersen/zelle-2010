# File:          coffee_shipping_order-progex3.5.py
# Date:          2019-09-26
# Author:        "Hannes Thiersen" <hannesthiersen@gmail.com>
# Exercise:      prog ex 3.5
# Description:
#   The Donditorie coffee shop sells coffee at $10.50 a pound plus the cost of
#   shipping. Each order ships for $0.86 per pound + $1.50 fixed cost for
#   overhead. Write a program that calculates the cost of an order.

#-----------------------------------------------------------------------------
# FUNCTIONS
#-----------------------------------------------------------------------------
def main():
    print("Calculate the shipping cost to the business of an order.")
    weight = eval(
                input(
                    "Insert the total weight of the coffee in the order: "
                    ))
    shipping_cost = weight*0.86 + 1.5
    print(f"The shipping cost is ${shipping_cost}")

#-----------------------------------------------------------------------------
# MAIN
#-----------------------------------------------------------------------------
if __name__ == "__main__":

    main()
