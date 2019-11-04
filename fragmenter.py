#!/usr/bin/env python

import os

from rdkit import Chem
from rdkit import RDConfig
from rdkit.Chem import FragmentCatalog

fName = os.path.join(RDConfig.RDDataDir,'FunctionalGroups.txt')
fparams = FragmentCatalog.FragCatParams(1,6,fName)
print('found %d functional groups in catalog' % (fparams.GetNumFuncGroups()))

fcat = FragmentCatalog.FragCatalog(fparams)
fcgen = FragmentCatalog.FragCatGenerator()

smiles = 'OCC=CC(=O)O'
m = Chem.MolFromSmiles(smiles)
print('examining molecule: ' + smiles)
frag_count = fcgen.AddFragsFromMol(m,fcat)
print ('identified %d fragments' % (frag_count))

for m in range(frag_count):
    print(fcat.GetEntryDescription(m))
