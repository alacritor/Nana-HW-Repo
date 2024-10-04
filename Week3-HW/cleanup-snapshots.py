#!C:\Users\Hallg\AppData\Local\Programs\Python\Python312\python.exe
# shebang line is used to specify the location of the Python interpreter
import boto3
from operator import itemgetter

ec2_client = boto3.client('ec2', region_name='us-east-1')

snapshots = ec2_client.describe_snapshots(
    Filters=[
            {
                'Name': 'tag:Name',
                'Values': ['prod', 'staging']
            }
        ]
    )

volumes = ec2_client.describe_volumes()

for volume in volumes['Volumes']:
    snapshots =ec2_client.describe_snapshots(
        OwnerIds=['self'],
        Filters=[
            {
                'Name': 'volume-id',
                'Values':[volume['VolumeId']]
            }
        ]
    )
#    print(volume['VolumeId'])

#for snap in sorted_by_date[:2]:
#    response = ec2_client.delete_snapshot(
#        SnapshotId=snap['SnapshotId']
#        
#   )
#    print(response)
#    
#    print(snap['SnapshotId'])
#    print(snap['StartTime'])
#    
#   
#for snap in sorted_by_date:
#   print(snap['StartTime'])
#
#for snap in snapshots ['Snapshots']:
#   print(snap['StartTime'])
#    
#print('###########')
#
#for snap in sorted_by_date:
#    print(snap['StartTime'])
