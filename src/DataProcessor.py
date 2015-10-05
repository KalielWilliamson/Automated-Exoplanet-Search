'''
Created on Aug 5, 2015

@author: Kaliel
'''
from DataGrabber import DataGrabber
import numpy

class DataProcessor(DataGrabber):
    '''
    classdocs
    '''
    def __init__(self, table,column,order):
        '''
        Constructor
        '''
        #instantiate a DataGrabber object
        matrix = DataGrabber(table,column,order)
        #with the data in the form of an nxm matrix, we can perform matrix transformations
        #perhaps, relying on numpy to perform the matrix transforms will be useful