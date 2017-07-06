import yaml 
from array import array 
import glob
from openalpr import Alpr
import os 


a = 0 
alpr = Alpr('us', '/etc/openalpr/openalpr.conf', '/usr/share/openalpr/runtime_data')

alpr.set_top_n(20)
alpr.set_default_region("md")
for archivo in glob.glob(os.getcwd() + "/*.yaml"):
    results = alpr.recognize_file(archivo[:-7] + ".jpg")
    for plate in results['results']:

        for candidate in plate['candidates']:
            
            for cordiante in candidate['coordinates']:

                print coordinates + candidate + plate 

            break
        break     
    stream = open(archivo, "r")
    docs = yaml.load_all(stream)
    i = 0 
    for doc in docs:
        for k,v in doc.items():
            i+=1
            if i == 3:
                print v
                a += 1 


print a 

alpr.unload()