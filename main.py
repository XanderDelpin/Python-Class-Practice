class Menu:

  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
    return f"The {self.name} menu is available from {self.start_time} to {self.end_time}"

  def get_name(self):
    return self.name

  def calculate_bill(self, purchased_items):
    adder = 0
    if (type(purchased_items) == list):
      for x in purchased_items:
        adder += self.items[x]
    return f"The total of your purchase is ${adder}"



brunch_items = {'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

early_bird_items = {'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}

dinner_items = {'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}

kids_items = {'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}




brunch = Menu("Brunch", brunch_items, 1100, 1600)

early_bird = Menu("Early Bird", early_bird_items, 1500, 1800)

dinner = Menu("Dinner", dinner_items, 1700, 2300)

kids = Menu("Kids", kids_items, 1100, 2100)

list_of_menus = [brunch, early_bird, dinner, kids]



print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))

print("\n")

print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

#------------------------------------------------------------------------

class Franchise:

  def __init__(self, address, menus):
    self.address = address
    self.menus = menus

  def available_menus(self, time):
    list_of_available_menus = []
    if (time >= 1100 and time < 1600):
      list_of_available_menus.append(brunch)
    if (time >= 1500 and time < 1800):
      list_of_available_menus.append(early_bird)
    if (time >= 1700 and time < 2300):
      list_of_available_menus.append(dinner)
    if (time >= 1100 and time < 2100):
      list_of_available_menus.append(kids)
    return list_of_available_menus
    
      




flagship_store = Franchise("1232 West End Road", list_of_menus)

new_installment = Franchise("12 East Mulberry Street", list_of_menus)

print(flagship_store.available_menus(1200))

print("\n\n")

print(new_installment.available_menus(1700))

#--------------------------------------------------------------------------------

class Bussiness:
  def __init__(self, name, franchises):
    self.name = name
    self.franchises = franchises

basta_fazoolin = Bussiness("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepa_items = {'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

arepas_menu = Menu("Arepas", arepa_items, 1000, 2000)

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

take_a_arepa = Bussiness("Take a' Arepa", [arepas_place])














