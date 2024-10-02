class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
    
    def describe(self):
        return f"It is {self.year} {self.color} {self.model} car and it is {"for sale" if self.for_sale else "not for sale"}."

def main():
    car1 = Car(model = "Chevrolet", year = 2024, color = "red", for_sale = False)
    print(car1.describe())

main()

    