

# export datos a s3
aws dynamodb export-table-to-point-in-time \
    --table-arn arn:aws:dynamodb:us-east-1:834860586869:table/fh_user-notes \
    --s3-bucket fh-user-notes \
    --s3-prefix export-table-fh_user-notes-feb-2-2022 \
    --export-format DYNAMODB_JSON \

aws dynamodb export-table-to-point-in-time \
    --table-arn arn:aws:dynamodb:us-east-1:834860586869:table/fh_token-email-lookup \
    --s3-bucket fh-user-notes \
    --s3-prefix export-table-fh_token-email-lookup-feb-2-2022 \
    --export-format DYNAMODB_JSON \

