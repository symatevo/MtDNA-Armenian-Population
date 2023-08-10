from Bio import SeqIO
from Bio import Entrez
from Bio.SeqFeature import SeqFeature, FeatureLocation
import re
import pandas as pd

def create_metadata(name, startId, lastId):
    lastId = lastId + 1
    access_id = []
    population = []
    Entrez.email = "syuzi.matevosyan1802@gmail.com"
    for id in range(startId, lastId):
        filename = name + str(id)
        net_handle = Entrez.efetch(
            db="nucleotide", id=filename, rettype="gb", retmode="text"
        )
        record = SeqIO.read(net_handle, "gb")
        access_id.append(filename)
        population.append(record.features[0].qualifiers.get("isolation_source")[0])
    
    list_of_tuples = list(zip(access_id, population))
    metadata = pd.DataFrame(list_of_tuples,
                  columns=['access_id', 'population'])
    return metadata

df = create_metadata("MK491", 355, 357)
print(df)