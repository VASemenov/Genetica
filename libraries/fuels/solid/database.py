from libraries.fuels.solid import *


class Fuel:
    def __init__(self, name, model, Ro, u0, v, B):

        self.params = {'Ro': Ro,
                       'u_0': u0,
                       'nu': v,
                       'Betta': B * 9.8}

        self.name = name
        self.model = model
        self.density = Ro
        self.linear_speed = u0
        self.v = v
        self.B = B*9.8




data = dict()


def add_fuel(name, model, Ro, u0, v, B):
    data[name] = Fuel(name, model, Ro, u0, v, B)


add_fuel('MGP', MGP, 1610, 0.383, 0.7, 180)
add_fuel('NM-2', NM2, 1600, 0.7, 0.6, 177)
add_fuel('SC', SC, 1570, 0.41, 0.69, 185)
add_fuel('PCA-1', PCA1, 1650, 2.15, 0.3, 151)
add_fuel('PCA-2', PCA2, 1730, 8.14, 0.19, 143)
add_fuel('PCA-3M', PCA3M, 1740, 3.44, 0.26, 158)
add_fuel('PCA-4M', PCA4M, 1800, 6.49, 0.24, 154)
add_fuel('PCA-5M', PCA5M, 1530, 3.9, 0.40, 158)
add_fuel('PCA-6M', PCA6M, 1320, 0.99, 0.43, 160)
add_fuel('PCA-7M', PCA7M, 1720, 6.15, 0.23, 160)
add_fuel('PCA-8M', PCA8M, 1280, 9.81, 0.21, 182)
add_fuel('PCA-9M', PCA9M, 2020, 2.51, 0.39, 136)
add_fuel('PCK-1M', PCK1M, 2040, 4.72, 0.28, 139)
add_fuel('PCL-1', PCL1, 1940, 1.5, 0.47, 140)
add_fuel('PCL-2М', PCL2M, 1970, 5.28, 0.25, 149)
add_fuel('PCL-3М', PCL3M, 1720, 7.05, 0.30, 161)
add_fuel('PCN-1М', PCN1M, 1760, 17.01, 0.29, 168)
add_fuel('PCN-2М', PCN2M, 2430, 14.5, 0.19, 103)
