# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class IsOntwerpVoor(DirectioneleRelatie):
    """Mobiliteitsmaatregel die deel uitmaakt van het ontwerp"""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#IsOntwerpVoor'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
