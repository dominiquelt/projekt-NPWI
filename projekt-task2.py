
import os
import argparse
import json
import xmltodict
import yaml

parser = argparse.ArgumentParser(description="konwerter plikow")

parser.add_argument('input_f', type=str,)
parser.add_argument('output_f', type=str)

args = parser.parse_args()

input_f = args.input_f
output_f = args.output_f

if os.path.isfile(args.input_f):
    print('conversion begins!')
else:
    print(f"requested input: {args.input_f} does not exist")
    exit(1)

if input_f.endswith(".yml") or input_f.endswith(".yaml"):
    with open(input_f, 'r') as y:
        try:
            data = yaml.safe_load(y)
        except yaml.YAMLError as e:
            print("Parsowanie pliku yaml nie powiodlo sie", e)
            exit(1)
elif input_f.endswith(".json"):
    with open(input_f, 'r') as j:
        try:
            data = json.load(j)
        except json.JSONDecodeError as e:
            print("Parsowanie pliku json nie powiodlo sie", e)
            exit(1)
elif input_f.endswith(".xml"):
    with open(input_f, 'r') as x:
        try:
            data = xmltodict.parse(x.read())
        except xmltodict.ExpatError as e:
            print("Parsowanie pliku xml nie powiodlo sie", e)
            exit(1)
