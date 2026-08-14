from sensores import Sensor


def contar_riesgos(sensores: list[Sensor], lecturas: dict[str, list[float]]):

    conteos: dict = {}
    for sensor in sensores:
        conteos[sensor.nombre] = 0
        for lectura in lecturas:
            if sensor.nombre == lectura:
                for valor in lecturas[lectura]:
                    if sensor.es_riesgo(valor):
                        conteos[sensor.nombre] += 1
    return conteos
