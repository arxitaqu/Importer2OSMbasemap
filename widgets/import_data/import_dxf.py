'''
Created on 05 nov. 2022

@author: arxit
'''
from __future__ import absolute_import

from builtins import object
from qgis.PyQt.QtCore import QCoreApplication
from qgis.core import *

from ... import main

from .import_dxf_dialog import ImportDxfDialog

class ImportDXF(object):
    '''
    Main class for the DXF importer
    '''

    def __init__(self, filename):
        '''
        Constructor

        :param filename: The DXF filename
        :type filename: str, QString
        '''
        self.filename = filename

    def runImport(self):
        '''
        Import a DXF file
        '''

        self.dlg = ImportDxfDialog(self.filename)

        if self.dlg.valid:
            self.dlg.show()
        elif self.dlg.dxf_layernames is None:
            main.qgis_interface.messageBar().pushCritical(QCoreApplication.translate('ImportDXF','Error'),
                                                                        QCoreApplication.translate('ImportDXF','DXF file is not valid'))