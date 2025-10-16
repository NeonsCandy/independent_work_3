import click

@click.group()
def cli():
    """Основна CLI-група для команди say."""
    pass

@cli.command()
@click.option("--name", required=True, help="Ім'я для виведення")
def say(name):
    """Виводить ім'я, якщо воно не починається з 'p' або 'P'."""
    if name.lower().startswith("p"):
        print("Ім'я не підходить")
    else:
        print(name)
if __name__ == "__main__":
    cli()