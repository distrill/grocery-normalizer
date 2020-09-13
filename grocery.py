import starwrap as sw
import json
import numpy as np
from operator import itemgetter
from os import listdir
from flask import Flask, request

app = Flask(__name__)

train_file = './grocery_train.txt'
data_dir = 'data'

# aggregate category sources into training file from food/ dir
filenames = [f for f in listdir(data_dir)]
items = []

for filename in filenames:
    label = filename.replace(".txt", "")
    file = open(f"{data_dir}/{filename}", "r")
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

@app.route('/')
def hello():
    item = request.args.get('item')
    dict_obj = sp.predictTags(item, 6)
    dict_obj = sorted( dict_obj.items(), key = itemgetter(1), reverse = True )

    # for tag, prob in dict_obj:
    # print( tag, prob )
    print(dict_obj[0])
    return {
        "version": "0.0.1",
        "data": dict_obj,
    }

print(__name__)
if __name__ == '__main__':
    app.run()

