import antimony

# load a simple SBML model with MIRIAM-style annotations
# for 'glucose' and the 'cytosol'
sb='''
// Created by libAntimony v2.11.0
model *beta_cell_model()

  // Compartments and Species:
  compartment cytosol;
  species glucose in cytosol;

  // Reactions:
  glucose_import:  => glucose; glucose_import_glucose_import_rate;

  // Species initializations:
  glucose = 0;
  glucose has molar_per_volume;

  // Compartment initializations:
  cytosol = 1;

  // Variable initializations:
  glucose_import_glucose_import_rate = 1;

  // Other declarations:
  const cytosol;

  // Unit definitions:
  unit molar = 1e1 mole / 1e1 litre;
  unit molar_per_volume = 1e1 mole / (1e1 litre * litre);

  // CV terms:
  cytosol identity "https://identifiers.org/GO:0005829"
  glucose identity "http://identifiers.org/CHEBI:17234"
end
'''

antimony.loadAntimonyString(sb)

sbml = antimony.getSBMLString('beta_cell_model')
print(sbml)
