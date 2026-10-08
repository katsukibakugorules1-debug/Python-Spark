"""Security module for SPARK."""

def handle(command: str, user: str) -> str:
    command = command.lower()

    if "intruder" in command:
        return "Intruder protocol activated. Lights flashing. Alarm simulated."

    if "allow" in command:
        return "Entry authorized. Security systems standing down."

    if "tornado" in command:
        return "Tornado exception recognized. Entry allowed."

    return "Security module: unknown security command."
