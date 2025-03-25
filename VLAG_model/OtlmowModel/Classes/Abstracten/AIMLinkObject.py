# coding=utf-8
from abc import abstractmethod
from ...Classes.ImplementatieElement.AIMObject import AIMObject


# Generated with OTLClassCreator. To modify: extend, do not edit
class AIMLinkObject(AIMObject):
    """Abstracte voor de relaties met AIMObject te linken."""

    typeURI = 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#AIMLinkObject'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    @abstractmethod
    def __init__(self):
        super().__init__()
