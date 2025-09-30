from modeller import environ
from modeller.automodel import automodel

# Set up the Modeller environment
env = environ()

# Optional: Set directories for input atom files (PDB)
env.io.atom_files_directory = ['./']

# Define a subclass of automodel to allow chain breaks (for ICL3)
class MyModel(automodel):
    def special_patches(self, aln):
        # Tell Modeller not to build missing loop between chain break (residues 346-363)
        self.patch(residue_type='DISU', residues=(self.residues['346'], self.residues['363']))
        # Alternatively, don't patch anything if you want it fully disconnected

# Create the model-building object
a = MyModel(env,
            alnfile='alignment.ali',         # PIR alignment file
            knowns='9AS5',               # Code of the template in the alignment file
            sequence='5HT2A_full')           # Code of the target sequence

a.starting_model = 1
a.ending_model = 1                           # Generate only one model for now

# Run the modeling
a.make()

