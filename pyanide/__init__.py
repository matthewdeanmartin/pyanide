"""
Kill processes and make them stay dead.
"""
from pyanide.main import kill_current_process, kill_process_by_name, kill_function_on_high_memory_usage

__all__ = ["kill_process_by_name", "kill_current_process", "kill_function_on_high_memory_usage"]
