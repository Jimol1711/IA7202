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
        if (
            isinstance(other, Imagen)
            and not self.imagen.ndim == other.imagen.ndim
        ):
            raise ValueError("no calzan")

        if isinstance(other, float):
            other = int(other)

        new_other = np.zeros(self.imagen.shape, dtype="int64")

        return new_other

    def __radd__(self, other: int | float | np.ndarray | Imagen) -> Imagen:
        # Su código aquí
        raise NotImplementedError(
            "Completen __radd__ antes de ejecutar el programa."
        )

    def __sub__(self, other: int | float | np.ndarray | Imagen) -> Imagen:
        # Su código aquí
        raise NotImplementedError(
            "Completen __sub__ antes de ejecutar el programa."
        )

    def __rsub__(self, other: int | float | np.ndarray | Imagen) -> Imagen:
        # Su código aquí
        raise NotImplementedError(
            "Completen __rsub__ antes de ejecutar el programa."
        )

    def __mul__(self, other: int | float | np.ndarray | Imagen) -> Imagen:
        # Su código aquí
        raise NotImplementedError(
            "Completen __mul__ antes de ejecutar el programa."
        )

    def __rmul__(self, other: int | float | np.ndarray | Imagen) -> Imagen:
        # Su código aquí
        raise NotImplementedError(
            "Completen __rmul__ antes de ejecutar el programa."
        )
