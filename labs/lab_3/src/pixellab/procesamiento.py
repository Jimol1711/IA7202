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
        brightness[brightness > 255] = 255
        brightness[brightness < 0] = 0
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
            og_img[og_img[..., :] > 255] = 255
            og_img[og_img[..., :] < 0] = 0
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
        is_axis_h = axis == "h"
        is_axis_v = axis == "v"
        img_out = img_in.imagen.copy()
        img_out[img_out[..., :] > 255] = 255
        img_out[img_out[..., :] < 0] = 0
        if is_axis_h:
            img_out = img_out[:, ::-1, ...]
            return Imagen(img_out.astype(int))
        elif is_axis_v:
            img_out = img_out[::-1, ...]
            return Imagen(img_out.astype(int))
        else:
            raise ValueError(
                "Eje 'x' no válido. Valores posibles: 'h' (horizontal) o 'v' (vertical)."
            )

    def set_saturation(self, img_in: Imagen, C: float) -> Imagen:
        gris = self.to_gray(img_in)
        R = gris + C * (img_in - gris)
        R.imagen[R.imagen[..., :] > 255] = 255
        R.imagen[R.imagen[..., :] < 0] = 0
        R.imagen = R.imagen.astype(int)
        return R

    def set_contrast(self, img_in: Imagen, C: float) -> Imagen:
        F = 259 * (C + 255) / (255 * (259 - C))
        R = F * (img_in.imagen - 128) + 128

        R[R > 255] = 255
        R[R < 0] = 0

        return Imagen(R.astype(int))

    def conv_channel(self, img_in: Imagen, kernel: np.ndarray) -> Imagen:
        """Aplica una convolución bidimensional a cada canal de una imagen.

        La convolución desplaza el kernel sobre cada canal RGB y reemplaza
        cada píxel por la suma ponderada de sus píxeles vecinos. El resultado
        conserva las dimensiones originales, usa una extensión simétrica en
        los bordes y limita las intensidades al intervalo [0, 255].

        Args:
            img_in: Imagen RGB cuyos canales se procesarán.
            kernel: Matriz bidimensional de pesos que define el filtro.

        Returns:
            Una nueva imagen, con valores enteros, resultante de aplicar el
            kernel de forma independiente a cada canal.
        """
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
