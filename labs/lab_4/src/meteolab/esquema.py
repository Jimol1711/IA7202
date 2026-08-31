"""Funciones para declarar y validar el esquema CRU."""

from __future__ import annotations

import pandera.polars as pa
import polars as pl

from src.meteolab.constantes import PERIODOS_VALIDOS

ESQUEMA_TEMPERATURAS = pa.DataFrameSchema(
    {
        "country": pa.Column(pl.String),
        "iso_alpha2": pa.Column(pl.String),
        "iso_alpha3": pa.Column(pl.String),
        "year": pa.Column(
            pl.Int64, pa.Check.in_range(min_value=1901, max_value=2025)
        ),
        "period": pa.Column(pl.String, pa.Check.isin(PERIODOS_VALIDOS)),
        "temperature_c": pa.Column(pl.Float64, nullable=True),
        "parameter": pa.Column(
            pl.String, pa.Check.equal_to("Mean Temperature")
        ),
        "units": pa.Column(pl.String, pa.Check.equal_to("degrees Celsius")),
        "source_file": pa.Column(pl.String),
    }
)


def comparar_esquema(temperaturas: pl.DataFrame) -> list[str]:
    """Devuelve diferencias entre el esquema real y el esperado."""
    diferencias: list[str] = []

    columnas_esperadas = ESQUEMA_TEMPERATURAS.columns
    columnas_reales = temperaturas.schema

    for nombre, columna_esperada in columnas_esperadas.items():
        if nombre not in columnas_reales:
            diferencias.append(nombre)
            continue

        dtype_esperado = columna_esperada.dtype.type
        dtype_real = columnas_reales[nombre]

        if dtype_real != dtype_esperado:
            diferencias.append(nombre)

    return diferencias


def validar_esquema(temperaturas: pl.DataFrame) -> None:
    """Comprueba los nombres y tipos de las columnas."""
    columnas_esperadas = ESQUEMA_TEMPERATURAS.columns
    columnas_reales = temperaturas.schema

    for nombre, columna_esperada in columnas_esperadas.items():
        if nombre not in columnas_reales:
            raise ValueError(nombre)

        dtype_esperado = columna_esperada.dtype.type
        dtype_real = columnas_reales[nombre]

        if dtype_real != dtype_esperado:
            raise ValueError(nombre)


def validar_datos(temperaturas: pl.DataFrame) -> pl.DataFrame:
    """Valida tipos, periodos, unidades y valores faltantes."""
    try:
        return ESQUEMA_TEMPERATURAS.validate(temperaturas, lazy=True)
    except pa.errors.SchemaErrors as err:
        indices_invalidos = (
            err.failure_cases.get_column("index")
            .drop_nulls()
            .unique()
            .to_list()
        )
        return (
            temperaturas.with_row_index("indices")
            .filter(~pl.col("indices").is_in(indices_invalidos))
            .drop("indices")
        )


def casos_que_fallan(temperaturas: pl.DataFrame) -> pl.DataFrame:
    """Devuelve los incumplimientos sin ocultar sus columnas."""
    try:
        ESQUEMA_TEMPERATURAS.validate(temperaturas, lazy=True)
    except pa.errors.SchemaErrors as err:
        return err.failure_cases

    return temperaturas.clear()
