# coding=utf-8
from ...Classes.ImplementatieElement.DirectioneleRelatie import DirectioneleRelatie


# Generated with OTLClassCreator. To modify: extend, do not edit
class Vergunt(DirectioneleRelatie):
    """Inname dat vergunt is in de innamevergunning."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#Vergunt'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()
