import json
import collections

dogs1 = json.load(open('dog_list_1.json', 'r'))
dogs2 = json.load(open('dog_list_2.json', 'r'))
#dogs2
names1 = set([d['name'] for d in dogs1])
allnames2 = [d['name'] for d in dogs2]
len(names2_pure)
#names2 = set([d['name'] for d in dogs2 if len(d['parents'])])
#print(len(names1), len(names2))
#names1 - names2
#print([item for item, count in collections.Counter(names1 | set(names2)).items() if count > 1])

all_names = names1 | set(allnames2)

def make_dog_dict(dog_list):
    dogs_dict = {}
    for dog in dog_list:
        name = dog['name']
        dogs_dict[name] = dog
    return dogs_dict

dog_dict = make_dog_dict(dogs1)
dog_dict_2 = make_dog_dict(dogs2)

len(dog_dict_2.keys())

for name, obj in dog_dict_2.items():
    if name in dog_dict:
        #if set(dog_dict[name]['parents']) != set(obj['parents']):
            #print(dog_dict[name]['parents'], obj['parents'], name)
            # Disparities are fine.
            # dog_dict (from the first website) has better parent data in disparities, so leave be
        dog_dict[name]['imgs'] = list(set(dog_dict[name]['imgs'] + obj['imgs']))
        dog_dict[name]['urls'] = [dog_dict[name]['url'], obj['url']]
        dog_dict[name]['other_names'] = obj['other_names']
    else:
        dog_dict[name] = obj

len(dog_dict)

all_parents = set()
for name in dog_dict:
    all_parents |= set(dog_dict[name]['parents'])
len(all_parents)

all_parents = list(all_parents)

all_pure = set()
for name in dog_dict:
    if len(dog_dict[name]['parents']) == 0:
        all_pure.add(name)

set(all_parents) - set(all_pure)

f = open('dog_dict.json', 'w')
f.write(json.dumps(dog_dict))
f.close()

f = open('all_parents.json', 'w')
f.write(json.dumps([p.lower() for p in all_parents]))
f.close()


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

#all_hybrids = []
#for name in unique_names:
#    if !dogs2[name]['parents']
