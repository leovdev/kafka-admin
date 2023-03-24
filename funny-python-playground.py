class Perro():
    def __init__(self, patas, orejas):
        self.patas = patas
        self.orejas = orejas

jhonny = Perro(4, 2)

print(hasattr(jhonny,'patas1'))

print('tiene') if hasattr(jhonny,'patas1') else print('no tiene')