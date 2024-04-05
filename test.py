import numpy as np
import pytest
from naloga2 import filtriraj_sobel_smer

def test_filtriraj_sobel_smer():
    # Testni podatki
    slika = np.array([[1, 2, 1],
                      [0, 0, 0],
                      [-1, -2, -1]])

    # Pričakovani rezultat
    expected_output = np.array([[0, 0, 0],
                                [0, 0, 0],
                                [0, 0, 0]])

    # Preverjanje rezultata
    assert np.array_equal(filtriraj_sobel_smer(slika), expected_output)


