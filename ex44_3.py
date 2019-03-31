class Lambada(object):
    
    def steps_rhythm(self):
        print("slow cik cik")

    def roots(self):
        print("Caribbean")
    
    def outfit(self):
        print("bikinis and short skirts!")

    def music(self):
        print("Kaoma!")


class Lamba_Zouk(object):

    def __init__(self):
        self.lambada = Lambada()

    def outfit(self):
        print("casual")

    def music(self):
        print("even more slow cik cik")
    
    def dancers(self):
        print("Ryel and Jessica!")
    
    def steps_rhythm(self):
        self.lambada.steps_rhythm()
    
    def roots(self):
        self.lambada.roots()


class Zouk(object):

    def __init__(self):
        self.lamba_zouk = Lamba_Zouk()

    def outfit(self):
        print("tracksuits")

    def music(self):
        print("also lyrical")

    def roots(self):
        print("Caribbean and Brasil")

    def also_like(self):
        self.lamba_zouk.dancers()

    def steps_rhythm(self):
        self.lamba_zouk.steps_rhythm()
    
    def dancers(self):
        self.lamba_zouk.dancers()

    
lambada = Lambada()
lamba_zouk = Lamba_Zouk()
zouk = Zouk()

print("\nLambada!")

print("steps_rhythm: ")
lambada.steps_rhythm()
print("roots: ")
lambada.roots()
print("outfit: ")
lambada.outfit()
print("music: ")
lambada.music()

print("\nLamba Zouk")

print("steps_rhythm: ")
lamba_zouk.steps_rhythm()
print("roots: ")
lamba_zouk.roots()

print("outfit: ")
lamba_zouk.outfit()
print("music: ")
lamba_zouk.music()
print("dancers: ")
lamba_zouk.dancers()

print("\nZouk")

print("steps_rhythm: ")
zouk.steps_rhythm()
print("dancers: ")
zouk.dancers()

print("roots: ")
zouk.roots()
print("outfit: ")
zouk.outfit()
print("music: ")
zouk.music()

print("also like: ")
zouk.also_like()
