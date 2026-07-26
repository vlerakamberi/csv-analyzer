import logging

logger = logging.getLogger(__name__)


def validate_data(df):
    """Verifikon që të dhënat kanë kuptim logjik, jo vetëm që janë 'plot'."""
    problems = []

    if (df["Age"] < 0).any() or (df["Age"] > 100).any():
        problems.append("Ka mosha jo-realiste (negative ose mbi 100)")

    if not df["Pclass"].isin([1, 2, 3]).all():
        problems.append("Ka vlera Pclass jashtë 1, 2, 3")

    if not df["Survived"].isin([0, 1]).all():
        problems.append("Ka vlera Survived jashtë 0 ose 1")

    if problems:
        for p in problems:
            logger.error(p)
        raise ValueError("Të dhënat dështuan validimin, shiko errors sipër")

    logger.info("Validimi i të dhënave kaloi me sukses")
    return df