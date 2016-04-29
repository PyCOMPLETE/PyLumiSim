import sys
import numpy as np
from math import *
from optparse import OptionParser
from Beam import Beam
from Config import Config

parser = OptionParser()

parser.add_option("-t", "--table",   dest = "table",   help = "1: Exist after table. 0: Do complete fill.", default = "0")
parser.add_option("-n", "--name",    dest = "name",    help = "Configuration name",    default = "TDRBaselineStage2Round")
parser.add_option("-v", "--version", dest = "version", help = "Version of Luminosity", default = "034")
parser.add_option("-p", "--plevel",  dest = "plevel",  help = "Luminosity Level (p)",  default = "0.98")

(options, args) = parser.parse_args()

table   = int(options.table)
name    = options.name
version = options.version
p       = float(options.plevel)

config    = Config(name)
config._p = p

modulename = "Luminosity_v" + version

if version in  ["011", "012", "013", "021", "031", "032", "033", "034"]:
    print "Loading", modulename + "..."
    LumiModule = map(__import__, [modulename])
else:
    sys.exit("\n[!] " + modulename + ": Wrong version of Luminosity.\n")
    
print "\n>>> Initializing BEAM\n"
myBeam = Beam(config)
print ""
myBeam.printBeamParam()
print "\n<<< End of BEAM\n"

print "\n>>> Initializing LUMINOSITY"

if version in ["011", "012"]:
    lumi = LumiModule[0].Luminosity(config, name)
elif version in ["013", "021", "031", "032"]:
    lumi = LumiModule[0].Luminosity(config, name, table)
else:
    lumi = LumiModule[0].Luminosity(config, name, table, version)
print ""    

if version in ["011", "012", "013"]:
    lumi.printLumiParam()
else:
    lumi.printLumiParam(myBeam)
print ""

lumi.doFill(myBeam)

print "\n<<< End of LUMINOSITY\n"
