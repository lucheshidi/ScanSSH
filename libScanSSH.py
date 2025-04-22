# -*- coding:utf-8 -*-
# name:----------Jyx
# time:----------2023.1.15
import subprocess
from typing import Union
import os
import platform


def execute_command(command: Union[str, list[str]]) -> str:
    """
    Execute a command (string or list) and return the standard output.
    :param command: Command to run, either as a string or a list of arguments.
    :return: Trimmed output from the process.
    """
    if isinstance(command, str) or isinstance(command, list):
        run_result = subprocess.run(command, shell=isinstance(command, str), stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE, text=True, check=True)
        return run_result.stdout.strip()
    raise ValueError("Command must be a string or a list of strings.")


class libScanSSH:
    """
    A library for scanning SSH services on specified IP and port.
    """

    @staticmethod
    def scan_ip(ip: str, port: int, *custom_args: str) -> str:
        """
        Perform a scan on the given IP and port.
        :param custom_args:
        :param ip: Target IP address.
        :param port: Target Port.
        :return: Scan results as a string.
        """
        if platform.system() == "Windows":
            if custom_args is not None:
                execute_command("ssh -T" + ip + "-p" + port + custom_args)
                if os.getenv("errorlevel") == "0":
                    return True
                else:
                    return False
            else:
                execute_command("ssh -T" + ip + "-p" + port)
                if os.getenv("errorlevel") == "0":
                    return True
                else:
                    return False
        elif platform.system() == "Linux":
            if custom_args is not None:
                execute_command("ssh -T" + ip + "-p" + port + custom_args)
                if os.getenv("?") == "0":
                    return True
                else:
                    return False
            else:
                execute_command("ssh -T" + ip + "-p" + port)
                if os.getenv("?") == "0":
                    return True
                else:
                    return False
        elif platform.system() == "Darwin":
            if custom_args is not None:
                execute_command("ssh -T" + ip + "-p" + port + custom_args)
                if os.getenv("?") == "0":
                    return True
                else:
                    return False
            else:
                execute_command("ssh -T" + ip + "-p" + port)
                if os.getenv("?") == "0":
                    return True
                else:
                    return False
        elif platform.system() == "None":
            return "Unsupported OS"


    @staticmethod
    def scan_from_ip_to_ip(ip_start: str, ip_end: str, port: int, *custom_args: str) -> str:
        if platform.system() == "Windows":
            pass