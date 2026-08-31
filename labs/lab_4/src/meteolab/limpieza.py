"""Funciones para revisar nulos y claves temporales."""

from __future__ import annotations

import polars as pl

from src.meteolab.constantes import Tabla


def resumen_de_nulos(temperaturas: pl.DataFrame) -> pl.DataFrame:
    """Devuelve conteos y porcentajes de nulos por columna."""
    n = temperaturas.height
    return pl.DataFrame(
        {
            "columna": temperaturas.columns,
            "nulos": [
                temperaturas[col].null_count() for col in temperaturas.columns
            ],
            "porcentaje": [
                temperaturas[col].null_count() / n
                for col in temperaturas.columns
            ],
        }
    )


def claves_repetidas(temperaturas: Tabla) -> Tabla:
    """Cuenta repeticiones de país, año y periodo."""
    return (
        temperaturas.group_by(["country", "year", "period"])
        .len()
        .filter(pl.col("len") > 1)
    )


def limpiar_temperaturas(temperaturas: Tabla) -> Tabla:
    """Conserva el contrato de periodos y los nulos válidos."""
    meses = [
        "JAN",
        "FEB",
        "MAR",
        "APR",
        "MAY",
        "JUN",
        "JUL",
        "AUG",
        "SEP",
        "OCT",
        "NOV",
        "DEC",
    ]

    return temperaturas.filter(
        (pl.col("period").is_in(meses))
        & (pl.col("temperature_c").is_not_null())
    )
