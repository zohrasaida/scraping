from fastapi import FastAPI
from typing import Optional
import facebook
import json
import pymongo

app = FastAPI()

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.get("/page/description")
async def read_description(access_token: Optional[str] = None):
    if access_token is None:
        access_token= "EAAITrojGrNIBAAsW8lwIIz5DQ10vSRXnhWeC5b5rZBvjDrZBOYG2H5gx36RZCmU1cWgVojfAGFZBZADIBT5JRA0PsDZAmrnyJweXH39wuDPKTnCNs81I7BPVopyD9aj10QwuIEleI5IZAC6ZCTSLPT3UQcZB0AFIVEUblp2KiIseZCBYNWgDXh3SxSUNRvgGsnHvAZD"
    page_id = 511313695586831
    graph = facebook.GraphAPI(access_token=access_token)

    description_json= {
        "page_description" : graph.get_object(str(page_id)+"/?fields=description,emails,about,fan_count,engagement,picture{url},has_whatsapp_number,name")
    }

    #database creation
    dbClient = pymongo.MongoClient('mongodb://localhost:27017/')
    database = dbClient['facebook_scraping']
    collection = database['EJE_description']

    collection.insert_one(description_json)
    return description_json

@app.get("/page")
async def read_item(access_token: Optional[str] = None):
    if access_token is None:
        access_token= "EAAITrojGrNIBAAsW8lwIIz5DQ10vSRXnhWeC5b5rZBvjDrZBOYG2H5gx36RZCmU1cWgVojfAGFZBZADIBT5JRA0PsDZAmrnyJweXH39wuDPKTnCNs81I7BPVopyD9aj10QwuIEleI5IZAC6ZCTSLPT3UQcZB0AFIVEUblp2KiIseZCBYNWgDXh3SxSUNRvgGsnHvAZD"
    page_id = 511313695586831
    graph = facebook.GraphAPI(access_token=access_token)

    posts = graph.get_object(str(page_id)+"/posts")
    output_json= {
        "page_description" : graph.get_object(str(page_id)+"/?fields=description,emails,about,fan_count,engagement,picture{url},has_whatsapp_number,name"),
        "events" : graph.get_object(str(page_id)+"/events"),
        "videos": graph.get_object(str(page_id)+ "/videos")
    }

    #database creation
    dbClient = pymongo.MongoClient('mongodb://localhost:27017/')
    database = dbClient['facebook_scraping']
    collection = database['EJE_Page']

    collection.insert_one(output_json)
    return output_json