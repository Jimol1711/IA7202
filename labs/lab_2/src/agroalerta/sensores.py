from abc import ABC, abstractmethod


class Sensor(ABC):
    def __init__(
        self,
        nombre: str,
        unidad: str,
    ) -> None:
        self.nombre = nombre
        self.unidad = unidad

    @abstractmethod
    def es_riesgo(self, valor: int) -> bool:
        return False


class SensorTemperatura(Sensor):
    def __init__(
        self,
        _minimo: int,
        _maximo: int,
    ) -> None:
        super().__init__("Temperatura", "°C")
        self._minimo = _minimo
        self._maximo = _maximo

    def es_riesgo(self, valor: int) -> bool:
        return valor < self._minimo or valor > self._maximo


class SensorViento(Sensor):
    def __init__(
        self,
        _maximo: int,
    ) -> None:
        super().__init__("Viento", "km/h")
        self._maximo = _maximo

    def es_riesgo(self, valor: int) -> bool:
        return valor > self._maximo


class SensorHumedad(Sensor):
    def __init__(
        self,
        _maximo: int,
    ) -> None:
        super().__init__("humedad", "%")
        self._maximo = _maximo

    def es_riesgo(self, valor: int) -> bool:
        return valor > self._maximo
