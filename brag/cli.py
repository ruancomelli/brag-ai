import logging

from typer import Typer

logger = logging.getLogger(__name__)
app = Typer()


@app.command()
def generate(
    user: str,
    from_date: str,
    to_date: str,
    format: str,
) -> None:
    logger.info(
        f"Generating brag document for {user} from {from_date} to {to_date} in {format} format"
    )
