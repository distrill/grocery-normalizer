import starwrap as sw
import numpy as np
from operator import itemgetter
from os import listdir
from datetime import datetime

print(datetime.now().strftime("%H:%M:%S"))

train_file = './grocery_train.txt'

# aggregate category sources into training file from food/ dir
filenames = [f for f in listdir('food')]
items = []

for filename in filenames:
    label = filename.replace(".txt", "")
    file = open(f"food/{filename}", "r")
    items = items  + list(map(lambda x: f"__label__{label} {x}", file.readlines()));

with open(train_file, 'w') as file:
        file.writelines(i for i in items)

arg = sw.args()
arg.trainFile = train_file
arg.trainMode = 0		

sp = sw.starSpace(arg)
sp.init()
sp.train()

sp.saveModel('tagged_model')
sp.saveModelTsv('tagged_model.tsv')


sp.initFromSavedModel('tagged_model')
sp.initFromTsv('tagged_model.tsv')

dict_obj = sp.predictTags('ice cream', 6)
dict_obj = sorted( dict_obj.items(), key = itemgetter(1), reverse = True )

print(datetime.now().strftime("%H:%M:%S"))

for tag, prob in dict_obj:
    print( tag, prob )

