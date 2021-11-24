import datetime

class Order():
    def __init__(self, customer_name, order_date, quantity, product_name,
                 spice_level, preferred_delivery_date, glass_bottle):

        self.customer_name = customer_name
        self.order_date = order_date
        self.quantity = quantity
        self.product_name = product_name
        self.spice_level = spice_level
        self.preferred_delivery_date = preferred_delivery_date
        self.glass_bottle = glass_bottle
         


tomorrow = datetime.date.today() + datetime.timedelta(days = 1)
day_after_that = datetime.date.today() + datetime.timedelta(days = 2)

order1 = Order("Terry Chilli", datetime.date.today(), 5000, "Dominator", 10, tomorrow, True)
order2 = Order("Christopher Chilli", datetime.date.today(), 100, "Smooth Delight", 10, day_after_that, False)
orders = [order1, order2]