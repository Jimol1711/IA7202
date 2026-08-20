"""Clase ``Imagen``: contenedor de imágenes sobre el que se opera con NumPy."""

from __future__ import annotations

import numpy as np


class Imagen:
    """Contenedor de imágenes RGB.

    Completen el constructor y los operadores de esta clase siguiendo el
    contrato del enunciado y los tests de ``tests/test_imagen.py``.
    """

    def __init__(self, img: np.ndarray) -> None:
        # Su código aquí
        if not isinstance(img, np.ndarray):
            raise TypeError(
                "Debes entregar un arreglo de numpy como argumento del constructor de Imagen."
            )
        if not img.ndim == 3:
            raise ValueError("3 dimensiones")
        if not img.shape[-1] == 3:
            raise ValueError("3 canales")
        self.imagen = img

    def __add__(self, other: int | float | np.ndarray | Imagen) -> Imagen:
        # Su código aquí

        other_value = other.imagen if isinstance(other, Imagen) else other

        other_shape = (
            other.imagen.shape
            if isinstance(other, Imagen)
            else (
                other.shape
                if isinstance(other, np.ndarray)
                else self.imagen.shape
            )
        )

        if self.imagen.shape != other_shape:
            raise ValueError("no calzan")

        new_other = self.imagen.copy() + other_value

        new_other = new_other.astype(int)

        new_other[new_other > 255] = 255
        new_other[new_other < 0] = 0

        new_imagen = Imagen(new_other)

        return new_imagen

    def __radd__(self, other: int | float | np.ndarray | Imagen) -> Imagen:
        return self.__add__(other)

    def __sub__(self, other: int | float | np.ndarray | Imagen) -> Imagen:
        # Su código aquí

        other_value = other.imagen if isinstance(other, Imagen) else other

        other_shape = (
            other.imagen.shape
            if isinstance(other, Imagen)
            else (
                other.shape
                if isinstance(other, np.ndarray)
                else self.imagen.shape
            )
        )

        if self.imagen.shape != other_shape:
            raise ValueError("no calzan")

        new_other = self.imagen.copy() - other_value

        new_other = new_other.astype(int)

        new_other[new_other > 255] = 255
        new_other[new_other < 0] = 0

        new_imagen = Imagen(new_other)

        return new_imagen

    def __rsub__(self, other: int | float | np.ndarray | Imagen) -> Imagen:
        # Su código aquí
        # Su código aquí

        other_value = other.imagen if isinstance(other, Imagen) else other

        other_shape = (
            other.imagen.shape
            if isinstance(other, Imagen)
            else (
                other.shape
                if isinstance(other, np.ndarray)
                else self.imagen.shape
            )
        )

        if self.imagen.shape != other_shape:
            raise ValueError("no calzan")

        new_other = other_value - self.imagen.copy()

        new_other = new_other.astype(int)

        new_other[new_other > 255] = 255
        new_other[new_other < 0] = 0

        new_imagen = Imagen(new_other)

        return new_imagen

        return

    def __mul__(self, other: int | float | np.ndarray | Imagen) -> Imagen:
        # Su código aquí

        other_value = other.imagen if isinstance(other, Imagen) else other

        other_shape = (
            other.imagen.shape
            if isinstance(other, Imagen)
            else (
                other.shape
                if isinstance(other, np.ndarray)
                else self.imagen.shape
            )
        )

        if self.imagen.shape != other_shape:
            raise ValueError("no calzan")

        new_other = self.imagen.copy() * other_value

        new_other = new_other.astype(int)

        new_other[new_other > 255] = 255
        new_other[new_other < 0] = 0

        new_imagen = Imagen(new_other)

        return new_imagen

    def __rmul__(self, other: int | float | np.ndarray | Imagen) -> Imagen:
        return self.__mul__(other)
