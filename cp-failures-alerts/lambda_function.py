import json
import os
import logging
import boto3
import sys
logger = logging.getLogger()
logger.setLevel(logging.INFO)

cp_client=boto3.client('codepipeline')
sns_client = boto3.client('sns')
sns_topic_arn=os.getenv(sns_topic_arn)

def cp-failures-alerts(event, context):
    #Setting params
    pipelineName=event['detail']['pipeline']
    executionID=event['detail']['execution-id']
    state=event['detail']['state']
    stage=event['detail']['stage']
    
    #Getting  pipeline status on basis of the above executionID
    response=cp_client.get_pipeline_state(name=pipelineName)
    
    print ("Printing stage level issues")
    for i in response['stageStates']:
        if i['actionStates'][0].get('latestExecution') is not None:
            errorMessage=i['actionStates'][0]['latestExecution']['errorDetails']['message']
            errorCode=i['actionStates'][0]['latestExecution']['errorDetails']['code']
            message="Stage: "+stage+" failed due to "+errorMessage+" with errorCode "+errorCode
    #Sending alerts
    send_notification(message)
    
def send_notification(message):
    response = sns_client.publish(
    TopicArn=sns_topic_arn,   
    Message=message
    )
