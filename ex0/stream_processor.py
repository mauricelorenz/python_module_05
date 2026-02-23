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
        return f"Output: Processed values: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return f"Processing data: {data}"

    def validate(self, data: Any) -> bool:
        try:
            for item in data:
                if data.__class__.__name__ != "int":
                    return False
            return True
        except Exception:
            return False

    def format_output(self, result: str) -> str:
        result_len = 0
        result_sum = 0
        for item in result:
            result_len += 1
            result_sum += item
        result_avg = result_sum / result_len
        return (f"Output: Processed {result_len} numeric values, "
                f"sum={result_sum}, avg={result_avg:.1f}")


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return f"Processing data: {data}"

    def validate(self, data: Any) -> bool:
        return data.__class__.__name__ == "str"

    def format_output(self, result: str) -> str:
        result_chars = 0
        result_spaces = 0
        for char in result:
            result_chars += 1
            if char == " ":
                result_spaces += 1
        return (f"Output: Processed text: {result_chars} "
                f"characters, {result_spaces + 1} words")


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        return f"Processing data: {data}"

    def validate(self, data: Any) -> bool:
        return "INFO" in data or "ERROR" in data

    def format_output(self, result: str) -> str:
        result_info = result.split(":")[1].strip()
        if "INFO" in result:
            return f"Output: [INFO] INFO level detected: {result_info}"
        return f"Output: [ALERT] ERROR level detected: {result_info}"


def main() -> None:
    """Run the main program."""


if __name__ == "__main__":
    main()
