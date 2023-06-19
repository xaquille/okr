import argparse
import os 
import json
import os

# os.system('wafw00f spentera.id -o spentera.id.json')

# Create the parser
parser = argparse.ArgumentParser("tes.py -u google.com")
# Add an argument
parser.add_argument('-u', type=str, required=True)
# Parse the argument
args = parser.parse_args()
# Print the user input argument
print(args.u)
domain = args.u
os.system('wafw00f '+domain+' -o wafwoof/'+domain+'.json')


# Opening JSON file
# f = open('spentera.id.json')
# data = json.load(f)
# print (data[0]["firewall"])