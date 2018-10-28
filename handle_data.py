import pickle
import sys
import subprocess

cities = [
'Albuquerque',
'Atlanta',
'Austin',
'Baltimore',
'Boise',
'Boston',
'Charlotte',
'Chicago',
'Cincinnati',
'Cleveland',
'Colorado Springs',
'Columbus',
'Columbus',
'Dallas',
'Denver',
'Detroit',
'Fort Worth',
'Houston',
'Indianapolis',
'Jacksonville',
'Kansas City',
'Kansas City',
'Las Vegas',
'Los Angeles',
'Louisville',
'Madison',
'Memphis',
'Miami',
'Milwaukee',
'Minneapolis',
'Nashville',
'New Orleans',
'New York',
'Oakland',
'Oklahoma City',
'Omaha',
'Philadelphia',
'Phoenix',
'Pittsburgh',
'Portland',
'Portland',
'Raleigh',
'Sacramento',
'San Antonio',
'San Diego',
'San Francisco',
'San Jose',
'Seattle',
'St. Louis',
'Tampa',
'Tucson',
'Tulsa'
]

if __name__ == '__main__':    
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    #cd_command = 'cd /Users/hyacinth/workspace/AirbnbScraper'
    #print(cd_command)
    #process = subprocess.Popen(cd_command, shell=True, stdout=subprocess.PIPE)
    #process.wait()

    command = "scrapy crawl listing -a query='{city}' -o '{city}.json'"
    command2 = "python convert_json.py '{city}.json'"
    for city in cities[start:end]: 
        print(command.format(city=city))
        process = subprocess.Popen(command.format(city=city), shell=True)
        process.wait()

        print(command2.format(city=city))
        process2 = subprocess.Popen(command2.format(city=city), shell=True)
        process2.wait()
