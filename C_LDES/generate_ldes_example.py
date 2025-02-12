from pathlib import Path

from rdflib import Graph, URIRef, Dataset, RDF, Literal, XSD, Namespace
from rdflib.namespace import GEO

import objects

current_dir = Path(__file__).parent

class LDESServer:
    def __init__(self, source_path: Path):
        self.source_path = source_path
        self.g: Graph | None = None
        self.load()

    def load(self):
        self.g: Graph = Graph()
        self.g.parse(source=self.source_path, format='ttl')

        # timestamp_triples = [q for q in self.g.triples(
        #     (None, URIRef('https://www.w3.org/TR/prov-o/#generatedAtTime'), None))]

        base_ldes = self.create_ldes_fragment_from_partial_set(self.g)


    @staticmethod
    def print_graph(graph: Graph):
        for s, p, o in graph:
            print(f'{s} {p} {o}')

    @staticmethod
    def print_dataset(dataset: Dataset):
        for s, p, o, c in dataset:
            print(f'{s} {p} {o} {c}')

    def create_ldes_fragment_from_partial_set(self, graph_data: Graph):
        g = Graph()
        g.bind('ldes', 'https://w3id.org/ldes#')
        g.bind('tree', 'https://w3id.org/tree#')
        g.bind('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
        g.bind('sh', 'http://www.w3.org/ns/shacl#')
        g.bind('xsd', 'http://www.w3.org/2001/XMLSchema#')
        g.bind('hydra', 'http://www.w3.org/ns/hydra/core#')
        g.bind('dct', 'http://purl.org/dc/terms/')
        g.bind('locn', 'http://www.w3.org/ns/locn#')
        g.bind('asset', Namespace('https://data.awvvlaanderen.be/id/asset/'))
        g.bind('installatie', Namespace('https://wegenenverkeer.data.vlaanderen.be/ns/installatie#'))
        g.bind('wr', Namespace('https://www.vlaanderen.be/digitaal-vlaanderen/onze-oplossingen/wegenregister/'))
        g.bind('imel', Namespace('https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#'))
        g.bind('abs', Namespace('https://wegenenverkeer.data.vlaanderen.be/ns/abstracten#'))
        g.bind('sign', Namespace('https://wegenenverkeer.data.vlaanderen.be/doc/implementatiemodel/signalisatie/#'))
        g.bind('kl', Namespace('https://wegenenverkeer.data.vlaanderen.be/id/concept/'))
        g.bind('onderdeel', Namespace('https://wegenenverkeer.data.vlaanderen.be/ns/onderdeel#'))
        g.bind('wegcode', Namespace('https://www.wegcode.be/media/image/orig/'))

        self.print_graph(graph_data)

        ldes_uri = URIRef('https://example.com/ldes')
        g.add((ldes_uri, RDF.type, URIRef('https://w3id.org/ldes#EventStream')))
        # TODO add shape
        for subject in graph_data.subjects(predicate=RDF.type): # fetches all "assets" from the source data
            v_o = graph_data.value(subject=subject, predicate=URIRef(
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#AIMVersie.assetVersie'))
            asset_versie_timestamp = graph_data.value(subject=v_o, predicate=URIRef(
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAssetVersie.timestamp'))
            asset_versie_versienummer = graph_data.value(subject=v_o, predicate=URIRef(
                'https://wegenenverkeer.data.vlaanderen.be/ns/implementatieelement#DtcAssetVersie.versienummer'))

            if asset_versie_versienummer is None:
                raise ValueError(f'No version number found for asset {subject}')
            orig_id = '/'.join(str(subject).split('/')[:-1])
            g.add((subject, URIRef('http://purl.org/dc/terms/isVersionOf'), URIRef(orig_id)))
            g.add((ldes_uri, URIRef('https://w3id.org/tree#member'), subject))

            if asset_versie_timestamp is not None:
                g.add((subject, URIRef('http://purl.org/dc/terms/issued'),
                      Literal(f'{asset_versie_timestamp}Z', datatype=XSD.dateTime)))

            wkt_literal = graph_data.value(subject=subject, predicate=URIRef(
                'https://loc.data.wegenenverkeer.be/ns/implementatieelement#Locatie.geometrie'))
            if wkt_literal is not None:
                wkt_string = str(wkt_literal)
                graph_data.remove((subject, URIRef(
                'https://loc.data.wegenenverkeer.be/ns/implementatieelement#Locatie.geometrie'), wkt_literal))
                graph_data.add((subject, URIRef('http://www.w3.org/ns/locn#geometry'),
                                Literal(f'<https://www.opengis.net/def/crs/EPSG/0/31370> {wkt_string}',
                                        datatype=GEO.wktLiteral)))

        g = g + graph_data
        self.print_graph(g)

        g.serialize(destination=Path(current_dir / 'ldes_example.ttl'), format='ttl')
        g.serialize(destination=Path(current_dir / 'ldes_example.jsonld'), format='json-ld')
        g.serialize(destination=Path(current_dir / 'ldes_example.xml'), format='pretty-xml')


if __name__ == '__main__':
    objects_graph = objects.return_graph_from_objects()
    objects_graph.serialize(Path(current_dir / 'vkb_example.ttl'))
    LDESServer(Path(current_dir / 'vkb_example.ttl'))
