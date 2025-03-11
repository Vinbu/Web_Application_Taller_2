import typer

app = typer.Typer()

@app.command()
def encrypt(message : str, key: str):
    
@app.command()
def decrypt(key : str):
    