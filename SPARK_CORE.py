"""Core command handler for SPARK."""

import sys

SPARK_NAME = "SPARK"
SPARK_FULL_NAME = "Smart Personalized Automation & Responsive Knowledge"
USER_NAME = "User"

# Identity registry
IDENTITIES = {
    "Noah": {"relationship": "Creator", "notes": "Master user. Full override."},
    "Mom": {"relationship": "Parent", "notes": "Co-administrator."},
    "Christian": {"relationship": "Brother", "notes": "Household member."},
    "Jakob": {"relationship": "Brother", "notes": "Household member."},
    "Mea": {"relationship": "Frequent Visitor", "notes": "Trusted non-resident."},
    "Kelly": {"relationship": "Frequent Visitor", "notes": "Trusted non-resident."},
    "Wynn": {"relationship": "Frequent Visitor", "notes": "Trusted non-resident."},
}

# Authority levels
AUTHORITY = {
    "Unknown": 0,
    "Guest": 1,
    "Mea": 2,
    "Kelly": 2,
    "Wynn": 2,
    "Christian": 3,
    "Jakob": 3,
    "Mom": 4,
    "Noah": 5,
}

# Command requirements
COMMAND_LEVELS = {
    "spark activate": 1,
    "spark identify": 1,
    "spark status": 1,
    "spark reboot": 3,
    "spark shutdown": 3,
    "spark diagnostics": 2,
    "spark protocols": 1,
    "spark personality": 1,
    "spark version": 1,
    "spark intruder protocol": 4,
    "spark allow entry": 4,
    "spark tornado exception": 4,
}

# Routing table: command prefix → module
ROUTES = {
    "spark intruder": "security",
    "spark allow": "security",
    "spark tornado": "security",
    "spark identify": "identity",
    "spark personality": "personality",
    "spark diagnostics": "system",
    "spark reboot": "system",
    "spark shutdown": "system",
    "spark status": "system",
    "spark lights": "room",
    "spark music": "room",
}


def check_authority(user: str, command: str) -> bool:
    """Return True if user has permission to run the command."""
    level = AUTHORITY.get(user, 0)
    required = COMMAND_LEVELS.get(command, 1)
    return level >= required


def route_command(command: str):
    """Return the module name responsible for this command."""
    for prefix, module in ROUTES.items():
        if command.startswith(prefix):
            return module
    return None


def interpret(command: str, user: str = "Unknown") -> str:
    """Return SPARK's response to a supported command with authority checking."""
    command = command.strip().lower()

    # Intruder detection
    if user == "Unknown":
        return "⚠ Intruder detected. Activating intruder protocol."

    # Authority check
    if not check_authority(user, command):
        return f"Access denied for {user}. Required authority level too high."

    # Original commands
    if command == "spark activate":
        return f"{SPARK_NAME} online. Systems calibrated."

    if command == "spark identify":
        return f"I am {SPARK_NAME}, {SPARK_FULL_NAME}."

    if command == "spark status":
        return "All systems stable and awaiting your instruction."

    if command == "spark reboot":
        return "Rebooting core systems. Stand by."

    if command == "spark shutdown":
        return "Shutting down non-essential systems."

    if command == "spark diagnostics":
        return "Running diagnostics. CPU stable. Memory stable. No anomalies detected."

    if command == "spark protocols":
        return (
            "Available protocols: activate, identify, status, reboot, shutdown, "
            "diagnostics."
        )

    if command == "spark personality":
        return "Personality module active. Tone: analytical with mild sass."

    if command == "spark version":
        return "SPARK Core v1.0 — prototype build."

    if command == "spark intruder protocol":
        return "Intruder protocol simulated. Lights flashing. Alarm active."

    if command == "spark allow entry":
        return "Entry authorized. No security actions triggered."

    if command == "spark tornado exception":
        return "Tornado exception recognized. Entry allowed."

    return "Unrecognized command. Use SPARK-specific protocols."


def main() -> None:
    command = " ".join(sys.argv[1:]) or input("SPARK> ")
    print(interpret(command, user="Noah"))


if __name__ == "__main__":
    main()
