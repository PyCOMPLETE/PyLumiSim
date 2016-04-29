class Config:
  
  # Parameters for class "Beam":
  _momeV     = 0.0  # Momentum [eV]
  _intensity = 0.0  # Intensity (ppb) [1]
  _pmass     = 0.0  # Proton rest mass [eV]
  _epsxn     = 0.0  # Normalized horizontal emittance [m]
  _epsyn     = 0.0  # Normalized vertical emittance [m]
  _sigs      = 0.0  # Bunch length [m]
  _dpp       = 0.0  # Energy spread dp/p [1]
  _beta      = []   # [betax, betay] per IP [m]
    
  # Parameters for class "Machine":
  _circ    = 0.0  # Circunference [m]
  _rho     = 0.0  # Curvature radius [m]
  _frev    = 0.0  # Revolution frequency [Hz]
  _alfmom  = 0.0  # Momentum compaction [1]
  _tuneb   = 0.0  # Betatron tune H/V? [1]
  _tunes   = 0.0  # Synchrotron tune [1]
  _av_beta = 0.0  # Average beta [m]
  _dx      = 0.0  # Average dispersion [m]
  _nip     = 0    # Number of IPs [1]
  _ipnames = []   # [IPname] per IP
  _nbunch  = []   # Colliding pairs per IP [1]
  _Nbunch  = 0    # Number of bunches (total) [1]
  _sepLR   = []   # Beam LR separation per IP [sigma?]
  _xplane  = []   # Crossing plane per IP [H=0,V=1]
  _wcc     = 0.0  # Crab cavity frequency [Hz]
  _oncc    = []   # Crab cavity ON per IP [1]
  
  # Parameters for luminosity calculations:
  _level_Lumi     = []   # Leveled luminosity [cm-2 s-1]
  _level_pileup   = []   # Leveled pile-up [1]
  _betatol        = 0.0  # Beta tolerance (minimum beta achievable)
  _xsec           = 0.0  # Cross section for pile-up [mb]
  _xsecburn       = 0.0  # Cross section for burn-off [mb]
  _days           = 0.0  # Dedicated time to physics [days yr-1]
  _efficiency     = 0.0  # Beam fficiency [1]
  _turnaround     = 0.0  # Turn-around time [h]
  _step           = 0.0  # Time steps [s]
  _max_length     = 0.0  # Maximum store length (time) [s]
  _p              = 0.0  # Reduction (percentage) of the luminosity that triggers leveling.
  _constbetaratio = []   # Constant beta ratio [Yes=1,No=0]
  _timealignstep  = 0.0  # Time to realign the beams after squeezing [s]
  
  # IBS:
  _kappa   = 0.0  # ? [1]
  _kappa_c = 0.0  # ? [1]
  
  # Bunch length leveling:
  _lengthleveling      = 0   # Reduction factor of sigs and dpp [1]
  _constantbunchlength = 0   # [0 for no, 1 for yes]
  _betamindict         = {}  # ?
  
  def __init__(self,name):
    
    print ""
    print "Loading configuration", name, "..."
    self.loadcommon()
    
    exec("self.load"+name+"()")
    self.checkconfig()

  def loadcommon(self):
    
      self._momeV = 6500.0e9
      self._pmass = 0.93827231e9
      self._dpp   = 1.2e-4  
      
      self._circ    = 26658.8832
      self._rho     = 2804          # Before: 3000.0
      self._alfmom  = 3.225e-4
      self._tuneb   = 64.31
      self._tunes   = 0.002342
      self._nip     = 3
      self._ipnames = ["IP1", "IP5", "IP8"]
      self._xplane  = [0, 0, 1]
      self._wcc     = 400.0e6
      
      self._level_pileup    = [1e9, 1e9, 1e9]  # Large number to not do pile-up leveling by default?
      self._betatol         = 0.002
      self._xsec            = 81     # Old: 85.  New: 81  (updated 16/Oct/15)
      self._xsecburn        = 111    # Old: 100. New: 100 (updated 16/Oct/15)
      self._days            = 160
      self._efficiency      = 0.5
      self._turnaround      = 3.12
      self._step            = 600        # Original: 600, equal to 10 min. 
      self._max_length      = 20*3600    # 20 h
      self._p               = 0.9        # The fraction of initial luminosity that, after decay, triggers leveling. Careful with the extremes. p = 0.0: The first imply burning the beam one sigle time, with no leveling. Analytically, the intensity tends to zero, but never it will never reach it. p = 1.0: The decaying time will be zero, and it will be stucked running at the initial time over and over.
      self._constbetaratio  = [1, 1, 0]
      self._alignstep       = True
      self._timealignstep   = 3.0
      self._updatealignstep = False
      
      self._kappa   = 1.0
      self._kappa_c = 0.1
      
      self._lengthleveling      = 0
      self._constantbunchlength = 0
      
      self._RF800 = 0  # [0 for no, 1 for yes]

  def loadLargeLumi(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 2.2e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.1,0.1],[0.1,0.1],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.0755
    #LUminosity
    self._level_Lumi = [7.5e34,7.5e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 0
    self._lengthleveling = -0.0001

  def loadLargeLumi200MHzLev(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [11.2,11.2,11.2]
    self._intensity = 2.2e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.12
    #LUminosity
    self._level_Lumi = [7.5e34,7.5e34,2.0e33]
    self._level_pileup = [1.41,1.41,1e9]
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 0
    self._lengthleveling = -0.0001

  def loadLargeLumi200MHzPushed(self):
    #General
    self._nbunch = [2880,2880,2880]
    self._sepLR = [11.,11.,11.]
    self._intensity = 2.4e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.1,0.1],[0.1,0.1],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.10
    #LUminosity
    self._level_Lumi = [7.86e34,7.86e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 0
    self._lengthleveling = -0.0001

  def loadecloud200MHz_short(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 2.2e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.15
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=0
    self._xplane = [0,0,1]
    self._RF800 = 0
    self._lengthleveling = -0.012

  def loadecloud200MHz(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 2.4e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.15
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 0
    self._lengthleveling = -0.0001

  def loadecloud8b4e_pushed(self):
    #General
    self._nbunch = [2016,2016,2016]
    self._sepLR = [8,8,11.0]
    self._intensity = 2.3e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.1,0.1],[0.1,0.1],[3.5,3.5]]
    self._epsxn = 2.2e-6
    self._epsyn = 2.2e-6
    self._sigs = 0.0755
    #LUminosity
    self._level_Lumi = [3.75e34,3.75e34,2.0e33]  
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._max_length = 19*3600

  def load8b4eOfficialVH(self):
    
    self._momeV     = 7000.0e9
    self._intensity = 2.3e11
    self._epsxn     = 2.2e-6
    self._epsyn     = 2.2e-6
    self._sigs      = 0.0755
    self._dpp       = 1.13e-4
    self._beta      = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    
    self._nbunch = [1960,1960,1868]
    self._Nbunch = 1968
    self._sepLR  = [9.0,9.0,10.0]  # Original: [10.0,10.0,10.0]. Rogelio slides Ago 27, 2015: [9.0,9.0,?]
    self._xplane = [1,0,1]    
    #self._oncc  = [1,1,0]          # Original (ON)
    #self._oncc   = [1.200,1.200,0.0]
    #self._oncc  = [1.150,1.150,0.0]
    #self._oncc  = [1.100,1.100,0.0]
    #self._oncc  = [1.050,1.050,0.0]
    #self._oncc  = [1.010,1.010,0.0]
    #self._oncc  = [1.001,1.001,0.0]
    #self._oncc  = [1.000,1.000,0.0]
    #self._oncc  = [0.999,0.999,0.0]
    #self._oncc  = [0.990,0.990,0.0]
    #self._oncc  = [0.950,0.950,0.0]
    #self._oncc  = [0.900,0.900,0.0]
    #self._oncc  = [0.800,0.800,0.0]
    #self._oncc  = [0.700,0.700,0.0]
    #self._oncc  = [0.600,0.600,0.0]
    self._oncc  = [0.500,0.500,0.0]
    #self._oncc  = [0.400,0.400,0.0]
    #self._oncc  = [0.300,0.300,0.0]
    #self._oncc  = [0.200,0.200,0.0]
    #self._oncc  = [0.150,0.150,0.0]
    #self._oncc  = [0.100,0.100,0.0]
    #self._oncc  = [0.050,0.050,0.0]
    #self._oncc  = [0.010,0.010,0.0]
    #self._oncc  = [0.001,0.001,0.0]
    #self._oncc  = [0.0,0.0,0.0]
    #self._oncc  = [0,0,0]         # Off
    
    self._level_Lumi = [3.63e34,3.63e34,2.0e33]
    self._max_length = 19*3600
    
    self._constantbunchlength = 1

  def load8b4eOfficial(self):
    #General
    self._momeV = 7000.0e9
    self._nbunch = [1960,1960,1868]
    self._Nbunch = 1968
    self._sepLR = [10,10,10.0]
    self._intensity = 2.3e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 2.2e-6
    self._epsyn = 2.2e-6
    self._sigs = 0.0755
    self._dpp = 1.13e-4
    #LUminosity
    self._level_Lumi = [3.63e34,3.63e34,2.0e33]  
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._max_length = 19*3600

  def loadFlatNowireNoCC_DAlev(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [13.0,13.0,13.0]
    self._intensity = 2.2e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.4,0.35],[0.40,0.35],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.0755
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]  
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._betamindict = { "intensities":[3e11, 1.8e11, 1.65e11 ,1.5e11, 1.4e11, 1.3e11], "betas": [[0.4,0.35], [0.4,0.30], [0.4,0.25] ,[0.4,0.20],[0.4,0.10], [0.3,0.075]] }

  def loadFlatNowireNoCC_DAlev2(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [13.5,13.5,11.0]
    self._intensity = 2.2e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.4,0.35],[0.40,0.35],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.0755
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]  
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._betamindict = { "intensities":[3e11, 2e11, 1.6e11, 1.5e11], "betas": [[0.4,0.35], [0.4,0.30],   [0.4,0.10], [0.3,0.075]] }

  def loadFlatNowireNoCC200MHz(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [12,12,12]
    self._intensity = 2.56e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.5,0.1],[0.5,0.1],[3.5,3.5]]
    self._epsxn = 3e-6
    self._epsyn = 3e-6
    self._sigs = 0.15
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]  
    self._constantbunchlength=0
    self._xplane = [0,0,1]
    self._lengthleveling = -0.008

  def loadFlatNowireNoCC(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [11.2,11.2,11.0]
    self._intensity = 2.2e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.30,0.075],[0.30,0.075],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.0825
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]  
    self._constantbunchlength=1
    self._xplane = [0,0,1]

  def loadFlatNowireNoCC4010_6cm(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [11.0,11.0,11.0]
    self._intensity = 2.2e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.4,0.1],[0.4,0.1],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.06
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]  
    self._constantbunchlength=1
    self._xplane = [0,0,1]

  def loadFlatNowireNoCC4010_800(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [11.0,11.0,11.0]
    self._intensity = 2.2e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.4,0.1],[0.4,0.1],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.0755
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]  
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 1

  def loadFlatNowireNoCC4010(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [11.0,11.0,11.0]
    self._intensity = 2.2e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.4,0.1],[0.4,0.1],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.0755
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]  
    self._constantbunchlength=1
    self._xplane = [0,0,1]

  def loadFlatNoCC(self):              #Valishev 22nd LARP Collaboration Meeting
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [9.5,9.5,9.5]
    self._intensity = 2.2e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.3,0.075],[0.30,0.075],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.095
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]  
    self._constantbunchlength=1
    self._xplane = [0,0,1]

  def load50ns(self):
    #General
    self._nbunch = [1380,1380,1380]
    self._sepLR = [11.0,11.0,11.0]
    self._intensity = 3.5e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 3e-6
    self._epsyn = 3e-6
    self._sigs = 0.1
    #LUminosity
    self._level_Lumi = [2.6e34,2.6e34,1.0e33]  
    self._constantbunchlength=1
    self._xplane = [0,0,1]

  def loadrecord(self):
    #General
    self._nbunch = [300,300,100]
    self._sepLR = [0,0,0.0]
    self._intensity = 2e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.1,0.1],[0.1,0.1],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.0755
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 0

  def loadUS2abeta10cm80b(self):
    #General
    self._nbunch = [2880,2880,2748]
    self._sepLR = [9.8,9.8,10.0]   # 590mum at 6.5TeV and 0.1m
    self._intensity = 2.2e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.1,0.1],[0.1,0.1],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.08
    #LUminosity
    self._level_Lumi = [5.34e34,5.34e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 0

  def loadUS2abeta10cm80b200(self):
    #General
    self._nbunch = [2880,2880,2748]
    self._sepLR = [10.7,10.7,10.0]   # scaled from 9.8 with int.
    self._intensity = 2.4e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.1,0.1],[0.1,0.1],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.1
    #LUminosity
    self._level_Lumi = [5.34e34,5.34e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 0

  def loadUS2abeta10cm(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [9.8,9.8,10.0]
    self._intensity = 2.2e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.1,0.1],[0.1,0.1],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.0755
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 0

  def loadUS2aNoCCrama(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [9.5,9.5,9.5]
    self._intensity = 2.2e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.0755
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 0

  def loadUS2a(self):
    #General
    self._momeV = 7000.0e9
    self._Nbunch = 2748
    self._nbunch = [2736,2736,2524] 
    self._sepLR = [12.5,12.5,12.0]
    self._intensity = 2.2e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.0755
    self._dpp = 1.2e-4
    #LUminosity
    self._level_Lumi = [5.0e34,5.e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 0

  def loadUS2aVH(self):
    
    self._momeV = 7000.0e9
    self._intensity = 2.2e11
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.0755
    self._dpp = 1.13e-4  # I've been working with 1.13e-4, but I think (?) that the original was 1.2e-4. Update: Rogelio's slide says 1.13e-4
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]  # Original
    #self._beta = [[0.30,0.15],[0.30,0.15],[7.0,3.5]]  # To check flat beams
    
    self._nbunch = [2736,2736,2524] 
    self._Nbunch = 2748
    self._sepLR = [12.5,12.5,12.0]
    self._xplane = [1,1,1]   # Original: [1,0,1], I change it to [1,1,1] to make IP1/5 identical and speed up. With [0,0,1] it makes leveling in y (not x), keeping IP1/5 identical.
    self._oncc  = [1,1,0]          # Original (ON)
    #self._oncc  = [0.68,0.68,0.0]      # The right value
    #self._oncc  = [0,0,0]         # Off
    
    self._level_Lumi = [5.0e34,5.e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    
    self._constantbunchlength = 1
     
    self._RF800 = 0

  def loadMyFlat(self): # Replaced for new configurations: see at the bottom
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736,2736,2748] 
    self._sepLR     = [11.9,11.9,10.0]
    self._intensity = 2.2e11
    self._oncc      = [1,1,0]
    #Beam
    self._beta  = [[0.3,0.075],[0.3,0.075],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081     # Updated; 15/Oct/15
    self._dpp   = 1.08e-4   # Updated; 15/Oct/15
    #LUminosity
    self._level_Lumi = [5.0e34,5.0e34,2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0,0,1]

  def loadMyRound(self):  # Replaced for new configurations: see at the bottom
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736,2736,2748] 
    self._sepLR     = [12.5,12.5,12.0]
    self._intensity = 2.2e11
    self._oncc      = [1,1,0]    # Original: [0.6771,0.6771,0]
    #Beam
    self._beta  = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081    # Updated; 15/Oct/15
    self._dpp   = 1.08e-4  # Updated; 15/Oct/15
    #LUminosity
    self._level_Lumi = [5.0e34,5.0e34,2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0,0,1]
  
  def loadUS2a10sigma(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [10.0,10.0,12.0]
    self._intensity = 2.2e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.0755
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 0

  def loadUS2Gianluigi(self):
    #General
    self._momeV = 7000.0e9
    self._nbunch = [2592,2592,2592]
    self._sepLR = [12.5,12.5,12.5]
    self._intensity = 2.2e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.1
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 0

  def loadUS2a10cm(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 2.2e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.1
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 0
    self._level_pileup=[0.96,0.96,5]
    self._betatol = 0.002

  def loadUS2aForStephane(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 1e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.1
    #LUminosity
    self._level_Lumi = [55.1e34,55.1e34,52.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 0
    self._level_pileup=[1000,10000,10000]
    self._betatol = 0.002

  def loadUS2aRF800(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 2.2e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.125
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=1
    self._xplane = [0,0,1]
    self._RF800 = 1
    self._level_pileup=[0.9,0.9,5]
    self._betatol = 0.004

  def loadUS2b(self):
    #General
    self._nbunch = [2748,2748,2748]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 2.2e11
    self._oncc=[1,1,0]
    #Beam
    self._beta = [[0.3,0.075],[0.30,0.075],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.0755
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]  
    self._constantbunchlength=1
    self._xplane = [0,0,1]

  def loadUS2NoPic(self):
    #General
    self._nbunch = [2760,2760,2760]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 2.2e11
    self._oncc=[0,0,0]
    self._xplane = [1,0,1]
    #Beam
    self._beta = [[0.25,0.8],[0.8,0.25],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.1
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]

  def load200MHzSplit(self):
    self._nbunch = [2760.*2,2760*2.,2760*2.]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 2.56e11/2.
    self._oncc=[1,1,0]
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 3e-6
    self._epsyn = 3e-6
    self._sigs = 0.1
    self._xplane = [1,1,1]
    self._level_Lumi = [9.1e34,9.1e34,4.0e33]
    self._lengthleveling = -0.0001 # Relative increment every step

  def load200MHzSplit8b4e(self):
    self._nbunch = [2760.*4./3,2760*4./3,2760*4./3]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 3.e11/2.
    self._oncc=[1,1,0]
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 3e-6
    self._epsyn = 3e-6
    self._sigs = 0.1
    self._xplane = [1,1,1]
    self._level_Lumi = [6.8e34,6.8e34,3.0e33]
    self._lengthleveling = -0.0001 # Relative increment every step

  def load200MHzPushed(self):
    #General
    self._nbunch = [2760,2760,2760]
    self._sepLR = [15.0,15.0,15.0]
    self._intensity = 2.5e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.2,1],[1,0.2],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.15
    self._xplane = [1,0,1]
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]

  def load200MHz400CC(self):
    self._nbunch = [2760,2760,2760]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 2.56e11
    self._oncc=[1,1,0]
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 3e-6
    self._epsyn = 3e-6
    self._sigs = 0.13
    self._xplane = [1,1,1]
    self._level_Lumi = [5.13e34,5.13e34,2.0e33]
    self._lengthleveling = -0.012 # Relative increment every step

  def load200MHz400CCf(self):
        self._nbunch = [2760,2760,2760]
        self._sepLR = [12.0,12.0,12.0]
        self._intensity = 2.56e11
        self._oncc=[1,1,0]
        self._beta = [[0.1,0.5],[0.1,0.5],[3.5,3.5]]
        self._epsxn = 3e-6
        self._epsyn = 3e-6
        self._sigs = 0.13
        self._xplane = [1,1,1]
        self._level_Lumi = [5.1e34,5.1e34,2.0e33]
        self._lengthleveling = -0.012 # Relative increment every step

  def load200MHz400CCfb(self):
        self._nbunch = [2760,2760,2760]
        self._sepLR = [12.0,12.0,12.0]
        self._intensity = 2.56e11
        self._oncc=[1,1,0]
        self._beta = [[0.075,0.3],[0.075,0.3],[3.5,3.5]]
        self._epsxn = 3e-6
        self._epsyn = 3e-6
        self._sigs = 0.13
        self._xplane = [1,1,1]
        self._level_Lumi = [5.1e34,5.1e34,2.0e33]
        self._lengthleveling = -0.001 # Relative increment every step, with 0.005 and 0.003 this gave:
        #200MHz400CCfb 2.56 3.0 0.075 0.3 274.7 11. 10. 141. 1.21 0.030 0.031 5.152 0.075 232.7
        #200MHz400CCfb 2.56 3.0 0.075 0.3 273.4 11. 9.8 140. 1.14 0.030 0.031 5.145 0.086 232.6

  def load200MHz400CCfb_PUL(self):
        self._nbunch = [2760,2760,2760]
        self._sepLR = [12.0,12.0,12.0]
        self._intensity = 2.56e11
        self._oncc=[1,1,0]
        self._beta = [[0.075,0.3],[0.075,0.3],[3.5,3.5]]
        self._epsxn = 3e-6
        self._epsyn = 3e-6
        self._sigs = 0.13
        self._xplane = [1,1,1]
        self._level_Lumi = [5.1e34,5.1e34,2.0e33]
        self._lengthleveling = -0.001
        self._level_pileup = [0.98, 0.98, 100]

  def load200MHz400CCfb11sigma(self):
        self._nbunch = [2760,2760,2760]
        self._sepLR = [11.0,11.0,11.0]
        self._intensity = 2.56e11
        self._oncc=[1,1,0]
        self._beta = [[0.075,0.3],[0.075,0.3],[3.5,3.5]]
        self._epsxn = 3e-6
        self._epsyn = 3e-6
        self._sigs = 0.13
        self._xplane = [1,1,1]
        self._level_Lumi = [5.1e34,5.1e34,2.0e33]
        self._lengthleveling = -0.003 # Relative increment every step

  def load200MHz400NoCC(self):
    self._nbunch = [2760,2760,2760]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 2.56e11
    self._oncc=[0,0,0]
    self._beta = [[0.1,0.5],[0.1,0.5],[3.5,3.5]]
    self._epsxn = 3e-6
    self._epsyn = 3e-6
    self._sigs = 0.13
    self._xplane = [1,1,1]
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    self._lengthleveling = -0.012 # Relative increment every step
    self._level_pileup = [1.4,1.4,1e9]

  def load200MHz400NoCCNoWire(self):
    self._nbunch = [2760,2760,2760]
    self._sepLR = [14.0,14.0,12.0]
    self._intensity = 2.56e11
    self._oncc=[0,0,0]
    self._beta = [[0.1,0.5],[0.1,0.5],[3.5,3.5]]
    self._epsxn = 3e-6
    self._epsyn = 3e-6
    self._sigs = 0.13
    self._xplane = [1,1,1]
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    self._lengthleveling = -0.012 # Relative increment every step
    self._level_pileup = [1.4,1.4,1e9]

  def load200MHz400NoCCNoWireRound(self):
    self._nbunch = [2760,2760,2760]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 2.56e11
    self._oncc=[0,0,0]
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 3e-6
    self._epsyn = 3e-6
    self._sigs = 0.13
    self._xplane = [1,1,1]
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    self._lengthleveling = -0.012 # Relative increment every step
    self._level_pileup = [100,100,1e9]

  def load200MHz400(self):
    self._nbunch = [2760,2760,2760]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 2.56e11
    self._oncc=[0,0,0]
    self._beta = [[0.20,0.8],[0.8,0.20],[3.5,3.5]]
    self._epsxn = 3e-6
    self._epsyn = 3e-6
    self._sigs = 0.13
    self._xplane = [1,0,1]
    self._level_Lumi = [6.5e34,6.5e34,2.0e33]
    self._lengthleveling = -0.02 # Relative increment every step

  def load200MHz(self):
    #General
    self._nbunch = [2760,2760,2760]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 2.56e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.20,0.8],[0.8,0.20],[3.5,3.5]]
    self._epsxn = 3e-6
    self._epsyn = 3e-6
    self._sigs = 0.15
    self._xplane = [1,0,1]
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]

  def load200MHzBCMS(self):
    self._nbunch = [2504,2504,2504]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 2.56e11
    self._oncc=[0,0,0]
    self._beta = [[0.20,0.8],[0.8,0.20],[3.5,3.5]]
    self._epsxn = 2.4e-6
    self._epsyn = 2.4e-6
    self._sigs = 0.15
    self._xplane = [1,0,1]
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]

  def load200MHz8b4e(self):
    self._nbunch = [1840,1840,1840]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 3e11
    self._oncc=[1,1,0]
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 3e-6
    self._epsyn = 3e-6
    self._sigs = 0.13
    self._xplane = [1,1,1]
    self._level_Lumi = [3.5e34,3.5e34,1.2e33]
    self._lengthleveling = -0.012

  def loadUS2NoPicMaxi(self):
    #General
    self._nbunch = [2760,2760,2760]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 2.5e11
    self._oncc=[0,0,0]
    self._xplane = [1,0,1]
    #Beam
    self._beta = [[0.25,0.8],[0.8,0.25],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.1
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    
  def load2012(self):
      self._momeV = 4000.0e9
      self._nbunch = [1340,1340,1340]
      self._sepLR = [10.0,10.0,10.0]
      self._intensity = 1.6e11
      self._oncc=[0,0,0]
      self._beta = [[0.6,0.6],[0.6,0.6],[3.5,3.5]]
      self._epsxn = 2e-6
      self._epsyn = 2e-6
      self._sigs = 0.1
      self._level_Lumi = [1e34,1e34,2.0e33]
      self._efficiency = 0.4

  def loadLS1flat1(self):
    #General
    self._nbunch = [2590,2590,2590]
    self._sepLR = [12.0,12.0,10.0]
    self._intensity = 1.2e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.4,0.5],[0.5,0.4],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.075
    #LUminosity
    self._level_Lumi = [1.7e34,1.7e34,2.0e33]
    self._xplane = [1,0,1]
    self._lengthleveling = 0.002 

  def loadLS1Rod2(self):
    #General
    self._nbunch = [2590,2590,2590]
    self._sepLR = [12.0,12.0,10.0]
    self._intensity = 1.2e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.4,0.4],[0.4,0.4],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.075
    #LUminosity
    self._level_Lumi = [1.7e34,1.7e34,2.0e33]
    self._xplane = [1,0,1]
    self._lengthleveling = 0.002  

  def loadLS1Roderick(self):
    #General
    self._nbunch = [2590,2590,2590]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 1.2e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.65,0.65],[0.65,0.65],[3.5,3.5]]
    self._epsxn = 3.75e-6
    self._epsyn = 3.75e-6
    self._sigs = 0.1
    #LUminosity
    self._level_Lumi = [1.6e34,1.6e34,2.0e33]
    self._xplane = [1,0,1]
    self._lengthleveling = 0.002  
    self._turnaround = 5.0
    self._days = 90

  def loadLS1mine(self):
    #General
    self._nbunch = [2590,2590,2590]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 1.2e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.61,0.61],[0.61,0.61],[3.5,3.5]]
    self._epsxn = 3.e-6
    self._epsyn = 3.e-6
    self._sigs = 0.1
    #LUminosity
    self._level_Lumi = [1.6e34,1.6e34,2.0e33]
    self._xplane = [1,0,1]
    self._lengthleveling = 0.002 
    self._turnaround = 5.0
    self._days = 90

  def loadLS1mine2(self):
    #General
    self._nbunch = [2590,2590,2590]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 1.2e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.65,0.65],[0.65,0.65],[3.5,3.5]]
    self._epsxn = 3.e-6
    self._epsyn = 3.e-6
    self._sigs = 0.1
    #LUminosity
    self._level_Lumi = [1.6e34,1.6e34,2.0e33]
    self._xplane = [1,0,1]
    self._lengthleveling = 0.002 
    self._turnaround = 5.0
    self._days = 90

  def loadLS1design(self):
    #General
    self._nbunch = [2590,2590,2590]
    self._sepLR = [10.0,10.0,10.0]
    self._intensity = 1.2e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.55,0.55],[0.55,0.55],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.1
    #LUminosity
    self._level_Lumi = [1.54e34,1.54e34,2.0e33]
    self._xplane = [1,0,1]
    self._lengthleveling = 0.002

  def loadLS1Nom(self):
    #General
    self._nbunch = [2590,2590,2590]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 1.25e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.4,0.4],[0.4,0.4],[3.5,3.5]]
    self._epsxn = 1.65e-6
    self._epsyn = 1.65e-6
    self._sigs = 0.1
    #LUminosity
    self._level_Lumi = [1.54e34,1.54e34,2.0e33]
    self._xplane = [1,0,1]
    self._lengthleveling = 0.002   
    
  def loadLS18b4e(self):
    #General
    self._nbunch = [1960,1960,1840]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 1.71e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.4,0.4],[0.4,0.4],[3.5,3.5]]
    self._epsxn = 2.7e-6
    self._epsyn = 2.7e-6
    self._sigs = 0.075
    #LUminosity
    self._level_Lumi = [1.1e34,1.1e34,1.0e33]
    self._xplane = [1,0,1]
    self._lengthleveling = 0.002   
    self._max_length = 19*3600
    self._turnaround = 5.0
    self._days = 90

  def loadNoPic(self):
    #General
    self._nbunch = [2592,2592,2592]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 1.38e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.2,0.8],[0.80,0.20],[3.5,3.5]]
    self._epsxn = 1.8e-6
    self._epsyn = 1.8e-6
    self._sigs = 0.075
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    self._xplane = [1,0,1]

  def loadPIC8be4(self):
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 1.85e11
    self._nbunch = [1840,1840,1840]
    self._oncc=[0,0,0]
    self._beta = [[0.2,0.8],[0.80,0.20],[3.5,3.5]]
    self._epsxn = 2.2e-6
    self._epsyn = 2.2e-6
    self._sigs = 0.1
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    self._xplane = [1,0,1]

  def loadPIC8be4Nom(self):
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 1.85e11
    self._nbunch = [1840,1840,1840]
    self._oncc=[0,0,0]
    self._beta = [[0.2,0.4],[0.40,0.20],[3.5,3.5]]
    self._epsxn = 2.2e-6
    self._epsyn = 2.2e-6
    self._sigs = 0.1
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    self._xplane = [1,0,1]

  def loadPIC50ns(self):
    #General
    self._nbunch = [1380,1380,1380]
    self._sepLR = [11.0,11.0,11.0]
    self._intensity = 3.5e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.2,0.8],[0.8,0.2],[3.5,3.5]]
    self._epsxn = 3e-6
    self._epsyn = 3e-6
    self._sigs = 0.1
    #LUminosity
    self._level_Lumi = [2.6e34,2.6e34,2.0e33]
    self._xplane = [1,0,1]
    self._constantbunchlength=0

  def loadPIC1(self):
    #General
    self._nbunch = [2592,2592,2592]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 1.38e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.2,0.4],[0.4,0.2],[3.5,3.5]]
    self._epsxn = 1.8e-6
    self._epsyn = 1.8e-6
    self._sigs = 0.0755
    #LUminosity
    self._level_Lumi = [4.6e34,4.6e34,2.0e33]
    self._xplane = [1,0,1]
    self._constantbunchlength=1
    
  def loadPIC2(self):
    #General
    self._nbunch = [2760,2760,2760]
    self._sepLR = [12.0,12.0,12.0]
    self._intensity = 1.38e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.20,0.40],[0.40,0.20],[3.5,3.5]]
    self._epsxn = 2.22e-6
    self._epsyn = 2.22e-6
    self._sigs = 0.075
    #LUminosity
    self._level_Lumi = [4.6e34,4.6e34,2.0e33]
    self._xplane = [1,0,1]

  def loadUS150ns(self):
    self._nbunch = [1380,1380,1380]
    self._sepLR = [10.0,10.0,10.0]
    self._intensity = 3.5e11
    self._oncc=[0,0,0]
    self._xplane = [1,0,1]
    self._beta = [[0.2,0.8],[0.8,0.2],[3.5,3.5]]
    self._epsxn = 3e-6
    self._epsyn = 3e-6
    self._sigs = 0.1
    self._level_Lumi = [2.6e34,2.6e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]

  def loadUS1ct(self):
    self._nbunch = [2760,2760,2760]
    self._sepLR = [10.0,10.0,10.0]
    self._intensity = 1.9e11
    self._oncc=[0,0,0]
    self._xplane = [1,0,1]
    self._beta = [[0.2,0.8],[0.8,0.2],[3.5,3.5]]
    self._epsxn = 2.62e-6
    self._epsyn = 2.62e-6
    self._sigs = 0.0755
    self._level_Lumi = [4.64e34,4.64e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]

  def loadUS1200MHz(self):
    self._nbunch = [2760,2760,2760]
    self._sepLR = [10.0,10.0,10.0]
    self._intensity = 2.56e11
    self._oncc=[0,0,0]
    self._xplane = [1,0,1]
    self._beta = [[0.2,0.8],[0.8,0.2],[3.5,3.5]]
    self._epsxn = 3e-6
    self._epsyn = 3e-6
    self._sigs = 0.13
    self._level_Lumi = [5.05e34,5.05e34,2.0e33]
    self._lengthleveling = -0.01

  def loadUS18b4e(self):
    self._nbunch = [1960 ,1960,1840]
    self._sepLR = [10.0,10.0,10.0]
    self._intensity = 2.4e11
    self._oncc=[0,0,0]
    self._xplane = [1,0,1]
    self._beta = [[0.2,0.8],[0.8,0.2],[3.5,3.5]]
    self._epsxn = 2.2e-6
    self._epsyn = 2.2e-6
    self._sigs = 0.075
    self._level_Lumi = [3.67e34,3.675e34,.8e33]
    self._constantbunchlength=1

  def loadUS18b4elargerX(self):
    self._nbunch = [1840,1840,1840]
    self._sepLR = [14.0,14.0,14.0]
    self._intensity = 2.4e11
    self._oncc=[0,0,0]
    self._xplane = [1,0,1]
    self._beta = [[0.2,0.8],[0.8,0.2],[3.5,3.5]]
    self._epsxn = 2.2e-6
    self._epsyn = 2.2e-6
    self._sigs = 0.075
    self._level_Lumi = [3.45e34,3.45e34,.8e33]
    self._constantbunchlength=1

  def loadUS1200MHz8b4e(self):
    self._nbunch = [1840*2,1840*2,1840*2]
    self._sepLR = [10.0,10.0,10.0]
    self._intensity = 3.e11/2.
    self._oncc=[0,0,0]
    self._xplane = [1,0,1]
    self._beta = [[0.2,0.8],[0.8,0.2],[3.5,3.5]]
    self._epsxn = 3e-6
    self._epsyn = 3e-6
    self._sigs = 0.1
    self._level_Lumi = [7e34,7e34,.8e33]
    self._lengthleveling = -0.0001

  def loadUS18b4eNom(self):
    self._nbunch = [1960,1960,1840]
    self._sepLR = [10.0,10.0,10.0]
    self._intensity = 2.85e11
    self._oncc=[0,0,0]
    self._xplane = [1,0,1]
    self._beta = [[0.2,0.4],[0.4,0.2],[3.5,3.5]]
    self._epsxn = 2.2e-6
    self._epsyn = 2.2e-6
    self._sigs = 0.075
    self._level_Lumi = [3.67e34,3.67e34,.8e33]

  def loadUS1a(self):
    self._nbunch = [2748,2748,2748]
    self._sepLR = [10.0,10.0,10.0]
    self._intensity = 1.9e11
    self._oncc=[0,0,0]
    self._xplane = [1,0,1]
    self._beta = [[0.2,0.4],[0.4,0.2],[3.5,3.5]]
    self._epsxn = 2.62e-6
    self._epsyn = 2.62e-6
    self._sigs = 0.0755
    self._level_Lumi = [5.05e34,5.05e34,2.0e33]
    #self._level_pileup = [1.1,1.1,1e9]
    self._constantbunchlength=1

  def loadUS1b(self):
    #General
    self._nbunch = [2592,2592,2592]
    self._sepLR = [10.0,10.0,10.0]
    self._intensity = 1.9e11
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.2,0.4],[0.4,0.2],[3.5,3.5]]
    self._epsxn = 2.62e-6
    self._epsyn = 2.62e-6
    self._sigs = 0.0755
    #LUminosity
    self._level_Lumi = [4.6e34,4.6e34,2.0e33]
    self._xplane = [1,0,1]
    self._constantbunchlength=1

  def loadUS2_noX_noCC(self):
    #General
    self._momeV = 6500.0e9
    self._pmass = 0.93827231e9
    self._circ = 26658.8832
    self._rho = 3000.0
    self._alfmom = 3.225e-4
    self._tuneb = 64.31
    self._tunes = 0.002342
    self._nip = 3
    self._nbunch = [2760,2760,2600]
    self._sepLR = [0.0,0.0,0.0]
    self._xplane = [1,0,1]
    self._intensity = 2.2e11
    self._wcc = 400.0e6
    self._oncc=[0,0,0]
    #Beam
    self._beta = [[0.15,0.15],[0.15,0.15],[3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs = 0.075
    self._dpp = 1.2e-4
    #LUminosity
    self._level_Lumi = [5.1e34,5.1e34,2.0e33]
    self._betatol = 0.006
    self._xsec = 85
    self._days = 160
    self._efficiency = 0.5
    self._turnaround = 3.12
    self._step = 600
    self._max_length = 15*3600  
    #IBS
    self._kappa=1.0
    self._kappa_c = 0.1
    self.checkconfig()
    
  def checkconfig(self):
    
    if (len(self._nbunch) != self._nip):
      print "ERROR: wrong bunch definition:", self._nip, self._nbunch
    
    if (len(self._beta) != self._nip):
      print "ERROR: wrong beta1 definition:", self._nip, self._beta
    
    if (len(self._sepLR) != self._nip):
      print "ERROR: wrong sepLR definition:", self._nip, self._sepLR
    
    if (len(self._xplane) != self._nip):
      print "ERROR: wrong xplane definition:", self._nip, self._xplane
    
    if (len(self._level_Lumi) != self._nip):
      print "ERROR: wrong Level_Lumi definition:", self._nip, self._level_Lumi
  
  
  # FOR TDR (18 Nov 15):

  def loadTDRBaselineStage1Round(self):  # From "US2a" (with oncc != 1)  -- DONE
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]    # Updated in IP8 (in proceedings). Original: 2748.
    self._sepLR     = [12.5, 12.5, 12.0]
    self._intensity = 2.2e11
    self._oncc      = [0.6771, 0.6771, 0.0]
    #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [5.31783065e34, 5.31783065e34, 2.0e33]  # New values to make pile-up equal to 140, and to compensate the change of xsec from 85 to 81
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
  
  def loadTDRBaselineStage1Flat(self):  # From "FlatNoWire_CCstage1" -- DONE
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]    # Updated in IP8 (in proceedings). Original: 2748.
    self._sepLR     = [11.9, 11.9, 10.0]
    self._intensity = 2.2e11
    self._oncc      = [1.0, 1.0, 0.0]
    #Beam
    self._beta  = [[0.3,0.075], [0.3,0.075], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [5.31779215e34, 5.31779215e34, 2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
  
  def loadTDRBaselineStage2Round(self):  # From "US2a" -- DONE
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]
    self._sepLR     = [12.5, 12.5, 12.0]
    self._intensity = 2.2e11
    self._oncc      = [1.0, 1.0, 0.0]
        #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [5.31783065e34, 5.31783065e34, 2.0e33]  # New values to make pile-up equal to 140, and to compensate the change of xsec from 85 to 81
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
    
  def loadTDR8b4e(self):   # From "8b4eOfficial" -- DONE
    #General
    self._momeV     = 7000.0e9
    self._nbunch    = [1960, 1960, 1868]
    self._Nbunch    = 1968
    self._sepLR     = [12.5, 12.5, 10.0]   # I kept IP8 equal to 10.0 since I don't have any update
    self._intensity = 2.3e11
    self._oncc      = [1.0, 1.0, 0.0]
        #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.2e-6
    self._epsyn = 2.2e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [3.80958650e34, 3.80958650e34, 2.0e33]  
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
  
  def loadTDR200MHz(self):  # From "ecloud200MHz_short"  -- DONE
    #General
    self._momeV     = 7000.0e9
    self._nbunch    = [2736, 2736, 2524]    # Updated in IP8 (in proceddings). Original: 2400.
    self._Nbunch    = 2748
    self._sepLR     = [12.5,12.5,12.0]
    self._intensity = 2.2e11
    self._oncc      = [1.0, 1.0, 0.0]
        #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.15    # Change in sigs does not apply to 200 MHz
    self._dpp   = 1.0e-4  # Change in sigs does not apply to 200 MHz
    #Luminosity
    self._level_Lumi = [5.31511207e34, 5.31511207e34, 2.0e33]  # New values to make pile-up equal to 140, and to compensate the change of xsec from 85 to 81
    self._constantbunchlength = 0
    self._xplane = [0, 0, 1]
    self._RF800 = 0
    self._lengthleveling = -0.012  # This value is no lnger valid. It should be lower, but I'll keep it the same since it's not very important (as long as 0.15 reaches 0.081 before the run ends).
   
  def loadTDRNoCCNoWire(self):  # From "FlatNoWire"  -- DONE
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]    # Updated in IP8 (in proceddings). Original: 2748
    self._sepLR     = [11.9, 11.9, 10.0]
    self._intensity = 2.2e11
    self._oncc      = [0.0, 0.0, 0.0]
    #Beam
    self._beta  = [[0.3,0.075], [0.3,0.075], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [5.31996889e34, 5.31996889e34, 2.0e33]  # New values to make pile-up equal to 140, and to compensate the change of xsec from 85 to 81
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
  
  def loadTDRNoCCWire(self):  # From "FlatWireNoCC_Stephane280"  - DONE
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]    # Updated in IP8 (in proceddings). Original: 2748
    self._sepLR     = [9.7, 9.7, 10.0]
    self._intensity = 2.2e11
    self._oncc      = [0.0, 0.0, 0.0]
    #Beam
    self._beta  = [[0.4,0.1], [0.4,0.1], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [5.31903413e34, 5.31903413e34, 2.0e33]  # New values to make pile-up equal to 140, and to compensate the change of xsec from 85 to 81
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
    
  def loadTDRBaselineStage2Round210pileup(self):  # From "US2a" 
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]
    self._sepLR     = [12.5, 12.5, 12.0]
    self._intensity = 2.2e11
    self._oncc      = [1.0, 1.0, 0.0]
    #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [7.98443371e34, 7.98443371e34, 2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]

  def loadTDR200MHzConstBunchLength(self):  # From "TDR200MHz", pero manteniendo el bunch length constante
    #General
    self._momeV     = 7000.0e9
    self._nbunch    = [2736, 2736, 2524]
    self._Nbunch    = 2748
    self._sepLR     = [12.5,12.5,12.0]
    self._intensity = 2.2e11
    self._oncc      = [1.0, 1.0, 0.0]
    #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.15
    self._dpp   = 1.0e-4
    #Luminosity
    self._level_Lumi = [5.31511207e34, 5.31511207e34, 2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
    self._RF800 = 0
    #self._lengthleveling = -0.012  # Not needed if bunch length is kept constant

  ####

  def loadApr16BaselineStage2Round(self):  # The same than TDRBaselineStage2Round
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]
    self._sepLR     = [12.5, 12.5, 12.0]
    self._intensity = 2.2e11
    self._oncc      = [1.0, 1.0, 0.0]
    #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [5.31783065e34, 5.31783065e34, 2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
    
  def loadApr16200MHz(self):  # The same than TDR200MHz
    #General
    self._momeV     = 7000.0e9
    self._nbunch    = [2736, 2736, 2524]
    self._Nbunch    = 2748
    self._sepLR     = [12.5,12.5,12.0]
    self._intensity = 2.2e11
    self._oncc      = [1.0, 1.0, 0.0]
    #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.15
    self._dpp   = 1.0e-4
    #Luminosity
    self._level_Lumi = [5.31511207e34, 5.31511207e34, 2.0e33]
    self._constantbunchlength = 0
    self._xplane = [0, 0, 1]
    self._RF800 = 0
    self._lengthleveling = -0.012
   
  def loadApr16BaselineStage1Round(self):  # The same than TDRBaselineStage1Round
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]
    self._sepLR     = [12.5, 12.5, 12.0]
    self._intensity = 2.2e11
    self._oncc      = [0.6771, 0.6771, 0.0]
    #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [5.31783065e34, 5.31783065e34, 2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
    
  def loadApr16NoCCNoWire(self):  #The same than TDRNoCCNoWire
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]
    self._sepLR     = [11.9, 11.9, 10.0]
    self._intensity = 2.2e11
    self._oncc      = [0.0, 0.0, 0.0]
    #Beam
    self._beta  = [[0.3,0.075], [0.3,0.075], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [5.31996889e34, 5.31996889e34, 2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
    
  def loadApr16200MHz10percMorePPB(self):
    #General
    self._momeV     = 7000.0e9
    self._nbunch    = [2736, 2736, 2524]
    self._Nbunch    = 2748
    self._sepLR     = [12.5,12.5,12.0]
    self._intensity = 2.2e11*1.10
    self._oncc      = [1.0, 1.0, 0.0]
    #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.15
    self._dpp   = 1.0e-4
    #Luminosity
    self._level_Lumi = [5.31511207e34, 5.31511207e34, 2.0e33]
    self._constantbunchlength = 0
    self._xplane = [0, 0, 1]
    self._RF800 = 0
    self._lengthleveling = -0.012

  def loadApr16BaselineStage2Round200PU(self):
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]
    self._sepLR     = [12.5, 12.5, 12.0]
    self._intensity = 2.2e11
    self._oncc      = [1.0, 1.0, 0.0]
    #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [7.596622e34, 7.596622e34, 2.0e33]   # It's with nbunc, not Nbunch! -- the values used for TDR are wrong 8a little bit!)
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
    
  def loadApr16200MHz200PU(self):
    #General
    self._momeV     = 7000.0e9
    self._nbunch    = [2736, 2736, 2524]
    self._Nbunch    = 2748
    self._sepLR     = [12.5,12.5,12.0]
    self._intensity = 2.2e11
    self._oncc      = [1.0, 1.0, 0.0]
    #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.15
    self._dpp   = 1.0e-4
    #Luminosity
    self._level_Lumi = [7.596622e34, 7.596622e34, 2.0e33]
    self._constantbunchlength = 0
    self._xplane = [0, 0, 1]
    self._RF800 = 0
    self._lengthleveling = -0.012
   
  def loadApr16BaselineStage1Round200PU(self):
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]
    self._sepLR     = [12.5, 12.5, 12.0]
    self._intensity = 2.2e11
    self._oncc      = [0.6771, 0.6771, 0.0]
    #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [7.596622e34, 7.596622e34, 2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
    
  def loadApr16NoCCNoWire200PU(self):
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]
    self._sepLR     = [11.9, 11.9, 10.0]
    self._intensity = 2.2e11
    self._oncc      = [0.0, 0.0, 0.0]
    #Beam
    self._beta  = [[0.3,0.075], [0.3,0.075], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [7.596622e34, 7.596622e34, 2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
    
  def loadApr16BaselineStage2RoundStephane(self):  # The same than Apr16BaselineStage2Round (but sigs=0.075), to corroborate his luminous region
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]
    self._sepLR     = [12.5, 12.5, 12.0]
    self._intensity = 2.2e11
    self._oncc      = [1.0, 1.0, 0.0]
    #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.075
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [5.31783065e34, 5.31783065e34, 2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
    
    
  def loadApr16NoCCWire(self):  # The same than TDRNoCCWire, for completness
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]
    self._sepLR     = [9.7, 9.7, 10.0]
    self._intensity = 2.2e11
    self._oncc      = [0.0, 0.0, 0.0]
    #Beam
    self._beta  = [[0.4,0.1], [0.4,0.1], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [5.31903413e34, 5.31903413e34, 2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
    
  def loadApr16BaselineStage1Flat(self):  # The same than TDRBaselineStage1Flat, for completness
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]
    self._sepLR     = [11.9, 11.9, 10.0]
    self._intensity = 2.2e11
    self._oncc      = [1.0, 1.0, 0.0]
        #Beam
    self._beta  = [[0.3,0.075], [0.3,0.075], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [5.31779215e34, 5.31779215e34, 2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
    
  def loadApr16BaselineStage2RoundCCOff(self):  # The same than Apr16BaselineStage2Round, but oncc = 0.0, 0.0
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]
    self._sepLR     = [12.5, 12.5, 12.0]
    self._intensity = 2.2e11
    self._oncc      = [0.0, 0.0, 0.0]
    #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [5.31783065e34, 5.31783065e34, 2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
    
  def loadApr16BaselineStage1FlatCCOff(self):  # The same than Apr16BaselineStage1Flat, but oncc = 0.0, 0.0
    #General
    self._momeV     = 7000.0e9
    self._Nbunch    = 2748
    self._nbunch    = [2736, 2736, 2524]
    self._sepLR     = [11.9, 11.9, 10.0]
    self._intensity = 2.2e11
    self._oncc      = [0.0, 0.0, 0.0]
        #Beam
    self._beta  = [[0.3,0.075], [0.3,0.075], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.081
    self._dpp   = 1.08e-4
    #Luminosity
    self._level_Lumi = [5.31779215e34, 5.31779215e34, 2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]

  def loadApr16200MHzConstSIGS(self):  # Keeping constant sigs ) 15 cm
    #General
    self._momeV     = 7000.0e9
    self._nbunch    = [2736, 2736, 2524]
    self._Nbunch    = 2748
    self._sepLR     = [12.5,12.5,12.0]
    self._intensity = 2.2e11
    self._oncc      = [1.0, 1.0, 0.0]
    #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.15
    self._dpp   = 1.0e-4
    #Luminosity
    self._level_Lumi = [5.31511207e34, 5.31511207e34, 2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
    self._RF800 = 0
    self._lengthleveling = -0.012

  def loadApr16200MHz200PUConstSIGS(self): # Keeping constant sigs = 15 cm
    #General
    self._momeV     = 7000.0e9
    self._nbunch    = [2736, 2736, 2524]
    self._Nbunch    = 2748
    self._sepLR     = [12.5,12.5,12.0]
    self._intensity = 2.2e11
    self._oncc      = [1.0, 1.0, 0.0]
    #Beam
    self._beta  = [[0.15,0.15], [0.15,0.15], [3.5,3.5]]
    self._epsxn = 2.5e-6
    self._epsyn = 2.5e-6
    self._sigs  = 0.15
    self._dpp   = 1.0e-4
    #Luminosity
    self._level_Lumi = [7.596622e34, 7.596622e34, 2.0e33]
    self._constantbunchlength = 1
    self._xplane = [0, 0, 1]
    self._RF800 = 0
    self._lengthleveling = -0.012