# resources:
# https://www.ida.liu.se/~robke04/SHACLTutorial/Introduction%20to%20SHACL.pdf
# https://shacl.org/playground/
# http://www.validatingrdf.com/
# https://15926.org/topics/SHACL/index.htm
import concurrent.futures
import os

import time
from os.path import abspath
from pathlib import Path

from rdflib import Graph, Namespace, URIRef, RDF, RDFS, OWL, Literal, SH, BNode, SKOS
from pyshacl import validate

from SQLDbReader import SQLDbReader

if __name__ == '__main__':
    # load the SHACL graphs
    g = Graph()
    g.parse(format='turtle', source=Path(__file__).parent.parent / 'B_CreateShacl' / 'generated_ont_vlag.ttl')
    g.parse(format='turtle', source=Path(__file__).parent.parent / 'B_CreateShacl' / 'generated_shacl_vlag.ttl')
    print(f'Loaded {len(g)} triples in SHACL graph')

    # load the data graph
    h = Graph()
    h.parse(format='turtle', source=Path(__file__).parent.parent / 'C_LDES' / 'vkb_example.ttl')
    print(f'Loaded {len(h)} triples in data graph')

    start = time.time()
    r = validate(h,
                 shacl_graph=g,
                 allow_infos=True,
                 allow_warnings=True)
    conforms, results_graph, results_text = r
    end = time.time()
    print(f'Validation done in {round(end - start, 2)} seconds')
    print(results_text)
