import datetime
from pathlib import Path

from VLAG_model.OtlmowModel.BaseClasses.OTLObject import OTLObject
from VLAG_model.OtlmowModel.Classes.Installatie.Verkeersbordopstelling import Verkeersbordopstelling
from VLAG_model.OtlmowModel.Classes.Mobiliteit.AanvullendReglementOntwerp import AanvullendReglementOntwerp
from VLAG_model.OtlmowModel.Classes.Mobiliteit.Mobiliteitsmaatregel import Mobiliteitsmaatregel
from VLAG_model.OtlmowModel.Classes.Mobiliteit.OntwerpVerkeersteken import OntwerpVerkeersteken
from VLAG_model.OtlmowModel.Classes.Mobiliteit.SignalisatieOntwerp import SignalisatieOntwerp
from VLAG_model.OtlmowModel.Classes.Mobiliteit.VerkeersbordVerkeersteken import VerkeersbordVerkeersteken
from VLAG_model.OtlmowModel.Classes.Mobiliteit.Verkeersbordconcept import Verkeersbordconcept
from VLAG_model.OtlmowModel.Classes.Onderdeel.BevatOntwerp import BevatOntwerp
from VLAG_model.OtlmowModel.Classes.Onderdeel.BevatOntwerpVoor import BevatOntwerpVoor
from VLAG_model.OtlmowModel.Classes.Onderdeel.BevatVerkeersteken import BevatVerkeersteken
from VLAG_model.OtlmowModel.Classes.Onderdeel.Bevestiging import Bevestiging
from VLAG_model.OtlmowModel.Classes.Onderdeel.HeeftAanzicht import HeeftAanzicht
from VLAG_model.OtlmowModel.Classes.Onderdeel.HeeftOntwerp import HeeftOntwerp
from VLAG_model.OtlmowModel.Classes.Onderdeel.HeeftVerkeersteken import HeeftVerkeersteken
from VLAG_model.OtlmowModel.Classes.Onderdeel.IsGebaseerdOp import IsGebaseerdOp
from VLAG_model.OtlmowModel.Classes.Onderdeel.Realiseert import Realiseert
from VLAG_model.OtlmowModel.Classes.Onderdeel.RetroreflecterendVerkeersbord import RetroreflecterendVerkeersbord
from VLAG_model.OtlmowModel.Classes.Onderdeel.RetroreflecterendeFolie import RetroreflecterendeFolie
from VLAG_model.OtlmowModel.Classes.Onderdeel.WordtAangeduidDoor import WordtAangeduidDoor
from VLAG_model.OtlmowModel.Helpers.RelationCreator import create_relation
from VLAG_model.OtlmowModel.Classes.Installatie.AanzichtVerkeersbordopstelling import AanzichtVerkeersbordopstelling
from VLAG_model.OtlmowModel.Classes.Onderdeel.HoortBij import HoortBij

from rdflib import Graph

from CustomRDFExporter import CustomRDFExporter


model_dir = Path(__file__).parent.parent / 'VLAG_model'

def return_graph_from_objects() -> Graph:
    """
    Create a Graph (rdflib) from a list of objects using a custom RDF exporter
    :return:
    """
    objects = create_objects()
    g = CustomRDFExporter(dotnotation_settings={'waarde_shortcut': False}).create_graph(list_of_objects=objects)
    return g

def add_versie_attributen(object: OTLObject) -> None:
    """
    Add version attributes to an object
    :param object: OTLObject
    :return: None
    """
    object.assetVersie.context = 'DA_Init'
    object.assetVersie.timestamp = datetime.datetime(2021, 1, 1)
    object.assetVersie.versienummer = 1
    object.isActief = True

def create_objects() -> [OTLObject]:
    """
    Generate a list of objects to be used in the test LDES
    :return: list of OTLObject
    """
    list_of_objects = []
    opstelling = Verkeersbordopstelling()
    opstelling.assetId.identificator = 'opstelling_01'
    add_versie_attributen(opstelling)
    opstelling.toestand = 'in-gebruik'
    opstelling.geometry = 'POINT Z (200000 200000 0)'
    list_of_objects.append(opstelling)

    aanzicht = AanzichtVerkeersbordopstelling()
    aanzicht.assetId.identificator = 'aanzicht_01'
    add_versie_attributen(aanzicht)
    aanzicht.toestand = 'in-gebruik'
    aanzicht.hoek = 1.0
    list_of_objects.append(aanzicht)

    aanzicht_opstelling = create_relation(source=opstelling, target=aanzicht, relation_type=HeeftAanzicht,
                                          model_directory=model_dir)
    add_versie_attributen(aanzicht_opstelling)
    list_of_objects.append(aanzicht_opstelling)

    bord = RetroreflecterendVerkeersbord()
    bord.assetId.identificator = 'bord_01'
    add_versie_attributen(bord)
    bord.toestand = 'in-ontwerp'
    bord.afmeting.rond.diameter.waarde = 600
    list_of_objects.append(bord)

    bord_aanzicht = create_relation(source=bord, target=aanzicht, relation_type=HoortBij, model_directory=model_dir)
    add_versie_attributen(bord_aanzicht)
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
    add_versie_attributen(folie)
    folie.toestand = 'in-gebruik'
    folie.folietype = 'folietype-3a'
    list_of_objects.append(folie)

    folie_bord = create_relation(source=bord, target=folie, relation_type=Bevestiging, model_directory=model_dir)
    add_versie_attributen(folie_bord)
    list_of_objects.append(folie_bord)

    teken = VerkeersbordVerkeersteken()
    teken.assetId.identificator = 'teken_01'
    add_versie_attributen(teken)
    list_of_objects.append(teken)

    bord_teken = create_relation(source=teken, target=bord, relation_type=Realiseert, model_directory=model_dir)
    add_versie_attributen(bord_teken)
    list_of_objects.append(bord_teken)

    concept = Verkeersbordconcept()
    concept.assetId.identificator = 'concept_01'
    add_versie_attributen(concept)
    concept.verkeersbordcode = 'C3'
    list_of_objects.append(concept)

    teken_concept = create_relation(source=teken, target=concept, relation_type=IsGebaseerdOp, model_directory=model_dir)
    add_versie_attributen(teken_concept)
    list_of_objects.append(teken_concept)

    aro = AanvullendReglementOntwerp()
    aro.assetId.identificator = 'aro_01'
    add_versie_attributen(aro)
    aro.naam = 'Aanvullend Reglement - Ontwerp'
    list_of_objects.append(aro)

    teken_aro = create_relation(source=aro, target=teken, relation_type=HeeftVerkeersteken, model_directory=model_dir)
    add_versie_attributen(teken_aro)
    list_of_objects.append(teken_aro)

    mobm = Mobiliteitsmaatregel()
    mobm.assetId.identificator = 'mobm_01'
    add_versie_attributen(mobm)
    mobm.zone[0].geometrie.wkt = 'POINT Z (200000 200000 0)'
    mobm.beschrijving = 'Mobiliteitsmaatregel'
    list_of_objects.append(mobm)

    mobm_teken = create_relation(source=mobm, target=teken, relation_type=WordtAangeduidDoor, model_directory=model_dir)
    add_versie_attributen(mobm_teken)
    list_of_objects.append(mobm_teken)

    aro_mobm = create_relation(source=aro, target=mobm, relation_type=BevatOntwerpVoor, model_directory=model_dir)
    add_versie_attributen(aro_mobm)
    list_of_objects.append(aro_mobm)

    sigo = SignalisatieOntwerp()
    sigo.assetId.identificator = 'sigo_01'
    add_versie_attributen(sigo)
    sigo.naam = 'Signalisatie Ontwerp'
    sigo.datum = datetime.datetime(2020, 6, 1)
    list_of_objects.append(sigo)

    sigo_aro = create_relation(source=sigo, target=aro, relation_type=BevatOntwerp, model_directory=model_dir)
    add_versie_attributen(sigo_aro)
    list_of_objects.append(sigo_aro)

    o_teken = OntwerpVerkeersteken()
    o_teken.assetId.identificator = 'o_teken_01'
    add_versie_attributen(o_teken)
    list_of_objects.append(o_teken)

    sigo_teken = create_relation(source=sigo, target=o_teken, relation_type=BevatVerkeersteken, model_directory=model_dir)
    add_versie_attributen(sigo_teken)
    list_of_objects.append(sigo_teken)

    # missing in model
    # oteken_teken = create_relation(source=teken, target=o_teken, relation_type=HeeftOntwerp, model_directory=model_dir)
    # add_versie_attributen(oteken_teken)
    # list_of_objects.append(oteken_teken)

    return list_of_objects
