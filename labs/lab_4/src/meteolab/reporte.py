"""Pipelines lazy para analizar únicamente temperaturas mensuales."""

from __future__ import annotations

from pathlib import Path

import polars as pl

from src.meteolab.constantes import ESQUEMA_CRU, PAISES_COMPARACION, RUTA_CSV
from src.meteolab.derivadas import agregar_fecha_mensual
from src.meteolab.limpieza import limpiar_temperaturas
from src.meteolab.metricas import (
    anomalias_mensuales,
    resumen_anual_desde_mensuales,
    resumen_mensual,
)


def pipeline_mensual(
    ruta: Path = RUTA_CSV,
    paises: list[str] | tuple[str, ...] = PAISES_COMPARACION,
) -> pl.LazyFrame:
    """Construye el flujo mensual sin ejecutarlo."""
    consulta = pl.scan_csv(
        ruta,
        schema_overrides=ESQUEMA_CRU,
    )

    consulta = limpiar_temperaturas(consulta)

    consulta = consulta.filter(pl.col("iso_alpha3").is_in(paises))

    consulta = agregar_fecha_mensual(consulta)

    return consulta.sort(["iso_alpha3", "fecha"])


def pipeline_resumen_mensual(
    ruta: Path = RUTA_CSV,
    paises: list[str] | tuple[str, ...] = PAISES_COMPARACION,
) -> pl.LazyFrame:
    """Construye la climatología mensual."""
    mensuales = pipeline_mensual(ruta, paises)

    return resumen_mensual(mensuales)


def pipeline_resumen_anual(
    ruta: Path = RUTA_CSV,
    paises: list[str] | tuple[str, ...] = PAISES_COMPARACION,
) -> pl.LazyFrame:
    """Calcula medias anuales desde meses limpios."""
    mensuales = pipeline_mensual(ruta, paises)

    return resumen_anual_desde_mensuales(mensuales)


def pipeline_anomalias(
    ruta: Path = RUTA_CSV,
    paises: list[str] | tuple[str, ...] = PAISES_COMPARACION,
    umbral: float = 2.0,
) -> pl.LazyFrame:
    """Construye el flujo de anomalías mensuales."""
    mensuales = pipeline_mensual(ruta, paises)

    return anomalias_mensuales(
        mensuales,
        umbral=umbral,
    )


def ejecutar_reporte(
    ruta: Path = RUTA_CSV,
    paises: list[str] | tuple[str, ...] = PAISES_COMPARACION,
) -> pl.DataFrame:
    """Materializa la climatología mensual."""
    return pipeline_resumen_mensual(
        ruta,
        paises,
    ).collect()


def plan_de_ejecucion(
    ruta: Path = RUTA_CSV,
    paises: list[str] | tuple[str, ...] = PAISES_COMPARACION,
    optimizado: bool = True,
) -> str:
    """Devuelve el plan lazy como texto."""
    return pipeline_resumen_mensual(
        ruta,
        paises,
    ).explain(optimized=optimizado)
