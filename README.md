# cp-failures-alerts
This solution will provide alerts on failures occured in AWS CodePipeline

## Commands to run:

`aws cloudformation package --region us-east-1 --template-file runtask-verification.yaml \
--s3-bucket <<s3_bucket>> \
--output-template-file runtask-verification-transformed.yaml`

`aws cloudformation deploy --template-file /home/ec2-user/environment/runtask-verification-transformed.yml --stack-name runtask-verification --parameter-overrides NameOfSolution='runtask-verification' --capabilities CAPABILITY_NAMED_IAM`

Note:
1) Replace s3_bucket with the desired s3 bucket in the format bucket-test (do not use 's3://' syntax)

## Sample output:
Stage: Source failed due to The action failed because no branch named master was found in the selected AWS CodeCommit repository CodePipelineStepFunctionsRepo. Make sure you are using the correct branch name, and then try again. Error: null with errorCode ConfigurationError
