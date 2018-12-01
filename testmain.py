from plotter import Plotter
from data import CsvDataBase

data = CsvDataBase()
data.add_csv("DATA_01_05_Cow_42.csv") #load file to  database in ram,also returns key indentifiers such as iD,internaliD,externaliD


plotter = Plotter(data)

#data.add_csv("DATA_01_05_Cow_42.csv") #will skip this file
#print(data.addedFiles()) #print already added files
#data.export_db("backup.db") #export database to file
#data.load_db("backup.db") #load database to ram,previous database will be destroyed,can call this function on load
#data.add_csv("DATA_01_05_Cow_42.csv") #will skip this file again,because it was saved to localdb,exported,loaded...and it is still in db


xcord,ycord = plotter.plot(42)

print(len(xcord),len(ycord))
