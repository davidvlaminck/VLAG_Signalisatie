# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut
from otlmow_model.OtlmowModel.BaseClasses.OTLAsset import OTLAsset
from otlmow_model.OtlmowModel.BaseClasses.StringField import StringField


# Generated with OTLClassCreator. To modify: extend, do not edit
class Concept(OTLAsset):
    """TODO"""

    typeURI = 'http://www.w3.org/2004/02/skos/core#Concept'
    """De URI van het object volgens https://www.w3.org/2001/XMLSchema#anyURI."""

    def __init__(self):
        super().__init__()

        self.add_valid_relation(relation='https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#BehoortTot', target='http://www.w3.org/2004/02/skos/core#ConceptScheme', direction='u')  # u = unidirectional

        self._label = OTLAttribuut(field=StringField,
                                   naam='label',
                                   label='label',
                                   objectUri='http://www.w3.org/2004/02/skos/core#Concept.label',
                                   definition='TODO',
                                   owner=self)

    @property
    def label(self) -> str:
        """TODO"""
        return self._label.get_waarde()

    @label.setter
    def label(self, value):
        self._label.set_waarde(value, owner=self)
