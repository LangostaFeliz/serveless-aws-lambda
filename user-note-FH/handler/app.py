import json
import boto3
from boto3.dynamodb.types import TypeDeserializer, TypeSerializer
# import requests
client=boto3.client("dynamodb")

def from_dynamodb_to_json(item):
    d = TypeDeserializer()
    return {k: d.deserialize(value=v) for k, v in item.items()}

def generateResponse(statusCode,dataKey,data):

    return {
        "statusCode": statusCode,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({dataKey:data})
    }

def getUserNotes(event, context):
    headers=event["headers"]
    
    if headers.get("Bearer") == None:
        return generateResponse(403,"message","The Authentication header is malformed or missing.")
    
    
    item = client.get_item(TableName="fh-token-email-lookup",Key={"token":{'S':headers.get("Bearer")}})
    if item.get("Item") == None:
        return generateResponse(400,"message","Token is invalid or empty (Bearer ).")
    user=item["Item"].get("email").get('S')


    name={"#user":'user'}
    items=client.query(TableName="fh-user-notes",
                    ScanIndexForward=False,
                    KeyConditionExpression="#user = :email",
                    ExpressionAttributeNames=name,
                    ExpressionAttributeValues={':email': {'S':user}},
                    Limit=10
                    )
    
    datas=[]
    for data in items["Items"]:
        datas.append(from_dynamodb_to_json(data))

    return generateResponse(200,"data",datas)