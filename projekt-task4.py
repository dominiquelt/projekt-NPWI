
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

def xml_json_write():
    jsondata=json.dumps(data,indent=4)
    with open(output_f,"w") as json_f:
        json_f.write(jsondata)

def yaml_json_write():
    with open(output_f,"w") as json_f:
        json.dump(data,json_f, indent=4)

def xml_yaml_write():
    yamldata = yaml.dump(data, indent=4)
    with open(output_f, "w") as yml_f:
        yml_f.write(yamldata)

def json_yaml_write():
    with open(output_f,"w") as json_f:
        yaml.dump(data,json_f,indent=4)

def yaml_xml_write():
    with open(output_f, "w") as xml_f:
        xmldata=xmltodict.unparse(data,pretty=True)
        xml_f.write(xmldata)

def json_xml_write():
    with open(output_f, "w") as xml_f:
        xmldata = xmltodict.unparse(data, pretty=True)
        xml_f.write(xmldata)


def inputisoutput():
    print("provided with the same format for the input as well as the output")
    exit(1)

if input_f.endswith(".json"):
    if output_f.endswith(".json"):
        inputisoutput()
    elif output_f.endswith(".xml"):
        json_xml_write()
    elif output_f.endswith(".yaml") or output_f.endswith(".yml"):
        json_yaml_write()
elif input_f.endswith(".xml"):
    if output_f.endswith(".xml"):
        inputisoutput()
    elif output_f.endswith(".json"):
        xml_json_write()
    elif output_f.endswith(".yaml") or output_f.endswith(".yml"):
        xml_yaml_write()
elif input_f.endswith(".yaml") or input_f.endswith(".yml"):
    if output_f.endswith(".yaml") or output_f.endswith(".yml"):
        inputisoutput()
    elif output_f.endswith(".xml"):
        yaml_xml_write()
    elif output_f.endswith(".json"):
        yaml_json_write()







            
