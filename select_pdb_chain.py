from Bio.PDB import PDBParser, PDBIO

parser = PDBParser(PERMISSIVE=1)
structure = parser.get_structure('model_Repair','model_Repair.pdb')
model = structure[0]
vp1 = model['1']

io = PDBIO()
io.set_structure(vp1)
io.save('5ddj.1.pdb')