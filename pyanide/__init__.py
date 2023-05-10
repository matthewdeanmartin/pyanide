"""
Kill processes and make them stay dead.
"""
from pyanide.main import (
    kill_current_process,
    kill_function_on_high_memory_usage,
    kill_process_by_name,
)

__all__ = ["kill_process_by_name", "kill_current_process", "kill_function_on_high_memory_usage"]
