from src.agroalerta.reporte import contar_riesgos
from src.agroalerta.sensores import (
    SensorHumedad,
    SensorTemperatura,
    SensorViento,
)


def test_SensorTemperatura():
    sensor_temp = SensorTemperatura(_minimo=0, _maximo=40)
    assert sensor_temp.nombre == "temperatura"
    assert sensor_temp.unidad == "°C"
    assert sensor_temp._maximo == 40
    assert sensor_temp._minimo == 0
    assert not sensor_temp.es_riesgo(20)
    assert sensor_temp.es_riesgo(-10)
    assert sensor_temp.es_riesgo(60)


def test_SensorHumedad():
    sensor_humedad = SensorHumedad(_maximo=85)
    assert sensor_humedad.nombre == "humedad"
    assert sensor_humedad.unidad == "%"
    assert sensor_humedad._maximo == 85
    assert not sensor_humedad.es_riesgo(20)
    assert sensor_humedad.es_riesgo(90)


def test_SensorViento():
    sensor_viento = SensorViento(_maximo=25)
    assert sensor_viento.nombre == "viento"
    assert sensor_viento.unidad == "km/h"
    assert sensor_viento._maximo == 25
    assert not sensor_viento.es_riesgo(20)
    assert sensor_viento.es_riesgo(90)


def test_contar_riesgos():
    sensor_temp = SensorTemperatura(_minimo=0, _maximo=40)
    sensor_humedad = SensorHumedad(_maximo=85)
    sensor_viento = SensorViento(_maximo=25)
    sensores = [sensor_temp, sensor_humedad, sensor_viento]
    lecturas = {
        "temperatura": [2.1, -1.2],
        "humedad": [80, 90],
        "viento": [10, 30],
    }

    resultado = contar_riesgos(sensores, lecturas)
    assert resultado == {"temperatura": 1, "humedad": 1, "viento": 1}
