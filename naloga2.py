import cv2 as cv
import numpy as np


def konvolucija(slika, jedro):
    '''Izvede konvolucijo nad sliko. Brez uporabe funkcije cv.filter2D, ali katerekoli druge funkcije, ki izvaja konvolucijo.
    Funkcijo implementirajte sami z uporabo zank oz. vektorskega računanja.'''

    visina_slike, sirina_slike = slika.shape
    visina_jedra, sirina_jedra = jedro.shape
    pad_v, pad_s = visina_jedra // 2, sirina_jedra // 2

    slika_padded = np.pad(slika, ((pad_v, pad_v), (pad_s, pad_s)))
    output = np.zeros_like(slika)

    for y in range(visina_slike):
        for x in range(sirina_slike):
            crop = slika_padded[y: y + visina_jedra, x: x + sirina_jedra]
            kon = jedro * crop
            output[y, x] = np.sum(kon)

    return output


def filtriraj_z_gaussovim_jedrom(slika, sigma):
    '''Filtrira sliko z Gaussovim jedrom..'''

    velikost_jedra = int(2 * sigma) * 2 + 1
    k = (velikost_jedra - 1) / 2
    jedro = np.zeros((velikost_jedra, velikost_jedra))

    for i in range(velikost_jedra):
        for j in range(velikost_jedra):
            jedro[i, j] = (1 / (2 * np.pi * sigma ** 2)) * np.exp(
                -(((i - k - 1) ** 2) + ((j - k - 1) ** 2)) / (2 * sigma ** 2))

    return jedro


def filtriraj_sobel_smer(slika):
    '''Filtrira sliko z Sobelovim jedrom in označi gradiente v orignalni sliki glede na ustrezen pogoj.'''

    gauss = filtriraj_z_gaussovim_jedrom(slika, 1)
    gauss_kon = konvolucija(slika, gauss)
    sobel_x = np.array([[-1, -2, -1], [0, 0, 0], [1, 2, 1]])

    output = konvolucija(gauss_kon, sobel_x)

    return output


if __name__ == '__main__':
    slika = cv.imread('.utils/lenna.png', cv.IMREAD_GRAYSCALE).astype(np.float32)
    slika_color = cv.imread('.utils/lenna.png')

    sigma = float(10)

    jedro1 = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])

    jedro = filtriraj_z_gaussovim_jedrom(slika, sigma)
    output_gauss = konvolucija(slika, jedro)
    output_konvolucija = konvolucija(slika, jedro1)

    output_sobel_x = filtriraj_sobel_smer(slika)

    mask = output_sobel_x > 150

    slika_color[mask] = [0, 255, 0]

    output_gaussian_clipped = np.clip(output_gauss, 0, 255).astype(np.uint8)

    cv.imshow('Original Image', slika.astype(np.uint8))
    cv.imshow('Gauss', output_gaussian_clipped)
    cv.imshow('Konvolucija', output_konvolucija)
    cv.imshow('Zelena', slika_color)
    cv.waitKey(0)
    cv.destroyAllWindows()