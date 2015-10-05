import urllib.request
class DataGrabber:
    def isFloat(self,string):
            try:
                float(string)
                return True
            except ValueError:
                return False
    def __init__(self,table,columns,order):
        url = 'http://exoplanetarchive.ipac.caltech.edu/cgi-bin/nstedAPI/nph-nstedAPI?table='+table+'&select='+columns+'&order='+order
        #bytes
        self.data = urllib.request.urlopen(url).read() 
        #decoded now
        self.text = self.data.decode('utf-8') 
        self.matrix = []
        #all rows in the text separated by newline
        rows = self.text.split('\n')
        for x in rows:
            #string array
            rawfields = x.split(',') 
            #multi-datatype array
            properfields = [] 
            #converts elements to float where applicable
            for i in rawfields:
                if self.isFloat(i):
                    properfields.append(float(i))
                else:
                    properfields.append(i)
            self.matrix.append(properfields)
        self.matrix.pop()
        
        
            
    def saveToFile(self):
        with open("output.txt",'w') as file:
            file.write(self.text)
 
    def printMatrix(self):
        for x in self.matrix:
            print(x)

    def getMatrix(self):
        return self.matrix
        
        
'''table = 'exoplanets'
columns = 'pl_hostname,ra,dec'
order = 'dec'
data = DataGrabber(table,columns,order)
data.printMatrix()'''