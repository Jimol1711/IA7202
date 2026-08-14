import argparse
from pathlib import Path

from src.agroalerta.datos import cargar_lecturas
from src.agroalerta.reporte import contar_riesgos
from src.agroalerta.sensores import (
    SensorHumedad,
    SensorTemperatura,
    SensorViento,
)

RUTA_LECTURAS = Path(__file__).parent / "data" / "lecturas.csv"


def main() -> None:
    parser = argparse.ArgumentParser(description="AgroAlerta")
    parser.add_argument("--fecha", default="2026-06-15")
    args = parser.parse_args()

    sensores = [
        SensorTemperatura(0, 40),
        SensorViento(25),
        SensorHumedad(85),
    ]
    lecturas = cargar_lecturas(RUTA_LECTURAS, args.fecha)
    conteos = contar_riesgos(sensores, lecturas)

    print(f"Estación Parcela Norte — {args.fecha}")
    for sensor in sensores:
        print(
            f"{sensor.nombre.capitalize():<15}{conteos[sensor.nombre]} lecturas en riesgo"
        )

    print(f"\nTotal: {sum(conteos.values())} situaciones de riesgo")


if __name__ == "__main__":
    main()
