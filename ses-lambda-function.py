import json
import boto3


ses = boto3.client('sesv2')


def lambda_handler(event, context):
    action = event['Records'][0]['eventName']
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    
    response = ses.send_email(
        FromEmailAddress = "irshathmohamed786@gmail.com",
        Destination={
            'ToAddresses':[
                'irshathmohamed786@gmail.com']
        },
        Content={
            'Simple':{
                'Subject':{
                    'Data': 'Action on S3 bucket'
                },
                'Body':{
                    'Text':{
                        'Data':'Bucket Action: ' + action +'\n' + 'Bucket Name: ' + bucket_name
                    }
                }
            }
        },
        EmailTags=[
        {
            'Name': 'Main',
            'Value': 'Bucket'
        },]
    )
