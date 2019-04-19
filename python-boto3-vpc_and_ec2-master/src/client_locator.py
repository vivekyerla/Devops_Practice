import boto3


class ClientLocator:
    def __init__(self, client):
        self._client = boto3.client(client, region_name="us-east-1", aws_access_key_id="XXX", aws_secret_access_key="XXX")


    def get_client(self):
        return self._client


class EC2Client(ClientLocator):
    def __init__(self):
        super().__init__('ec2')