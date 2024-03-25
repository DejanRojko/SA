# SA
	
V tej nalogi boste implementirali konvolucijo in jo uporabili z različnimi jedri. 

def konvolucija(slika,jedro):
    pass

def filtriraj_z_gaussovim_jedrom(slika,sigma):
    pass

def filtriraj_sobel_smer(slika):
    pass
    
Funkcija konvolucija prejme dva argumenta, kjer je prvi argument vhodna slika, ki je predstavljena kot 2D tabela, drugi argument jedro, pa je prav tako 2D tabela. Obe tabeli sta podatkovnega tipa float32.

Funkcija filtriraj_z_gaussovim_jedrom prejme 2 argumenta. Prvi je slika, ki je istega tipa kot pri konvoluciji, drugi parameter sigma je pa tipa float. S pomočjo sigme boste izračunali gaussovo jedro, ter z njim z uporabo prej implementirane konvolucije sliko tudi filtrirali

Funkcija filtriraj_sobel_horizontalno prejme en argument, ki je slika, katero morate filtrirati z lastno konvolucijo. Ustrezno jedro lahko definirate kar v funkciji. V glavnem progmrau nato z uporabo filtrirane slike poiščite vse slikovne elemente katerih gradient je močnejši od 150 in jim v sliki, ki ste jo filtrirali spremenite barvo na zeleno barvo.
