
# ISM2411 Lab 11 - Customer Dictionary & Lookup
# Name: Mina Ergin
# I used Ai to help me with areas I got stuck on.

# Question 1:
# In a real life situation, for work I would use .get() 
# when I'm not sure about the existence or availability 
# of certain information. For example a customers phone 
# number for a purchase. I would use .get() to avoid a 
# KeyError if the phone number is not available in the 
# dictionary. I would use brackets when I know that the 
# information should already be there. 

# Question 2:
# Exercise 8 showed me how Python can make it easier to 
# summarize data. For example Python can take individual 
# sales records and turn them into a summary of sales which
# is overall easier to understand. This is useful for work 
# because it can help me to quickly understand the overall 
# sales performance. You can also do this in PivotTable in 
# in Excel but I had to write the steps myself instead of 
# selecting options in a spreadhsheet. I think Python is 
# really useful for businesses that need to organize new 
# sales data and summarize it quickly and regularly. 



# Exercise 1 - One Customer

print("\nExercise 1")

customer = {
    "name": "Alice",
    "email": "alice@email.com",
    "tier": "gold",
    "ytd_spend": 1500
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2 - Update and Add

print("\nExercise 2")

customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)



# Exercise 3 - Safe Lookup

print("\nExercise 3")

print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email does not exist")



# Exercise 4 - Iterate

print("\nExercise 4")

for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), the loop only returns the keys.
# With .items(), the loop returns both keys and values.

for key in customer:
    print(key)



# Exercise 5 - Lookup Table

print("\nExercise 5")

tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

tier = customer["tier"]
discount = tier_discounts.get(tier, 0)

purchase_price = 200
final_price = purchase_price * (1 - discount)

print(f"Tier: {tier}")
print(f"Discount: {discount:.0%}")
print(f"Final price: ${final_price:.2f}")



# Exercise 6 - List of Dictionaries

print("\nExercise 6")

customers = [
    customer,
    {
        "name": "Bob",
        "tier": "silver",
        "ytd_spend": 800
    },
    {
        "name": "Charlie",
        "tier": "bronze",
        "ytd_spend": 300
    }
]

for person in customers:
    name = person["name"]
    tier = person["tier"]
    discount_rate = tier_discounts.get(tier, 0)
    discount_amount = 300 * discount_rate

    print(
        f"{name} - Tier: {tier}, "
        f"Discount: ${discount_amount:.2f}"
    )



# Exercise 7 - Nested Catalog

print("\nExercise 7")

catalog = {
    "Widget A": {
        "price": 9.99,
        "stock": 150
    },
    "Gadget C": {
        "price": 49.99,
        "stock": 8
    }
}

for product, details in catalog.items():
    if details["stock"] < 20:
        print(
            f"LOW STOCK: {product} - "
            f"{details['stock']} remaining"
        )



# Exercise 8 - Sales by Region

print("\nExercise 8")

transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_summary = {}

for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]

    sales_summary[region] = (
        sales_summary.get(region, 0) + amount
    )

for region in sorted(sales_summary):
    print(f"{region}: ${sales_summary[region]}")
