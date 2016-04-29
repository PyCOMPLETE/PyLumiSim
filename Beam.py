import numpy as np
from Constants import Constants as cst

class Beam:
  
  _momeV     = 0.0
  _intensity = 0.0
  _pmass     = 0.0
  _gamma     = 0.0  # Relativistic gamma [1]
  _betarel   = 0.0  # Relativistic beta [1]
  _epsxn     = 0.0
  _epsyn     = 0.0
  _sigs      = 0.0
  _initsigs  = 0.0  # Initial bunch length (equal to sigs)
  _dpp       = 0.0
  _initdpp   = 0.0  # Initial bunch length (equal to sigs), added by me here
  _beta      = []
  # betamin ?
  
  _circ    = 0.0
  _rho     = 0.0
  _frev    = 0.0
  _alfmom  = 0.0
  _tuneb   = 0.0
  _tunes   = 0.0
  _av_beta = 0.0
  _dx      = 0.0
  _nip     = 0
  _ipnames = []
  _nbunch  = []
  _sepLR   = []
  _xplane  = []
  _wcc     = 0.0
  _oncc    = []
  
  _kappa   = 0.0
  _kappa_c = 0.0
  
  _taux_sr  = 0.0  # Horizontal radiation damping time [h]
  _tauy_sr  = 0.0  # Vertical radiation damping time [h]
  _tauz_sr  = 0.0  # Longitudinal radiation damping time [h]
  _dpp0     = 0.0  # ?
  _sigs0    = 0.0  # ?
  _epsx0    = 0.0  # ?
  _epsy0    = 0.0  # ?
  _betamin  = []   # ? [m]
  _phi      = []   # Crossing angle [rad]
  _phiCR    = []   # CC angle [rad]
  
  def __init__(self,config):
    
    self._momeV     = config._momeV
    self._intensity = config._intensity
    self._pmass     = config._pmass    
    self._gamma     = config._momeV/config._pmass + 1.0
    self._betarel   = np.sqrt(1.0 - 1.0/(self._gamma**2.0))
    self._epsxn     = config._epsxn
    self._epsyn     = config._epsyn
    self._sigs      = config._sigs
    self._initsigs  = config._sigs
    self._dpp       = config._dpp
    self._initdpp   = config._dpp
    self._beta      = np.array(config._beta)
    self._betamin   = np.array(config._beta)
    
    self._circ    = config._circ
    self._rho     = config._rho
    self._frev    = cst.clight / config._circ    
    self._alfmom  = config._alfmom
    self._tuneb   = config._tuneb
    self._tunes   = config._tunes
    self._av_beta = config._circ/(2*np.pi) / config._tuneb
    self._dx      = config._circ/(2*np.pi) * config._alfmom
    self._nip     = config._nip
    self._ipnames = config._ipnames
    self._nbunch  = config._nbunch
    self._Nbunch  = config._Nbunch
    self._sepLR   = np.array(config._sepLR)
    self._xplane  = config._xplane  
    self._wcc     = config._wcc
    self._oncc    = config._oncc
    
    self._level_Lumi = config._level_Lumi
    
    self._lengthleveling      = config._lengthleveling
    self._constantbunchlength = config._constantbunchlength
    self._constbetaratio      = config._constbetaratio
    
    self._identicalIP01 = (self._beta[0][0] == self._beta[1][0])*(self._beta[0][1] == self._beta[1][1]) * (self._oncc[0] == self._oncc[1]) * (self._sepLR[0] == self._sepLR[1]) * (self._nbunch[0] == self._nbunch[1]) * (self._xplane[0] == self._xplane[1] )* (self._constbetaratio[0] == self._constbetaratio[1] )
    
    print "*", "IP0 and IP1 are identical?",  self._identicalIP01
    
    # Crossing angle:
    
    for i in range(self._nip):
      sigp = np.sqrt( self._epsyn / (self._gamma*self._betarel) / self._beta[i][self._xplane[i]] )
      self._phi.append(sigp*self._sepLR[i]) 
    
    # Crab angle:
    
    for i in range(self._nip):
      self._phiCR.append( self._oncc[i]*self._phi[i] )
    
    # For radiation damping:
    
    dEsr = cst.e**2 * self._betarel**3 * self._gamma**4 / (3*cst.eps0*self._rho) / cst.e / self._momeV
    
    self._taux_sr = 2.0/(dEsr*self._frev*3600.0)
    self._tauy_sr = 2.0/(dEsr*self._frev*3600.0)
    self._tauz_sr = 1.0/(dEsr*self._frev*3600.0)
    
    I1 = self._dx*2*np.pi
    I2 = 2*np.pi/self._rho
    I3 = 2*np.pi/self._rho**2
    I4 = self._circ*self._alfmom/self._rho**2
    I5 = 1/self._av_beta*self._dx**2/self._rho**2*2*np.pi
    
    cq = 55/(32*np.sqrt(3.0))*cst.hbar/(cst.m*cst.clight)
    
    self._dpp0  = np.sqrt(cq*self._gamma**2*I3/(2*I2))
    self._sigs0 = self._alfmom*cst.clight/(2*np.pi*self._tunes*cst.clight/self._circ)*self._dpp0
    self._epsx0 = cq*self._gamma**2*I5/I2*self._betarel*self._gamma
    self._epsy0 = 13.0/55.0*cq/I2*self._av_beta/self._rho**2*2*np.pi*self._betarel*self._gamma
    
    # For IBS:
    
    self._kappa   = config._kappa
    self._kappa_c = config._kappa_c
  
  def getsigma(self,ip):
    
    betx = self._beta[ip][0]
    bety = self._beta[ip][1]
    sigx = np.sqrt( self._epsxn*betx/(self._gamma*self._betarel) )
    sigy = np.sqrt( self._epsyn*bety/(self._gamma*self._betarel) )
    
    return sigx, sigy
  
  
  def printBeamParam(self):
    
    print "BEAM PARAMETERS:"
    print ""
    print "*", "{0:32} {1:10}".format("Momentum", "eV"),                  "%1.2e" %self._momeV
    print "*", "{0:32} {1:10}".format("Relativistic gamma", "1"),         "%1.2f" %self._gamma
    print "*", "{0:32} {1:10}".format("Relativistic beta", "1"),          "%1.12f" %self._betarel
    print "*", "{0:32} {1:10}".format("Norm. emittance horizontal", "m"), "%1.4e" %self._epsxn
    print " ", "{0:32} {1:10}".format("                vertical", "m"),   "%1.4e" %self._epsyn
    print "*", "{0:32} {1:10}".format("Bunch length", "m"),               "%1.4e" %self._sigs
    print "*", "{0:32} {1:10}".format("Energy spread dp/p", "1"),         "%1.4e" %self._dpp
    print "*", "{0:32} {1:10}".format("Proton rest mass", "eV"),          "%1.4e" %self._pmass
    print "*", "{0:32} {1:10}".format("Intensity (ppb)", "1"),            "%1.4e" %self._intensity
    
    print "*", "{0:32} {1:10}".format("Beta* horizontal", "m"),
    for i in range(self._nip):
      print self._ipnames[i] + ":", "{0:16}".format("%1.8f" %self._beta[i][0]),
    print ""
    print " ", "{0:32} {1:10}".format("      vertical", "m"),
    for i in range(self._nip):
      print 4*" ", "{0:16}".format("%1.8f" %self._beta[i][1]),
    print ""
    
    print ""
    print "MACHINE PARAMETERS:"
    print ""
    print "*", "{0:32} {1:10}".format("Circumference", "m"),                "%1.4f" %self._circ
    print "*", "{0:32} {1:10}".format("Curvature radius", "m"),             "%1.2f" %self._rho
    print "*", "{0:32} {1:10}".format("Revolution frequency", "Hz"),        "%1.4e" %self._frev
    print "*", "{0:32} {1:10}".format("Average beta (H&V?)", "m"),          "%1.4f" %self._av_beta
    print "*", "{0:32} {1:10}".format("Average dispersion", "m"),           "%1.4f" %self._dx
    print "*", "{0:32} {1:10}".format("Momentum compaction", "1"),          "%1.4e" %self._alfmom
    print "*", "{0:32} {1:10}".format("Betatron tune (H&V?)", "1"),         "%1.2e" %self._tuneb
    print "*", "{0:32} {1:10}".format("Synchrotron tune", "1"),             "%1.4e" %self._tunes
    print "*", "{0:32} {1:10}".format("Crab cavity frequency", "Hz"),       "%1.2e" %self._wcc
    print "*", "{0:32} {1:10}".format("Number of IPs", "1"),                self._nip
    
    print "*", "{0:32} {1:10}".format("Crossing plane", "H=0/V=1"),
    for i in range(self._nip):
      print self._ipnames[i] + ":", repr(self._xplane[i]).ljust(16),
    print ""
    
    print "*", "{0:32} {1:10}".format("Colliding pairs", "1"),
    for i in range(self._nip):
      print 4*" ", repr(self._nbunch[i]).ljust(16),
    print ""
    
    print "*", "{0:32} {1:10}".format("Beam LR separation", "sigma?"),
    for i in range(self._nip):
      print 4*" ", "{0:16}".format("%1.4f" %self._sepLR[i]),
    print ""
    
    print "*", "{0:32} {1:10}".format("Crossing angle", "rad"),
    for i in range(self._nip):
      print 4*" ", "{0:16}".format("%1.4e" %self._phi[i]),
    print ""
    
    print "*", "{0:32} {1:10}".format("Crab cavity ON", "1"),
    for i in range(self._nip):
      print 4*" ", "{0:16}".format("%1.4f" %self._oncc[i]),
    print ""
    
    print "*", "{0:32} {1:10}".format("Crab cavity angle", "rad"),
    for i in range(self._nip):
      print 4*" ", "{0:16}".format("%1.4e" %self._phiCR[i]),
    print ""
    
    print ""
    print "RADIATION DAMPING AND IBS:"
    print ""
    print "*", "{0:32} {1:10}".format("Radiation damp. time horizontal", "h"), "%1.4f" %self._taux_sr
    print " ", "{0:32} {1:10}".format("                     vertical", "h"),   "%1.4f" %self._tauy_sr
    print " ", "{0:32} {1:10}".format("                     longitud.", "h"),  "%1.4f" %self._tauz_sr
    print "*", "{0:32} {1:10}".format("IBS kappa", "1"),                       "%1.2f" %self._kappa
    print "*", "{0:32} {1:10}".format("IBS kappa_c", "1"),                     "%1.2f" %self._kappa_c