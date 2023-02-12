import click
import requests


@click.command("push")
@click.argument("text")
def push_to_dapr():
    requests.post("http://localhost:8000")