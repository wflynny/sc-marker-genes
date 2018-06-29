#!/usr/bin/env python3
import os
import json
import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument('cl_id', help="Cell Onotology ID")
parser.add_argument('gene_names', nargs='+',
                    help="Comma or space separated gene names")
parser.add_argument('-s', '--species', choices=['hsapiens', 'mmusculus'],
                    default='hsapiens')
args = parser.parse_args()
if len(args.gene_names) > 1:
    args.gene_names = ','.join(args.gene_names)
args.gene_names = args.gene_names.upper()

biomart_xml=('<?xml version="1.0" encoding="UTF-8"?>'
             '<!DOCTYPE Query>'
             '<Query virtualSchemaName = "default" formatter = "CSV" header ='
             '"0" uniqueRows = "0" count = "" datasetConfigVersion = "0.6" >'
             f'<Dataset name = "{args.species}_gene_ensembl" interface = "default" >'
             f'<Filter name = "external_gene_name" value ="{args.gene_names}"/>'
             '<Attribute name = "external_gene_name" />'
             '<Attribute name = "ensembl_gene_id" /></Dataset></Query>')
biomart_url=f"http://www.ensembl.org/biomart/martservice?query={biomart_xml}"

biomart_req = requests.get(biomart_url)
biomart_response = biomart_req.content.decode('ascii').strip().split('\n')

ols_url = ("https://www.ebi.ac.uk/ols/api/ontologies/cl/terms?"
           f"iri=http://purl.obolibrary.org/obo/{args.cl_id}")
ols_req = requests.get(ols_url)
cell_type_info = json.loads(ols_req.content.decode('ascii'))
cell_type = cell_type_info.get('_embedded').get('terms')[0].get('label')
cell_type = cell_type.lower().replace(', ', '_').replace(' ', '_')

write_mode = 'w'
outfile = f"{args.cl_id}.{cell_type}.csv"
if os.path.exists(outfile):
    write_mode = 'a'

full_species = {'hsapiens': 'homo sapiens', 'mmusculus': 'mus musculus'}
with open(outfile, write_mode) as fout:
    for line in sorted(biomart_response):
        items = line.split(',') + ['', '']
        items.insert(1, full_species[args.species])
        fout.write(','.join(items) + '\n')
print(f"Saved {len(biomart_response)} genes to [{outfile}].")
