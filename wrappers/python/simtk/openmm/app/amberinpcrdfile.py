"""
armberinpcrdfile.py: Used for loading AMBER inpcrd files.
"""
__author__ = "Peter Eastman"
__version__ = "1.0"

from simtk.openmm.app.internal import amber_file_parser

class AmberInpcrdFile(object):
    """AmberInpcrdFile parses an AMBER inpcrd file and loads the data stored in it."""
    
    def __init__(self, file, loadVelocities=False, loadBoxVectors=False):
        """Load an inpcrd file.
        
        An inpcrd file contains atom positions and, optionally, velocities and periodic box dimensions.
        Unfortunately, it is sometimes impossible to determine from the file itself exactly what data
        it contains.  You therefore must specify in advance what data to load.  It is stored into this
        object's "positions", "velocities", and "boxVectors" fields.
        
        Parameters:
         - file (string) the name of the file to load
         - loadVelocities (boolean=False) whether to load velocities from the file
         - loadBoxVectors (boolean=False) whether to load the periodic box vectors
        """
        results = amber_file_parser.readAmberCoordinates(file, read_velocities=loadVelocities, read_box=loadBoxVectors)
        if loadVelocities:
            self.positions = results[0]
            if loadBoxVectors:
                self.boxVectors = results[1]
                self.velocities = results[2]
            else:
                self.velocities = results[1]
        elif loadBoxVectors:
            self.positions = results[0]
            self.boxVectors = results[1]
        else:
            self.positions = results