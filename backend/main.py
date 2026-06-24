from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import Draw
import os

img_path = '../assets/chemical_structure.png'
mol = Chem.MolFromSmiles('CC(C)Cc1ccc(cc1)C(C)C(=O)O')
img = Draw.MolToImage(mol)
img.show()
# Ro5 descriptors
img.save(img_path)
MW = Descriptors.MolWt(mol)
HBA = Descriptors.NOCount(mol)
HBD = Descriptors.NHOHCount(mol)
LogP = Descriptors.MolLogP(mol)
conditions = [MW <= 500, HBA <= 10, HBD <= 5, LogP <= 5]
pass_ro5 = conditions.count(True) >= 3
if pass_ro5:
    print("The drug is suitable for absorbtion in the human body.")
else:
    print("The drug is not suitable for absorbtion in the human body.")
input("Press enter to continue...")
if os.path.exists(img_path):
    os.remove(img_path)
