
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
