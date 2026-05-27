#Benjamin Flores
#The Grocery Store
global items
global prices




items = ["Milk", "Eggs", "Bread", "Butter", "Cheese",
    "Chicken Breast", "Ground Beef", "Pork Chops", "Bacon", "Sausage",
    "Pasta", "Rice", "Quinoa", "Cereal", "Oatmeal",
    "Apples", "Bananas", "Oranges", "Strawberries", "Blueberries",
    "Grapes", "Pineapple", "Mangoes", "Lemons", "Limes",
    "Potatoes", "Onions", "Garlic", "Carrots", "Broccoli",
    "Cauliflower", "Spinach", "Kalepyth", "Lettuce", "Bell Peppers",
    "Tomatoes", "Cucumbers", "Zucchini", "Mushrooms", "Avocados",
    "Olive Oil", "Vegetable Oil", "Cooking Spray", "Salt", "Pepper",
    "Sugar", "Brown Sugar", "Flour", "Baking Powder", "Baking Soda",
    "Peanut Butter", "Jelly", "Honey", "Maple Syrup", "Nutella",
    "Coffee", "Tea", "Hot Chocolate", "Creamer", "Sugar Packets",
    "Orange Juice", "Apple Juice", "Soda", "Sparkling Water", "Sports Drink",
    "Chips", "Crackers", "Pretzels", "Popcorn", "Cookies",
    "Ice Cream", "Frozen Pizza", "Frozen Vegetables", "Frozen Chicken Nuggets", "Frozen Waffles",
    "Canned Soup", "Canned Beans", "Canned Corn", "Canned Tomatoes", "Canned Tuna",
    "Ketchup", "Mustard", "Mayonnaise", "BBQ Sauce", "Hot Sauce",
    "Paper Towels", "Toilet Paper", "Facial Tissues", "Dish Soap", "Laundry Detergent"]

prices = [3.49, 2.99, 2.79, 3.99, 4.59,
    7.99, 6.49, 5.99, 4.99, 4.49,
    1.79, 4.29, 5.99, 3.99, 3.49,
    4.49, 1.39, 3.99, 4.99, 5.49,
    5.49, 3.49, 4.99, 1.79, 1.79,
    3.99, 2.49, 1.29, 2.29, 2.99,
    3.49, 3.49, 3.99, 2.49, 3.49,
    2.99, 1.79, 2.49, 2.99, 1.99,
    7.99, 5.49, 3.99, 1.29, 2.49,
    2.49, 2.99, 3.49, 2.49, 1.99,
    3.99, 3.29, 4.99, 6.99, 5.49,
    9.99, 4.49, 3.99, 2.49, 1.99,
    4.29, 3.99, 1.99, 2.49, 2.99,
    3.99, 3.49, 2.99, 2.49, 4.99,
    5.99, 6.49, 2.99, 7.49, 4.99,
    2.79, 1.49, 1.29, 1.79, 2.49,
    2.99, 2.49, 4.49, 3.49, 3.99,
    8.99, 12.99, 3.99, 2.99, 11.99]

def discount(decimal):
    for i in range(len(prices)):
        prices[i] = prices[i] * (1-float(decimal))
def price_check(item_name):
    global items
    global prices
    for i in range (len(items)):
        if item_name == items[i]:
            return(prices[i])

    if item_name != items[0:len(items)]:
        print("Item not availible")
def budget(cost):
    global items
    global prices
    for i in range(len(prices)):
        if cost >= prices[i]:
            print(items[i])

#main
discount(0.2)
budget(2.00)
total = float(price_check("Frozen Waffles"))+float(price_check("Coffee"))+float(price_check("Sugar"))+float(price_check("Maple Syrup"))+float(price_check("Butter"))
x = round(total,4)
total = x
print(total)
