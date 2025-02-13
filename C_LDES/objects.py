import datetime

from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLObject
from otlmow_model.OtlmowModel.Classes.Installatie.Verkeersbordopstelling import Verkeersbordopstelling
from otlmow_model.OtlmowModel.Classes.Onderdeel.HoortBij import HoortBij
from otlmow_model.OtlmowModel.Classes.Onderdeel.RetroreflecterendVerkeersbord import RetroreflecterendVerkeersbord
from otlmow_model.OtlmowModel.Helpers.RelationCreator import create_relation
from rdflib import Graph

from CustomRDFExporter import CustomRDFExporter


def return_graph_from_objects() -> Graph:
    """
    Create a Graph (rdflib) from a list of objects using a custom RDF exporter
    :return:
    """
    objects = create_objects()
    g = CustomRDFExporter(dotnotation_settings={'waarde_shortcut': False}).create_graph(list_of_objects=objects)
    return g

def create_objects() -> [OTLObject]:
    """
    Generate a list of objects to be used in the test LDES
    :return: list of OTLObject
    """
    list_of_objects = []
    opstelling = Verkeersbordopstelling()
    opstelling.assetId.identificator = 'opstelling_01'
    opstelling.assetVersie.context = 'DA_Init'
    opstelling.assetVersie.timestamp = datetime.datetime(2021, 1, 1)
    opstelling.assetVersie.versienummer = 1
    opstelling.isActief = True
    opstelling.toestand = 'in-gebruik'
    opstelling.geometry = 'POINT Z (200000 200000 0)'
    list_of_objects.append(opstelling)

    bord = RetroreflecterendVerkeersbord()
    bord.assetId.identificator = 'bord_01'
    bord.assetVersie.context = 'DA_Init'
    bord.assetVersie.timestamp = datetime.datetime(2021, 1, 1)
    bord.assetVersie.versienummer = 1
    bord.isActief = True
    bord.toestand = 'in-ontwerp'
    bord.afmeting.rond.diameter.waarde = 600
    list_of_objects.append(bord)

    bord_opstelling = create_relation(source=bord, target=opstelling, relation_type=HoortBij)
    bord_opstelling.assetVersie.context = 'DA_Init'
    bord_opstelling.assetVersie.timestamp = datetime.datetime(2021, 1, 1)
    bord_opstelling.assetVersie.versienummer = 1
    list_of_objects.append(bord_opstelling)

    bordv2 = RetroreflecterendVerkeersbord()
    bordv2.assetId.identificator = 'bord_01'
    bordv2.assetVersie.context = 'DA_Init'
    bordv2.assetVersie.timestamp = datetime.datetime(2025, 2, 2)
    bordv2.assetVersie.versienummer = 2
    bordv2.isActief = True
    bordv2.toestand = 'in-gebruik'
    bordv2.opstelhoogte.waarde = 1.8
    bordv2.afmeting.rond.diameter.waarde = 600
    list_of_objects.append(bordv2)

    return list_of_objects
