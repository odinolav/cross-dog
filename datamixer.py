import json
import collections

dogs1 = json.load(open('dog_list_1.json', 'r'))
dogs2 = json.load(open('dog_list_2.json', 'r'))
#dogs2
#names1 = set([d['name'] for d in dogs1])
#names2 = [d['name'] for d in dogs2]
#print(len(names1), len(set(names1)), len(names2), len(set(names2)))

def make_dog_dict(dog_list):
    dogs_dict = {}
    for dog in dog_list:
        name = dog['name']
        dogs_dict[name] = dog
    return dogs_dict

dog_dict = make_dog_dict(dogs1)
dog_dict_2 = make_dog_dict(dogs2)

len(dog_dict_2.keys())

for name, obj in dog_dict.items():



#print([item for item, count in collections.Counter(names2).items() if count > 1])
#[print(name) for name in names1 if name not in names2]

#all_entries = dogs1 + dogs2
#all_entries_names = [d['name'] for d in all_entries]
#unique_names = set(all_entries_names)

#print(len(all_entries_names))
#print(len(unique_names))
#print(len(all_entries_names) - len(unique_names))
# duplicates
#print([item for item, count in collections.Counter(all_entries_names).items() if count > 1])
#print([n for n in names1 if n not in names2])

all_hybrids = []
for name in unique_names:
    if !dogs2[name]['parents']
