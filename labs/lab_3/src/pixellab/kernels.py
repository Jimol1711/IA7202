"""Kernels de convolución que deben definir para la Etapa 6."""

import numpy as np

KERNELS: list[tuple[str, np.ndarray]] = [
    # Mantiene la imagen sin cambios.
    ("Identidad", np.array([[0, 0, 0], [0, 1, 0], [0, 0, 0]])),
    # Detecta bordes mediante el operador laplaciano.
    ("Laplaciano", np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])),
    # Resalta los detalles y bordes de la imagen.
    ("Enfoque", np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])),
    # Suaviza la imagen promediando los píxeles vecinos.
    (
        "Desenfoque",
        np.array(
            [
                [1 / 16, 1 / 8, 1 / 16],
                [1 / 8, 1 / 4, 1 / 8],
                [1 / 16, 1 / 8, 1 / 16],
            ]
        ),
    ),
    # Produce un efecto de relieve resaltando cambios de intensidad.
    ("Relieve", np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])),
]
