import pytest
from unittest.mock import patch
from pokeapi_processing import fetch_all_pokemon, fetch_pokemon_details, group_pokemon_by_type, calculate_statistics

class MockResponse:
    def __init__(self, json_data, status_code=200):
        self.json_data = json_data
        self.status_code = status_code

    def json(self):
        return self.json_data

@patch('pokeapi_processing.requests.get')
def test_fetch_all_pokemon(mock_get):
    mock_response = {
        'results': [
            {'name': 'bulbasaur', 'url': 'https://pokeapi.co/api/v2/pokemon/1/'},
            {'name': 'ivysaur', 'url': 'https://pokeapi.co/api/v2/pokemon/2/'}
        ]
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    result = fetch_all_pokemon()
    assert len(result) == 2
    assert result[0]['name'] == 'bulbasaur'
    assert result[1]['name'] == 'ivysaur'

@patch('pokeapi_processing.requests.get')
def test_fetch_pokemon_details(mock_get):
    mock_response = {
        'name': 'bulbasaur',
        'base_experience': 64,
        'abilities': [{'ability': {'name': 'overgrow'}}, {'ability': {'name': 'chlorophyll'}}],
        'types': [{'type': {'name': 'grass'}}, {'type': {'name': 'poison'}}]
    }
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = mock_response

    result = fetch_pokemon_details('https://pokeapi.co/api/v2/pokemon/1/')
    assert result['name'] == 'bulbasaur'
    assert result['base_experience'] == 64
    assert result['abilities'][0]['ability']['name'] == 'overgrow'

@patch('pokeapi_processing.requests.get')
def test_group_pokemon_by_type(mock_get):
    mock_pokemon_list = [
        {'name': 'bulbasaur', 'url': 'https://pokeapi.co/api/v2/pokemon/1/'},
        {'name': 'ivysaur', 'url': 'https://pokeapi.co/api/v2/pokemon/2/'}
    ]
    
    mock_response_1 = {
        'name': 'bulbasaur',
        'base_experience': 64,
        'abilities': [{'ability': {'name': 'overgrow'}}, {'ability': {'name': 'chlorophyll'}}],
        'types': [{'type': {'name': 'grass'}}, {'type': {'name': 'poison'}}]
    }
    mock_response_2 = {
        'name': 'ivysaur',
        'base_experience': 142,
        'abilities': [{'ability': {'name': 'overgrow'}}, {'ability': {'name': 'chlorophyll'}}],
        'types': [{'type': {'name': 'grass'}}, {'type': {'name': 'poison'}}]
    }
    
    def side_effect(url):
        if url == 'https://pokeapi.co/api/v2/pokemon/1/':
            return MockResponse(mock_response_1)
        elif url == 'https://pokeapi.co/api/v2/pokemon/2/':
            return MockResponse(mock_response_2)
    
    mock_get.side_effect = side_effect

    type_groups = group_pokemon_by_type(mock_pokemon_list)
    assert 'grass' in type_groups
    assert len(type_groups['grass']) == 2
    assert 'poison' in type_groups
    assert len(type_groups['poison']) == 2

def test_calculate_statistics():
    mock_type_groups = {
        'grass': [
            {'name': 'bulbasaur', 'base_experience': 64, 'abilities': ['overgrow', 'chlorophyll']},
            {'name': 'ivysaur', 'base_experience': 142, 'abilities': ['overgrow', 'chlorophyll']}
        ],
        'poison': [
            {'name': 'bulbasaur', 'base_experience': 64, 'abilities': ['overgrow', 'chlorophyll']},
            {'name': 'ivysaur', 'base_experience': 142, 'abilities': ['overgrow', 'chlorophyll']}
        ]
    }

    statistics = calculate_statistics(mock_type_groups)
    assert statistics['grass']['count'] == 2
    assert statistics['grass']['average_base_experience'] == pytest.approx(103)
    assert statistics['grass']['unique_abilities_count'] == 2
    assert statistics['poison']['count'] == 2
    assert statistics['poison']['average_base_experience'] == pytest.approx(103)
    assert statistics['poison']['unique_abilities_count'] == 2
