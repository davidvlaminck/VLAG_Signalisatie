from typing import Iterable

from otlmow_model.OtlmowModel.BaseClasses.FloatOrDecimalField import FloatOrDecimalField
from otlmow_model.OtlmowModel.BaseClasses.KeuzelijstField import KeuzelijstField
from otlmow_model.OtlmowModel.BaseClasses.OTLObject import OTLObject
from otlmow_model.OtlmowModel.Helpers.OTLObjectHelper import is_relation
from rdflib import Graph, FOAF, URIRef, RDF, BNode, Literal, XSD

from VLAG_model.OtlmowModel.BaseClasses.OTLObject import OTLAttribuut


class CustomRDFExporter:
    def __init__(self, dotnotation_settings: dict = None):
        """
        Create a new RDFExporter with the given settings for dotnotation
        :param dotnotation_settings: dict
        """
        if dotnotation_settings is None:
            dotnotation_settings = {}
        self.settings = dotnotation_settings

        for required_attribute in ['waarde_shortcut']:
            if required_attribute not in self.settings:
                raise ValueError("The settings are not loaded or don't contain the full dotnotation settings")

    def create_graph(self, list_of_objects: Iterable = None) -> Graph:
        g = Graph()
        for ns, namespace in {'foaf': FOAF,
                              'imel': 'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#',
                              'asset': 'https://data.awvvlaanderen.be/id/asset/',
                              'assetrelatie': 'https://data.awvvlaanderen.be/id/assetrelatie/',
                              'onderdeel': 'https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#',
                              'installatie': 'https://wegenenverkeer.data.vlaanderen.be/ns/installatie#',
                              'keuzelijst': 'https://wegenenverkeer.data.vlaanderen.be/id/concept/',
                              'abs': 'https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#',
                              'pem': 'https://wegenenverkeer.data.vlaanderen.be/ns/proefenmeting#',
                              'loc': 'https://loc.data.wegenenverkeer.be/ns/implementatieelement#'}.items():
            g.bind(ns, namespace)

        for instance in list_of_objects:
            if instance.assetId is None or instance.assetId.identificator is None or \
                    instance.assetId.identificator == '':
                raise ValueError('Can not export assets without a valid assetId')

            if not hasattr(instance, 'typeURI') or instance.typeURI is None or instance.typeURI == '':
                raise ValueError(f'Can not export invalid objects: {instance}')

            asset_uri = 'https://data.awvvlaanderen.be/id/asset/' + instance.assetId.identificator
            versioned_uri = asset_uri
            if instance.assetVersie is not None and instance.assetVersie.versienummer is not None:
                versioned_uri += f'/v{instance.assetVersie.versienummer}'
            asset = URIRef(versioned_uri)
            type_node = URIRef(instance.typeURI)
            g.add((asset, RDF.type, type_node))

            if is_relation(instance):
                g.add((asset,
                       URIRef('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject.bron'),
                       URIRef(asset_uri)))
                g.add((asset,
                       URIRef('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#RelatieObject.doel'),
                       URIRef(asset_uri)))
                instance.bronAssetId = None
                instance.doelAssetId = None
                instance.bron = None
                instance.doel = None

            self._add_attributes_to_graph(graph=g, asset_or_attribute=instance, asset_attribute_ref=asset)

        return g

    def _add_attributes_to_graph(self, graph: Graph, asset_or_attribute: [OTLAttribuut | OTLObject],
                                 asset_attribute_ref: [URIRef | BNode]) -> None:
        """
        Recursively add attributes to the graph
        :param graph: The graph to add the attributes to
        :param asset_or_attribute: The object to add the attributes from
        :param asset_attribute_ref: The reference to the object in the graph
        :return: None
        """
        for attribute in asset_or_attribute:
            if attribute.waarde is None:
                continue

            if attribute.field.waardeObject is not None:
                if attribute.kardinaliteit_max != '1':
                    for waarde_item in attribute.waarde:
                        waarde_object = BNode()
                        graph.add((asset_attribute_ref, URIRef(attribute.objectUri), waarde_object))
                        self._add_attributes_to_graph(graph=graph, asset_or_attribute=waarde_item,
                                                      asset_attribute_ref=waarde_object)
                else:
                    waarde_object = BNode()
                    graph.add((asset_attribute_ref, URIRef(attribute.objectUri), waarde_object))
                    self._add_attributes_to_graph(graph=graph, asset_or_attribute=attribute.waarde,
                                                  asset_attribute_ref=waarde_object)
                continue

            if attribute.kardinaliteit_max != '1':
                for waarde_item in attribute.waarde:
                    if waarde_item is not None and issubclass(attribute.field, KeuzelijstField):
                        graph.add((asset_attribute_ref, URIRef(attribute.objectUri),
                                   URIRef(attribute.field.options[waarde_item].objectUri)))
                    elif issubclass(attribute.field, FloatOrDecimalField):
                        graph.add((asset_attribute_ref, URIRef(attribute.objectUri), Literal(waarde_item, datatype=XSD.decimal)))
                    else:
                        graph.add((asset_attribute_ref, URIRef(attribute.objectUri), Literal(waarde_item)))
            else:
                if issubclass(attribute.field, KeuzelijstField):
                    graph.add((asset_attribute_ref, URIRef(attribute.objectUri),
                               URIRef(attribute.field.options[attribute.waarde].objectUri)))
                elif issubclass(attribute.field, FloatOrDecimalField):
                    graph.add((asset_attribute_ref, URIRef(attribute.objectUri), Literal(attribute.waarde, datatype=XSD.decimal)))
                else:
                    graph.add((asset_attribute_ref, URIRef(attribute.objectUri), Literal(attribute.waarde)))
