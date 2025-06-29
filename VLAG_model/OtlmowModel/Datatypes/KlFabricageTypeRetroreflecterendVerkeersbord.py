# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlFabricageTypeRetroreflecterendVerkeersbord(KeuzelijstField):
    """TODO"""
    naam = 'KlFabricageTypeRetroreflecterendVerkeersbord'
    label = 'Fabricage type retroreflecterend verkeersbord'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#KlFabricageTypeRetroreflecterendVerkeersbord'
    definition = 'TODO'
    status = 'ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlFabricageTypeRetroreflecterendVerkeersbord'
    options = {
        'testreferentie-rrvkb-type': KeuzelijstWaarde(invulwaarde='testreferentie-rrvkb-type',
                                                      label='testreferentie RRVKB type',
                                                      status='ingebruik',
                                                      definitie='testreferentie RRVKB type',
                                                      objectUri='https://wegenenverkeer.data.vlaanderen.be/id/concept/KlFabricageTypeRetroreflecterendVerkeersbord/testreferentie-rrvkb-type')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

