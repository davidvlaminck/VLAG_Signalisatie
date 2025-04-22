# resources:
# https://www.ida.liu.se/~robke04/SHACLTutorial/Introduction%20to%20SHACL.pdf
# https://shacl.org/playground/
# http://www.validatingrdf.com/
# https://15926.org/topics/SHACL/index.htm


from pathlib import Path

from otlmow_visuals.PyVisWrapper import PyVisWrapper


from C_LDES.objects import create_objects

if __name__ == '__main__':
    objects = create_objects()
    o = next(o for o in objects if o.assetId.identificator == 'bord_01' and o.assetVersie.versienummer == 1)
    objects.remove(o)
    model_dir = Path(__file__).parent.parent / 'VLAG_model'
    # requires modification of the PyVisWrapper to use the model directory
    # and color the relations
    wrapper = PyVisWrapper( model_directory=model_dir)
    wrapper.show(list_of_objects=objects, html_path=Path('show.html', model_directory=model_dir))

