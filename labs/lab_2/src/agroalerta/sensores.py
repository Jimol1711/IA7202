class Sensor:
    def __init__(
        self,
        nombre: str,
        unidad: str,
    ) -> None:
        self.nombre = nombre
        self.unidad = unidad

    def es_riesgo(self, valor: int) -> bool:
        return False


class SensorTemperatura(Sensor):
    def __init__(self, minimo: int, maximo: int) -> None:
        super().__init__("Temperatura", "°C")
        self.minimo = minimo
        self.maximo = maximo

    def es_riesgo(self, valor: int) -> bool:
        return valor < self.minimo or valor > self.maximo


class SensorViento(Sensor):
    def __init__(self, maximo: int):
        super().__init__("Viento", "km/h")
        self.maximo = maximo

    def es_riesgo(self, valor: int) -> bool:
        return valor > self.maximo


class SensorHumedad(Sensor):
    def __init__(self, maximo: int):
        super().__init__("humedad", "%")
        self.maximo = maximo

    def es_riesgo(self, valor: int) -> bool:
        return valor > self.maximo
