# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlZonaliteit(KeuzelijstField):
    """TODO"""
    naam = 'KlZonaliteit'
    label = 'Zonaliteit'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlZonaliteit'
    definition = 'TODO'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlZonaliteit'
    options = {
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

