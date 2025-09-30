from modeller import *

# Initialize environment
env = Environ()

# Create an alignment object
aln = Alignment(env)

# List of templates with their filenames and codes
templates = [
    ('9AS5', 'A', '9AS5.pdb'),
    ('6WGT_ECL3', 'A', '6WGT_ECL3.pdb'),
    ('6WGT_TM1', 'A', '6WGT_TM1.pdb'),
]

# Load each template model and add to the alignment
for code, chain, pdb_file in templates:
    mdl = Model(env, file=code, model_segment=(f'FIRST:{chain}', f'LAST:{chain}'))
    aln.append_model(mdl, align_codes=code, atom_files=pdb_file)

# Load the target sequence (no structure yet)
aln.append(file='5HT2A_full.ali', align_codes='5HT2A_full')

# Align the target to all templates
aln.align2d(max_gap_length=50)

# Save the alignment
aln.write(file='5HT2A-multitemplate.ali', alignment_format='PIR')
aln.write(file='5HT2A-multitemplate.pap', alignment_format='PAP')

