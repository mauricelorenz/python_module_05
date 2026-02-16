#!/usr/bin/env python3

from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        print(f"Output: Processed values: {result}")


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        print(f"Processing data: {data}")

    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        print(f"Output: Processed values: {result}")


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        pass

    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        print(f"Output: Processed values: {result}")


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        pass

    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        print(f"Output: Processed values: {result}")


def main() -> None:
    """Run the main program."""


if __name__ == "__main__":
    main()
