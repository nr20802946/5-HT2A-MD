from modeller import *

log.verbose()
env = Environ()

# Read your own alignment file containing 5HT2A and 9AS5
aln = Alignment(env)
aln.append(file='alignment.ali', alignment_format='PIR', align_codes=('5HT2A_full', '9AS5'))

# Convert to profile format
prf = aln.to_profile()

# If you want to use a database of sequences (optional, for scanning homologs)
# You can comment this part out if you're not scanning a large database
"""
sdb = SequenceDB(env)
sdb.read(seq_database_file='pdb_95.pir', seq_database_format='PIR',
         chains_list='ALL', minmax_db_seq_len=(30, 4000), clean_sequences=True)
sdb.write(seq_database_file='pdb_95.bin', seq_database_format='BINARY',
          chains_list='ALL')
sdb.read(seq_database_file='pdb_95.bin', seq_database_format='BINARY',
         chains_list='ALL')

# Scan the profile against the database
prf.build(sdb, matrix_offset=-450, rr_file='${LIB}/blosum62.sim.mat',
          gap_penalties_1d=(-500, -50), n_prof_iterations=1,
          check_profile=False, max_aln_evalue=0.01)
"""

# Write out the profile as text (optional)
prf.write(file='5HT2A_profile.prf', profile_format='TEXT')

# Convert back to alignment format and write out
aln = prf.to_alignment()
aln.write(file='alignment.ali', alignment_format='PIR')

