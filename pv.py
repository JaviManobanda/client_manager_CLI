import click
from clients import command as clients_commands

CLIENTS_TABLE = '.clients.csv'


@click.group()  # definimos que es el punto de entrada
@click.pass_context  # definimos el contexto
def cli(ctx):
    ctx.obj = {}
    ctx.obj['clients_table'] = CLIENTS_TABLE


cli.add_command(clients_commands.all)
