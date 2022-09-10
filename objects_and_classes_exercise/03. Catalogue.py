class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        sorted_list = []
        for i in range(len(self.products)):
            for j in range(len(self.products[i])):
                if first_letter == self.products[i][0]:
                    sorted_list.append(self.products[i])
                    break
        return sorted_list

    def __repr__(self):
        x = '\n'
        return f"Items in the {self.name} catalogue:\n" \
               f"{x.join(sorted(self.products))}"



catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
