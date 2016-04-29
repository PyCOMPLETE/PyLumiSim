import numpy as np

class Constants:
  r0     = 1.535e-18                     # Proton radius [m]
  eps0   = 8.854187817e-12               # Vacuum permittivity [F m-1 = A2 s4 kg-1 m-3 = C2 N-1 m-2 = C V-1 m-1]
  e      = 1.60217657e-19                # Elementaary charge [C]
  clight = 2.99792458e8                  # Speed of light [m s-1]
  h      = 6.62606957e-34                # Planck constant [J s-1] 
  hbar   = 6.62606957e-34/(2.0*np.pi)    # Reduced Planck constant [J s-1] 
  m      = 1.67262158e-27                # Proton rest mass [kg]