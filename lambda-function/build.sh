export account_id="your-account-id-here"

aws ecr get-login-password \
    --region us-east-1 | docker login \
    --username AWS \
    --password-stdin ${account_id}.dkr.ecr.us-east-1.amazonaws.com

aws ecr create-repository \
    --region us-east-1 \
    --repository-name timescale-insert > /dev/null
     

docker build \
    -t ${account_id}.dkr.ecr.us-east-1.amazonaws.com/timescale-insert:latest .

docker push \
    ${account_id}.dkr.ecr.us-east-1.amazonaws.com/timescale-insert:latest

aws lambda update-function-code \
    --function-name timescale-insert \
    --image-uri ${account_id}.dkr.ecr.us-east-1.amazonaws.com/timescale-insert:latest > /dev/null