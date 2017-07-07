import yaml 
from array import array 
import glob
from openalpr import Alpr
import os 


a = 0
alpr = Alpr('us', '/etc/openalpr/openalpr.conf', '/usr/share/openalpr/runtime_data')

if not alpr.is_loaded():
    print("Error loading OpenALPR")
    sys.exit(1)

alpr.set_top_n(20)
alpr.set_default_region("md")

leidas = 0 
correctas = 0 
placa = ''
for archivo in glob.glob(os.getcwd() + "/*.yaml"):
    jpg = archivo[:-7] + ".jpg"
    results = alpr.recognize_file(jpg)

    i = 0
    for plate in results['results']:
        i += 1

        for candidate in plate['candidates']:
            
            if candidate['matches_template']:
               
                placa = candidate['plate']
                print(candidate['plate'], "esta fue por lector")
                leidas += 1
                break
        break    
    


    stream = open(archivo, "r")
    docs = yaml.load_all(stream)
    i = 0 
    for doc in docs:
        for k,v in doc.items():
            i+=1
            if i == 3:
                if v == placa:
                    correctas += 1 
                print v
                a += 1 


print a 

print "correctas" , correctas , "leidas" , leidas 
