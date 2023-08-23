from abc import ABC, abstractmethod


class Command:
    @abstractmethod
    def execute_command(self):
        raise NotImplementedError
