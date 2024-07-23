# PokeAPI Data Processing

## Introduction

This document explains the Python script used to fetch, process, and analyze data from the PokeAPI. The script groups Pokémon by their types, counts the number of Pokémon in each group, calculates the average base experience for each type, and determines the total number of unique abilities for each type. The results are displayed in a clear and readable format.

## Script Overview

The script is divided into several functions:

1. **fetch_all_pokemon()**: Fetches the list of all Pokémon from the PokeAPI.
2. **fetch_pokemon_details(pokemon_url)**: Fetches detailed information for a given Pokémon.
3. **group_pokemon_by_type(pokemon_list)**: Groups Pokémon by their types and collects relevant data.
4. **calculate_statistics(type_groups)**: Calculates statistics for each type, including the count of Pokémon, average base experience, and unique abilities count.
5. **display_results(statistics)**: Displays the calculated statistics in a readable format.
6. **main()**: The main function that orchestrates the fetching, processing, and displaying of data.

## How To run
1. Create a new python enviroment using venv or a similiar package

    ```sh
    python3 -m venv venv
    ```
2. Activate the python enviroment

    ```sh
    source venv/bin/activate 
    ```
3. Install the required packages using pip

    ```sh
    pip install -r requirements.tx
    ```
4. Run The script!

    ```sh
    python pokeapi_processing.py
    ```

## Code

you can find the code under the file called `pokeapi_processing`.

## Output

The script processes and outputs the following statistics for each Pokémon type:

```yaml

Processing Pokemon: 100%|██████████████| 1302/1302 [01:23<00:00, 15.50pokemon/s]
Calculating Statistics: 100%|███████████████| 18/18 [00:00<00:00, 8650.03type/s]
Type: grass
  - Count: 152
  - Average Base Experience: 146.30
  - Unique Abilities Count: 82
Type: poison
  - Count: 102
  - Average Base Experience: 151.73
  - Unique Abilities Count: 76
Type: fire
  - Count: 103
  - Average Base Experience: 169.02
  - Unique Abilities Count: 64
Type: flying
  - Count: 149
  - Average Base Experience: 165.25
  - Unique Abilities Count: 105
Type: water
  - Count: 186
  - Average Base Experience: 146.54
  - Unique Abilities Count: 99
Type: bug
  - Count: 104
  - Average Base Experience: 133.49
  - Unique Abilities Count: 77
Type: normal
  - Count: 158
  - Average Base Experience: 134.94
  - Unique Abilities Count: 106
Type: electric
  - Count: 110
  - Average Base Experience: 154.60
  - Unique Abilities Count: 65
Type: ground
  - Count: 93
  - Average Base Experience: 163.94
  - Unique Abilities Count: 73
Type: fairy
  - Count: 83
  - Average Base Experience: 177.24
  - Unique Abilities Count: 74
Type: fighting
  - Count: 100
  - Average Base Experience: 177.48
  - Unique Abilities Count: 71
Type: psychic
  - Count: 136
  - Average Base Experience: 195.14
  - Unique Abilities Count: 96
Type: rock
  - Count: 102
  - Average Base Experience: 151.42
  - Unique Abilities Count: 64
Type: steel
  - Count: 91
  - Average Base Experience: 191.49
  - Unique Abilities Count: 77
Type: ice
  - Count: 66
  - Average Base Experience: 166.21
  - Unique Abilities Count: 53
Type: ghost
  - Count: 92
  - Average Base Experience: 161.87
  - Unique Abilities Count: 68
Type: dragon
  - Count: 107
  - Average Base Experience: 201.71
  - Unique Abilities Count: 74
Type: dark
  - Count: 94
  - Average Base Experience: 176.51
  - Unique Abilities Count: 90
  
  ```

### Explaining Output

- The first 2 lines are showing the progress of the script. it's an indication so that the person running the script could follow the progress.
- The later lines shows the output of the script with the requested statistics.

## Important Notes

- some of the Pokémons don't have `base_experience` **i.e.** it shows **null** in the API Response.
Example: https://pokeapi.co/api/v2/pokemon/10258

	 I set the value for the `base_experience` to zero, so that the average calculation can be made. However, it might be better to remove them from the calculation so that they don't affect the final output.

## Testing

To ensure the correctness of the script, unit tests were written using `pytest`. The tests cover the following functions:

1.  **test_fetch_all_pokemon()**: Tests fetching the list of all Pokémon.
2.  **test_fetch_pokemon_details()**: Tests fetching detailed information for a given Pokémon.
3.  **test_group_pokemon_by_type()**: Tests grouping Pokémon by their types.
4.  **test_calculate_statistics()**: Tests calculating statistics for each type.

The `unittest.mock` module is used to mock API responses to ensure that tests are reliable and do not depend on the actual API availability.

### code
you can find the code under the file called `test_pokeapi_processing`.

### Running the Tests

To run the tests, use the following command:

```sh
pytest -v
```

