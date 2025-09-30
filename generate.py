from modeller import *
from modeller.automodel import *

log.verbose()
env = environ()
env.io.hetatm = True  # <<< This keeps ligand (HETATM) in output

# Load topology for better radii handling
env.libs.topology.read(file='$(LIB)/top_heav.lib')
env.libs.parameters.read(file='$(LIB)/par.lib')

a = AutoModel(env,
              alnfile='5HT2A-multitemplate.ali',
              knowns=('9AS5', '6WGT_ECL3', '6WGT_TM1'),
              sequence='5HT2A_full',
              assess_methods=(assess.DOPE, assess.GA341))

a.starting_model = 1
a.ending_model = 5  # Builds 5 models
a.make()



