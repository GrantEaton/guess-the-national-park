from os import listdir, path
from collections import defaultdict
import subprocess
import json


parks = [
    'capitol_reef_national_park',
    'petrified_forest_national_park',
    'mesa_verde_national_park',
    'wrangell_\xe2\x80\x93_st._elias_national_park_and_preserve',
    'wrangell_-_st._elias_national_park_and_preserve',
    'everglades_national_park',
    'isle_royale_national_park',
    'dry_tortugas_national_park',
    '.DS_Store',
    'cuyahoga_valley_national_park',
    'glacier_national_park',
    'grand_teton_national_park',
    'gates_of_the_arctic_national_park',
    'badlands_national_park',
    'guadalupe_mountains_national_park',
    'kenai_fjords_national_park',
    'sequoia_national_park',
    'bryce_canyon_national_park',
    'nationalParks.py',
    'glacier_bay_national_park',
    'lake_clark_national_park',
    'voyageurs_national_park',
    'wind_cave_national_park',
    'volcanoes_national_park',
    'katmai_national_park_and_preserve',
    'hot_springs_national_park',
    'denali_national_park_and_preserve',
    'acadia_national_park',
    'american_samoa_national_park',
    '__pycache__',
    'north_cascades_national_park',
    'congaree_national_park',
    'grand_canyon_national_park',
    'joshua_tree_national_park',
    'canyonlands_national_park',
    'death_valley_national_park',
    'great_basin_national_park',
    'olympic_national_park',
    'big_bend_national_park',
    'theodore_roosevelt_national_park',
    'rocky_mountain_national_park',
    'lassen_volcanic_national_park',
    'shenandoah_national_park',
    'redwood_national_park',
    'yellowstone_national_park',
    'mount_rainier_national_park',
    'haleakala_national_park',
    'carlsbad_caverns_national_park',
    'arches_national_park',
    'channel_islands_national_park',
    'saguaro_national_park',
    'great_smoky_mountains_national_park',
    'yosemite_national_park',
    'zion_national_park',
    'virgin_islands_national_park',
    'kings_canyon_national_park',
    'crater_lake_national_park',
    'kobuk_valley_national_park',
    'great_sand_dunes_national_park_and_preserve',
    'mammoth_cave_national_park',
]

def index_park_images():
    db = defaultdict(list)
    for park in [d for d in parks if path.isdir('../data/' + d)]:
        for fname in [f for f in listdir('../data/' + park) if f != '.DS_Store']:
            db[park].append(fname)
        
        process = subprocess.Popen(f'cp ../data/{park}/* ../db/', stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        if error:
            print(output)
        
        with open('../db/db.json', 'w') as outfile:  
            json.dump(db, outfile, indent=2)


def main():
    index_park_images()

if __name__ == '__main__':
    main()