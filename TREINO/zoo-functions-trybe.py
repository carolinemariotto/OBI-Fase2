from data import species 
hfff
def get_animal_map(initial_species):
    result = dict()
    
    for specie in initial_species:
        if specie['location'] not in result:
            result[specie["location"]] = [specie]
        else:
            result[specie["locaation"]].append(specie)
    return result
print(get_animal_map())