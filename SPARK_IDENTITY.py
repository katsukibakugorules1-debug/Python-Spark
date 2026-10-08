"""Identity module for SPARK."""

from SPARK_CORE import IDENTITIES, AUTHORITY


def handle(command: str, user: str) -> str:
    command = command.lower()

    # SPARK self-identification
    if command == "spark identify":
        return "I am SPARK, Smart Personalized Automation & Responsive Knowledge."

    # List all known identities
    if command == "spark list identities":
        names = ", ".join(IDENTITIES.keys())
        return f"Known identities: {names}"

    # Authority lookup
    if command.startswith("spark authority"):
        parts = command.split()
        if len(parts) < 3:
            return "Specify a name to check authority."
        name = parts[2].capitalize()
        level = AUTHORITY.get(name)
        if level is None:
            return f"No identity found for {name}."
        return f"{name} has authority level {level}."

    # Relationship lookup
    if command.startswith("spark relationship"):
        parts = command.split()
        if len(parts) < 3:
            return "Specify a name to check relationship."
        name = parts[2].capitalize()
        info = IDENTITIES.get(name)
        if info is None:
            return f"No identity found for {name}."
        return f"{name}: {info['relationship']} — {info['notes']}"

    # Describe a person
    if command.startswith("spark who is"):
        parts = command.split()
        if len(parts) < 4:
            return "Specify a name to identify."
        name = parts[3].capitalize()
        info = IDENTITIES.get(name)
        if info is None:
            return f"No identity found for {name}."
        level = AUTHORITY.get(name, 0)
        return (
            f"{name}: {info['relationship']} — {info['notes']} "
            f"(Authority level {level})"
        )

    return "Identity module: unknown identity command."
