# cp-failures-alerts
This solution will provide alerts on failures occured in AWS CodePipeline. By design, CodePipeline provides Action/Stage/Pipeline level events. Stage level events based invocation will be helpful in understanding failures on all actions within a stage and in any given stage within a pipeline.

## Commands to run:

These commands were tested on an ec2 instance

`aws cloudformation package --region us-east-1 --template-file cp-failures-alerts.yaml \
--s3-bucket <<s3_bucket>> \
--output-template-file cp-failures-alerts-transformed.yaml`

`aws cloudformation deploy --template-file /home/ec2-user/cp-failures-alerts-transformed.yaml --stack-name cp-failures-alerts --parameter-overrides NameOfSolution='cp-failures-alerts' --capabilities CAPABILITY_NAMED_IAM`

Note:
1) Replace s3_bucket with the desired s3 bucket in the format bucket-test (do not use 's3://' syntax)

## Sample output:
Stage: Source failed due to The action failed because no branch named master was found in the selected AWS CodeCommit repository CodePipelineStepFunctionsRepo. Make sure you are using the correct branch name, and then try again. Error: null with errorCode ConfigurationError
