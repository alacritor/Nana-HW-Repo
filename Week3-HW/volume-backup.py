#!C:\Users\Hallg\AppData\Local\Programs\Python\Python312\python.exe
# shebang line is used to specify the location of the Python interpreter
import boto3
import schedule

ec2_client = boto3.client('ec2', region_name='us-east-1')
def create_volume_snapshots():
    volumes = ec2_client.describe_volumes(
        Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod', 'staging']
            }
        ]
    )
       
    for volume in volumes['Volumes']:
        new_snapshot = ec2_client.create_snapshot(
            VolumeId=volume['VolumeId']
        )
        print(new_snapshot)


schedule.every(60).seconds.do(create_volume_snapshots)

while True:
    schedule.run_pending()        