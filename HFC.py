import csv

class Design:
    
     # Initialize the variables
    def __init__(self, name, llx, lly, urx, ury, polygon_count, md5sum, area, density):
 
        # Instance Variable
        self.name = name
        self.llx = llx
        self.lly = lly
        self.urx = urx
        self.ury = ury
        self.polygon_count = polygon_count
        self.md5sum = md5sum
        self.area = area
        self.density = density

class Library:
    #This class stores all instances of the Design class
    designs = []
    def add_design(self, d):#take a design object and add it to the list#
        self.designs.append(d)

    def show(self): 
        for des in sorted(self.designs, reverse=True, key=lambda design:design.density): 
            print(des.name)
        
        
lib = Library()
with open("testdata.txt", 'r', encoding="utf-16") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    # the below statement will skip the first row
    next(csv_reader,None)
    
    for line in csv_reader:
        name = line[0]
        llx = int(line[1])
        lly = int(line[2])
        urx = int(line[3])
        ury = int(line[4])
        polygon_count = int(line[5])
        md5sum = line[6]
        area = ((urx - llx)*10**-3)*((ury - lly)*10**-3) #convert microns to mm^2
        density = polygon_count / area #polygons per mm^2

        d = Design(name, llx, lly, urx, ury, polygon_count, md5sum, area, density)
        lib.add_design(d) #saves all objects in library
    lib.show()
    
