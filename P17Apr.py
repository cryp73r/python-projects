class resturant:
    def __init__(self, name, cuisine_type):
        self.name=name
        self.cuisine_type=cuisine_type

    def describ_res(self):
        print('Resturant Nme: ' + self.name)
        print("It's Cuisine Type: " + self.cuisine_type)

    def open_res(self):
        print('RESTURANT IS OPEN')

res_info=resturant('royal foods', 'indian')
res_info.open_res()
res_info.describ_res()
