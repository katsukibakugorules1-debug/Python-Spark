"""Advanced diagnostics module for SPARK — no GPU version."""

import psutil
import time
import socket
import platform


def ping_test(host="8.8.8.8"):
    """Returns network latency in ms or None if unreachable."""
    try:
        start = time.time()
        socket.create_connection((host, 53), timeout=2)
        end = time.time()
        return round((end - start) * 1000, 2)
    except OSError:
        return None


def handle(command: str, user: str) -> str:
    command = command.lower().strip()

    # Basic status
    if command == "spark status":
        return "Systems online. Monitoring active."

    # Advanced diagnostics
    if command == "spark diagnostics":
        cpu = psutil.cpu_percent(interval=1)
        per_cpu = psutil.cpu_percent(interval=1, percpu=True)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        battery = psutil.sensors_battery()
        temps = psutil.sensors_temperatures()
        latency = ping_test()

        # Temperature output
        temp_output = "No temperature sensors detected."
        if temps:
            temp_output = "\n".join(
                f"- {chip}: {t.current}°C"
                for chip, readings in temps.items()
                for t in readings
            )

        # Battery output
        battery_output = "No battery detected."
        if battery:
            battery_output = (
                f"{battery.percent}% ({'Charging' if battery.power_plugged else 'Not charging'})"
            )

        return (
            "Running advanced diagnostics...\n"
            f"- CPU Load: {cpu}%\n"
            f"- Per-Core Load: {per_cpu}\n"
            f"- Memory: {memory.percent}% used ({memory.used // (1024**2)} MB)\n"
            f"- Disk: {disk.percent}% used\n"
            f"- Battery: {battery_output}\n"
            f"- GPU: Not present on this system\n"
            f"- Temperatures:\n{temp_output}\n"
            f"- Network Latency: {latency if latency else 'Disconnected'}\n"
            f"- OS: {platform.system()} {platform.release()}\n"
            f"- Python Version: {platform.python_version()}\n"
            "Advanced diagnostics complete."
        )

    # Reboot (simulated)
    if command == "spark reboot":
        return "Reboot sequence initiated. (Simulated)"

    # Shutdown (simulated)
    if command == "spark shutdown":
        return "Shutdown sequence initiated. (Simulated)"

    # Version info
    if command == "spark version":
        return "SPARK Core v1.0 — prototype build."

    return "System module: unknown system command."
