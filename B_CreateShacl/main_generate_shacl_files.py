from pathlib import Path

from OTLShaclGenerator import OTLShaclGenerator

if __name__ == '__main__':
    current_dir = Path(__file__).parent
    subset_path = Path(current_dir.parent / 'A_CreateModel/VLAG_model.db')
    shacl_path = Path(current_dir / 'generated_shacl_vlag.ttl')
    ont_path = Path(current_dir / 'generated_ont_vlag.ttl')
    shacl, ont = OTLShaclGenerator.generate_shacl_from_otl(subset_path=subset_path, shacl_path=shacl_path,
                                                           ont_path=ont_path, )
