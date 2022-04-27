
input="47rqunfynuzebpvyunqtlpaeja.json"
tableName="fh-token-email-lookup"
while IFS= read -r line
do
  data=${line:8}
  data=${data%?}
  aws dynamodb put-item \
  --table-name  ${tableName}\
  --item \
  "${data}" 
  echo "Cargando dato a ${tableName}: ${data}}"
done < "$input"

input="fkma3dnxxq7blkevex7pc62zlm.json"
tableName="fh-user-notes"
while IFS= read -r line
do
  data=${line:8}
  data=${data%?}
  aws dynamodb put-item \
  --table-name  ${tableName}\
  --item \
  "${data}" 
  echo "Cargando dato a ${tableName}: ${data}}"
done < "$input"