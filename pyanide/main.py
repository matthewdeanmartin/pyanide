"""
This module contains functions for killing processes.
"""

import ctypes
import functools
import os
import signal
import time

import psutil


def kill_process_by_name(name: str, interval: int, max_cycles: int = 10) -> None:
    """Kills a process by name and periodically checks if it has come back.

    Created with help from ChatGPT.
    """
    cycle = 0
    while True and cycle < max_cycles:
        cycle += 1
        # Check if the process is running
        for process in psutil.process_iter(["pid", "name"]):
            if process.info["name"] == name:
                # Kill the process
                process.kill()
                print(f"Killed process {name}")
        # Wait for the interval
        time.sleep(interval)


def kill_current_process() -> None:
    """Kills the current process.

    Created with help from ChatGPT.
    """
    if os.name == "nt":
        # Get the process handle
        handle = ctypes.windll.kernel32.OpenProcess(1, False, os.getpid())
        # Terminate the process
        ctypes.windll.kernel32.TerminateProcess(handle, -1)
    else:
        # Use the Unix-specific signal.SIGTERM signal to kill the process
        pid = os.getpid()
        os.kill(pid, signal.SIGTERM)


def kill_function_on_high_memory_usage(max_memory_usage: int):
    """Kills a function if it uses too much memory."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            process = psutil.Process(os.getpid())
            rss_before = process.memory_info().rss

            result = func(*args, **kwargs)

            rss_after = process.memory_info().rss
            rss_used = rss_after - rss_before

            if rss_used > max_memory_usage:
                os.kill(os.getpid(), signal.SIGTERM)
                raise MemoryError(f"Function {func.__name__} exceeded maximum memory usage of {max_memory_usage} bytes")

            return result

        return wrapper

    return decorator
