# coding=utf-8
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField

from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstWaarde import KeuzelijstWaarde


# Generated with OTLEnumerationCreator. To modify: extend, do not edit
class KlOrganisaties(KeuzelijstField):
    """De mogelijke organisaties."""
    naam = 'KlOrganisaties'
    label = 'Organisaties'
    objectUri = 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#KlOrganisaties'
    definition = 'De mogelijke organisaties.'
    status = 'https://wegenenverkeer-test.data.vlaanderen.be/id/concept/KlAdmsStatus/ingebruik'
    codelist = 'https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOrganisaties'
    options = {
        'AWV': KeuzelijstWaarde(invulwaarde='awv',
                                 label='AWV',
                                 status='ingebruik',
                                 definitie='Agentschap Wegen en Verkeer',
                                 objectUri='https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOrganisaties'
                                           '/awv'),
        'OTLMOW': KeuzelijstWaarde(invulwaarde='otlmow',
                                label='OTLMOW',
                                status='ingebruik',
                                definitie='The OTL MOW team',
                                objectUri='https://wegenenverkeer.data.vlaanderen.be/id/conceptscheme/KlOrganisaties/otlmow')
    }

    @classmethod
    def create_dummy_data(cls):
        return cls.create_dummy_data_keuzelijst(cls.options)

