import os.path
import subprocess

parks = [
    "Acadia National Park",
    "Arches National Park",
    "Badlands National Park",
    "Big Bend National Park",
    "Biscayne National Park"
    "Black Canyon of the Gunnison National Park",
    "Bryce Canyon National Park",
    "Canyonlands National Park",
    "Capitol Reef National Park",
    "Carlsbad Caverns National Park",
    "Channel Islands National Park",
    "Congaree National Park",
    "Crater Lake National Park",
    "Cuyahoga Valley National Park",
    "Death Valley National Park",
    "Denali National Park and Preserve",
    "Dry Tortugas National Park",
    "Everglades National Park",
    "Gates of the Arctic National Park",
    "Glacier Bay National Park",
    "Glacier National Park",
    "Grand Canyon National Park",
    "Grand Teton National Park",
    "Great Basin National Park",
    "Great Sand Dunes National Park and Preserve",
    "Great Smoky Mountains National Park",
    "Guadalupe Mountains National Park",
    "Haleakala National Park",
    "Volcanoes National Park",	
    "Hot Springs National Park",
    "Isle Royale National Park",
    "Joshua Tree National Park",
    "Katmai National Park and Preserve",
    "Kenai Fjords National Park",
    "Kings Canyon National Park",
    "Kobuk Valley National Park",
    "Lake Clark National Park",
    "Lassen Volcanic National Park",
    "Mammoth Cave National Park",
    "Mesa Verde National Park",
    "Mount Rainier National Park",
    "American Samoa National Park",
    "North Cascades National Park",
    "Olympic National Park",
    "Petrified Forest National Park",
    "Redwood National Park",
    "Rocky Mountain National Park",
    "Saguaro National Park",
    "Sequoia National Park",
    "Shenandoah National Park",
    "Theodore Roosevelt National Park",
    "Virgin Islands National Park",
    "Voyageurs National Park",
    "Wind Cave National Park",
    "Wrangell – St. Elias National Park and Preserve",
    "Yellowstone National Park",
    "Yosemite National Park",
    "Zion National Park"
]


for park in parks:
    park_snake_case = park.replace(" ", "_").lower()
    dir_path = '../data/' + park_snake_case

    if not os.path.exists(dir_path):
        # create directory
        os.makedirs(dir_path)
    
    path, dirs, files = os.walk(dir_path).__next__()
    file_count = len(files)

    if file_count < 25: 
        files = 25 - file_count

        # run script to download images
        park_with_quotes = '"' + park + '"'
        bash_command = ['googleimagesdownload', '--keywords', park_with_quotes,  '--limit', str(files)]
        process = subprocess.Popen(bash_command, stdout=subprocess.PIPE, cwd=dir_path)
        output, error = process.communicate()
        print(output)

        # move pictures into parent dir
        park_with_backslashes = '\\"' + park + '\\"'
        park_with_backslashes = park_with_backslashes.replace(" ", "\ ")
        print(park_with_backslashes)
        bash_command = ['mv', "./downloads/" + park_with_backslashes + "/*", "./"]
        print(bash_command)
        process = subprocess.Popen(bash_command, stdout=subprocess.PIPE, cwd=dir_path)
        
        # delete downloads folder
        bash_command = ['rm', "-r" "./downloads"]
        process = subprocess.Popen(bash_command, stdout=subprocess.PIPE, cwd=dir_path)

        print("Finished with " + park + "!")

