from urllib.parse import quote
import json, requests
from secrets_parser import parse

database_uri=parse("variables.txt")["database_uri"]

def get(table, key):
    out=requests.get(database_uri+"/get?key="+quote(table+"/"+key)).text
    response=json.loads(out)
    if response["Ok"]:
        response["Value"]=json.loads(response["Value"])
    return response

def set(table, key, val):
    requests.get(database_uri+"/set?key="+quote(table+"/"+key)+"&val="+quote(json.dumps(val)))