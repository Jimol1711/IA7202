"""Operaciones de procesamiento de imágenes para completar."""

from __future__ import annotations

import numpy as np
from scipy.signal import convolve2d

from src.pixellab.imagen import Imagen


class LibImagen:
    """Filtros y transformaciones que reciben y retornan ``Imagen``."""

    def to_negative(self, img_in: Imagen) -> Imagen:
        img_out = 255 - img_in
        img_out.imagen = img_out.imagen.astype(int)
        return img_out

    def to_gray(self, img_in: Imagen) -> Imagen:
        value_red_channel = img_in.imagen[..., :, 0]
        value_green_channel = img_in.imagen[..., :, 1]
        value_blue_channel = img_in.imagen[..., :, 2]
        brightness = (
            0.299 * value_red_channel
            + 0.587 * value_green_channel
            + 0.114 * value_blue_channel
        )
        channel_brightness = np.stack(
            (brightness, brightness, brightness), axis=-1
        )
        final_img = img_in.imagen.copy()
        final_img[..., :, :] = channel_brightness
        return Imagen(final_img.astype(int))

    def get_channel(self, img_in: Imagen, channel: str) -> Imagen:
        is_channel_r = channel == "r"
        is_channel_g = channel == "g"
        is_channel_b = channel == "b"

        if is_channel_r or is_channel_b or is_channel_g:
            og_img = img_in.imagen.copy()
            num_channel = 0 if is_channel_r else (1 if is_channel_g else 2)
            indexes = [0, 1, 2]
            indexes = [i for i in indexes if i != num_channel]
            for i in indexes:
                og_img[..., :, i] = np.zeros(og_img[..., :, i].shape)
            return Imagen(og_img.astype(int))
        else:
            raise ValueError(
                "Canal 'x' no válido. Valores posibles: 'r', 'g' o 'b'."
            )

    def flip(self, img_in: Imagen, axis: str) -> Imagen:
        # Su código aquí
        raise NotImplementedError(
            "Completen flip antes de ejecutar el programa."
        )

    def set_saturation(self, img_in: Imagen, C: float) -> Imagen:
        # Su código aquí
        raise NotImplementedError(
            "Completen set_saturation antes de ejecutar el programa."
        )

    def set_contrast(self, img_in: Imagen, C: float) -> Imagen:
        # Su código aquí
        raise NotImplementedError(
            "Completen set_contrast antes de ejecutar el programa."
        )

    def conv_channel(self, img_in: Imagen, kernel: np.ndarray) -> Imagen:
        """Por documentar (esto es parte del trabajo de la Etapa 6)."""
        # El cuerpo de este método lo entrega el curso.
        img = img_in.imagen
        img_out = []
        for i in range(img.shape[-1]):
            img_channel = convolve2d(
                img[:, :, i], kernel, mode="same", boundary="symm"
            )
            img_out.append(img_channel)
        new_image = np.stack(img_out, axis=2)
        new_image[new_image > 255], new_image[new_image < 0] = 255, 0
        return Imagen(new_image.astype(int))
