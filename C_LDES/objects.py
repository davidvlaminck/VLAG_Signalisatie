import datetime
from pathlib import Path

from VLAG_model.OtlmowModel.BaseClasses.OTLObject import OTLObject
from VLAG_model.OtlmowModel.Classes.Installatie.Verkeersbordopstelling import Verkeersbordopstelling
from VLAG_model.OtlmowModel.Classes.Mobiliteit.VerkeersbordVerkeersteken import VerkeersbordVerkeersteken
from VLAG_model.OtlmowModel.Classes.Onderdeel.Bevestiging import Bevestiging
from VLAG_model.OtlmowModel.Classes.Onderdeel.HeeftAanzicht import HeeftAanzicht
from VLAG_model.OtlmowModel.Classes.Onderdeel.Realiseert import Realiseert
from VLAG_model.OtlmowModel.Classes.Onderdeel.RetroreflecterendVerkeersbord import RetroreflecterendVerkeersbord
from VLAG_model.OtlmowModel.Classes.Onderdeel.RetroreflecterendeFolie import RetroreflecterendeFolie
from VLAG_model.OtlmowModel.Helpers.RelationCreator import create_relation
from rdflib import Graph

from CustomRDFExporter import CustomRDFExporter
from VLAG_model.OtlmowModel.Classes.Installatie.AanzichtVerkeersbordopstelling import AanzichtVerkeersbordopstelling
from VLAG_model.OtlmowModel.Classes.Onderdeel.HoortBij import HoortBij


model_dir = Path(__file__).parent.parent / 'VLAG_model'

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

    aanzicht = AanzichtVerkeersbordopstelling()
    aanzicht.assetId.identificator = 'aanzicht_01'
    aanzicht.assetVersie.context = 'DA_Init'
    aanzicht.assetVersie.timestamp = datetime.datetime(2021, 1, 1)
    aanzicht.assetVersie.versienummer = 1
    aanzicht.isActief = True
    aanzicht.toestand = 'in-gebruik'
    aanzicht.hoek = 1.0
    list_of_objects.append(aanzicht)

    aanzicht_opstelling = create_relation(source=opstelling, target=aanzicht, relation_type=HeeftAanzicht,
                                          model_directory=model_dir)

    aanzicht_opstelling.assetVersie.context = 'DA_Init'
    aanzicht_opstelling.assetVersie.timestamp = datetime.datetime(2021, 1, 1)
    aanzicht_opstelling.assetVersie.versienummer = 1
    list_of_objects.append(aanzicht_opstelling)

    bord = RetroreflecterendVerkeersbord()
    bord.assetId.identificator = 'bord_01'
    bord.assetVersie.context = 'DA_Init'
    bord.assetVersie.timestamp = datetime.datetime(2021, 1, 1)
    bord.assetVersie.versienummer = 1
    bord.isActief = True
    bord.toestand = 'in-ontwerp'
    bord.afmeting.rond.diameter.waarde = 600
    list_of_objects.append(bord)

    bord_aanzicht = create_relation(source=bord, target=aanzicht, relation_type=HoortBij, model_directory=model_dir)
    bord_aanzicht.assetVersie.context = 'DA_Init'
    bord_aanzicht.assetVersie.timestamp = datetime.datetime(2021, 1, 1)
    bord_aanzicht.assetVersie.versienummer = 1
    list_of_objects.append(bord_aanzicht)

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

    folie = RetroreflecterendeFolie()
    folie.assetId.identificator = 'folie_01'
    folie.assetVersie.context = 'DA_Init'
    folie.assetVersie.timestamp = datetime.datetime(2021, 1, 1)
    folie.assetVersie.versienummer = 1
    folie.isActief = True
    folie.toestand = 'in-gebruik'
    folie.folietype = 'folietype-3a'
    list_of_objects.append(folie)

    folie_bord = create_relation(source=bord, target=folie, relation_type=Bevestiging, model_directory=model_dir)
    folie_bord.assetVersie.context = 'DA_Init'
    folie_bord.assetVersie.timestamp = datetime.datetime(2021, 1, 1)
    folie_bord.assetVersie.versienummer = 1
    list_of_objects.append(folie_bord)

    teken = VerkeersbordVerkeersteken()
    teken.assetId.identificator = 'teken_01'
    teken.assetVersie.context = 'DA_Init'
    teken.assetVersie.timestamp = datetime.datetime(2021, 1, 1)
    teken.assetVersie.versienummer = 1
    teken.isActief = True
    teken.toestand = 'in-gebruik'
    list_of_objects.append(teken)

    bord_teken = create_relation(source=teken, target=bord, relation_type=Realiseert, model_directory=model_dir)
    bord_teken.assetVersie.context = 'DA_Init'
    bord_teken.assetVersie.timestamp = datetime.datetime(2021, 1, 1)
    bord_teken.assetVersie.versienummer = 1
    list_of_objects.append(bord_teken)

    return list_of_objects
