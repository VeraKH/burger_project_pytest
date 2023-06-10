from dataclasses import dataclass


@dataclass
class Person:
    name: str = None
    email: str = None
    password: str = None
    incorrect_password: str = None
