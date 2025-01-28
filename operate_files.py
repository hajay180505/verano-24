import json
import shutil


label_names = [
    "good_weld",
    "burn_through",
    "contamination",
    "lack_of_fusion",
    "misalignment",
    "lack_of_penetration",
]
labels = [0, 1, 2, 3, 4, 5]

data = json.load(open('./kaggle/al5083/test/test.json'))

counter = { 0 : 0 , 1 : 0, 2 : 0, 3 : 0, 4 : 0 , 5 : 0}
files = {
    0 : [],
    1 : [],
    2 : [],
    3 : [],
    4 : [],
    5 : []
}

for k,v in data.items():
    counter[v] +=1
    files[v].append('./kaggle/al5083/test/'+k)

for k, v in files.items() :
    tot = len(v)
    files[k] = {
        'train' : v[:int(.8*tot)],
        'test' : v[int(.8*tot) : int(.9*tot)],
        'val' : v[int(.9*tot):]
    }

print()
# print(files)
print(counter)

# f = open("./temp.json", "w")
# f.write(json.dumps(files, indent=2))


data = json.load(open("./kaggle/al5083/train/train.json"))

counter = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
files1 = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}

for k, v in data.items():
    counter[v] += 1
    files1[v].append("./kaggle/al5083/train/" + k)

for k, v in files1.items():
    tot = len(v)
    files[k] = {
        "train": v[: int(0.8 * tot)],
        "test": v[int(0.8 * tot) : int(0.9 * tot)],
        "val": v[int(0.9 * tot) :],
    }

print()
# print(files)
print(counter)

for i in range(6):
    files[label_names[i]] = files[i]
    del files[i]


f = open("./temp.json", "w")
f.write(json.dumps(files, indent=2))
print("doneee")


import os

os.makedirs("organized_data", exist_ok=True)
os.makedirs("organized_data/test", exist_ok=True)
os.makedirs("organized_data/train", exist_ok=True)
os.makedirs("organized_data/val", exist_ok=True)
for k in ['test', 'train', 'val']:
    for i in label_names:
        os.makedirs(os.path.join('organized_data',k,i), exist_ok=True)

counter = 0
for label,categs in files.items():
    for k,v in categs.items():
        for item in v:
            shutil.move(item, os.path.join('organized_data', k, label, str(counter))+'.png')
            counter +=1


print("Yes!!")
