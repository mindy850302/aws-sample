import boto3
import pandas

AWS_ACCESS_KEY_ID = 'YOUR_AWS_ACCESS_KEY_ID'
AWS_SECRET_ACCESS_KEY = 'YOUR_AWS_SECRET_ACCESS_KEY'

# connect to s3
s3 = boto3.client(
's3',
aws_access_key_id=AWS_ACCESS_KEY_ID,
aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)

listOfObject = []
resp = s3.list_objects_v2(Bucket='your-bucket-name')

for obj in resp['Contents']:
    # list key of object 
    listOfObject.append(obj['Key'])
    print(obj['Key'])

    
print(listOfObject)

# list to DataFrame
listDataFrame = pandas.DataFrame(listOfObject)
# export to csv
listDataFrame.to_csv('list.csv')