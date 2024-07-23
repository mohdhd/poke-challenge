import requests
from collections import defaultdict
from tqdm import tqdm

def fetch_all_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['results']
    else:
        raise Exception("Failed to fetch data from PokeAPI")

def fetch_pokemon_details(pokemon_url):
    response = requests.get(pokemon_url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch data for {pokemon_url}")

def group_pokemon_by_type(pokemon_list):
    type_groups = defaultdict(list)
    
    for pokemon in tqdm(pokemon_list, desc="Processing Pokemon", unit="pokemon"):
        details = fetch_pokemon_details(pokemon['url'])
        for poke_type in details['types']:
            type_name = poke_type['type']['name']

            #some pokemons base experience is null
            if details['base_experience'] is None:
                details['base_experience'] = 0

            type_groups[type_name].append({
                'name': details['name'],
                'base_experience': details['base_experience'],
                'abilities': [ability['ability']['name'] for ability in details['abilities']]
            })

            
    
    return type_groups

def calculate_statistics(type_groups):
    statistics = {}
    
    for poke_type, pokemons in tqdm(type_groups.items(), desc="Calculating Statistics", unit="type"):
        total_base_experience = sum(pokemon['base_experience'] for pokemon in pokemons)
        average_base_experience = total_base_experience / len(pokemons)
        
        unique_abilities = set()
        for pokemon in pokemons:
            unique_abilities.update(pokemon['abilities'])
        
        statistics[poke_type] = {
            'count': len(pokemons),
            'average_base_experience': average_base_experience,
            'unique_abilities_count': len(unique_abilities)
        }
    
    return statistics

def display_results(statistics):
    for poke_type, stats in statistics.items():
        print(f"Type: {poke_type}")
        print(f"  - Count: {stats['count']}")
        print(f"  - Average Base Experience: {stats['average_base_experience']:.2f}")
        print(f"  - Unique Abilities Count: {stats['unique_abilities_count']}")

def main():
    pokemon_list = fetch_all_pokemon()
    type_groups = group_pokemon_by_type(pokemon_list)
    statistics = calculate_statistics(type_groups)
    display_results(statistics)

if __name__ == "__main__":
    main()
