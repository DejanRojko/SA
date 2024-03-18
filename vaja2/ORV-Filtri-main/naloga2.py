import cv2 as cv
import numpy as np

def konvolucija(slika, jedro):
    '''Izvede konvolucijo nad sliko. Brez uporabe funkcije cv.filter2D, ali katerekoli druge funkcije, ki izvaja konvolucijo.
    Funkcijo implementirajte sami z uporabo zank oz. vektorskega računanja.'''

    visina_slike, sirina_slike = slika.shape
    visina_jedra, sirina_jedra = jedro.shape
    pad_v, pad_s = visina_jedra // 2, sirina_jedra // 2

    slika_padded = np.pad(slika, ((pad_v, pad_v), (pad_s, pad_s)), mode='constant')
    output = np.zeros_like(slika)

    for y in range(visina_slike):
        for x in range(sirina_slike):
            output[y, x] = (jedro * slika_padded[y: y + visina_jedra, x: x + sirina_jedra]).sum()

    return output

def filtriraj_z_gaussovim_jedrom(slika,sigma):
    '''Filtrira sliko z Gaussovim jedrom..'''
    pass

def filtriraj_sobel_smer(slika):
    '''Filtrira sliko z Sobelovim jedrom in označi gradiente v orignalni sliki glede na ustrezen pogoj.'''
    pass


if __name__ == '__main__':
    # Load an image
    slika = cv.imread('.utils/lenna.png', cv.IMREAD_GRAYSCALE).astype(np.float32)

    # Define a kernel
    jedro = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]], dtype=np.float32)

    # Apply the convolution operation
    output = konvolucija(slika, jedro)

    # Display the original and filtered images
    cv.imshow('Original Image', slika)
    cv.imshow('Filtered Image', output)
    cv.waitKey(0)
    cv.destroyAllWindows()