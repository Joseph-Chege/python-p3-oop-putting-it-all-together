#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand=None, size=None):
        self._brand = None
        self._size = None
        if brand is not None and size is not None:
            self.brand = brand
            self.size = size
        else:
            raise ValueError("brand and size are required")
        
    @property
    def brand(self):
        return self._brand
    
    @brand.setter
    def brand(self, value):
        self._brand = value.title()

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"

stan_smith = Shoe('Adidas', 8)
print(stan_smith.brand)
print(stan_smith.size)
print(stan_smith.cobble())