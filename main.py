import click
import boto3

@click.group()
def cli():
    """AWS CLI Tool"""
    pass

@cli.command()
@click.argument('bucket_name')
def create_bucket(bucket_name):
    """Create an S3 bucket"""
    s3 = boto3.client('s3')
    s3.create_bucket(Bucket=bucket_name)
    click.echo(f'Bucket {bucket_name} created!')

@cli.command()
@click.argument('instance_id')
def start_instance(instance_id):
    """Start an EC2 instance"""
    ec2 = boto3.client('ec2')
    ec2.start_instances(InstanceIds=[instance_id])
    click.echo(f'Instance {instance_id} started!')

@cli.command()
@click.argument('instance_id')
def stop_instance(instance_id):
    """Stop an EC2 instance"""
    ec2 = boto3.client('ec2')
    ec2.stop_instances(InstanceIds=[instance_id])
    click.echo(f'Instance {instance_id} stopped!')

if __name__ == '__main__':
    cli()
