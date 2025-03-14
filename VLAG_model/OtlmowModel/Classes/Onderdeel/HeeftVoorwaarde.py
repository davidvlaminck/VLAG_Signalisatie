# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class HeeftVoorwaarde(DirectioneleRelatie):
    """Bevat de voorwaarde van de legale verschijningsvorm."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#HeeftVoorwaarde'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
