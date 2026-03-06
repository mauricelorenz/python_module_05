#!/usr/bin/env python3

from typing import Any
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        return (f"Processed {len(data)} numeric values, "
                f"sum={sum(data)}, avg={sum(data)/len(data):.1f}")

    def validate(self, data: Any) -> bool:
        try:
            for item in data:
                if not isinstance(item, int):
                    return False
            return True
        except TypeError:
            return False

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        return (f"Processed text: {len(data)} characters, "
                f"{len(data.split())} words")

    def validate(self, data: Any) -> bool:
        return (isinstance(data, str) and "INFO" not in data and
                "ERROR" not in data)

    def format_output(self, result: str) -> str:
        return (f"Output: {result}")


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def process(self, data: Any) -> str:
        result_info = data.split(":")[1].strip()
        if "INFO" in data:
            return f"[INFO] INFO level detected: {result_info}"
        return f"[ALERT] ERROR level detected: {result_info}"

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ("INFO" in data or "ERROR" in data)

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    print("\nInitializing Numeric Processor...")
    num_data = [1, 2, 3, 4, 5]
    numeric_processor = NumericProcessor()
    print(f"Processing data: {num_data}")
    if numeric_processor.validate(num_data):
        print("Validation: Numeric data verified")
        print(numeric_processor.format_output(
            numeric_processor.process(num_data)))
    else:
        print("Validation: Numeric data verification failed")
    print("\nInitializing Text Processor...")
    text_data = "Hello Nexus World"
    text_processor = TextProcessor()
    print(f"Processing data: \"{text_data}\"")
    if text_processor.validate(text_data):
        print("Validation: Text data verified")
        print(text_processor.format_output(text_processor.process(text_data)))
    else:
        print("Validation: Text data verification failed")
    print("\nInitializing Log Processor...")
    log_data = "ERROR: Connection timeout"
    log_processor = LogProcessor()
    print(f"Processing data: \"{log_data}\"")
    if log_processor.validate(log_data):
        print("Validation: Log entry verified")
        print(log_processor.format_output(log_processor.process(log_data)))
    else:
        print("Validation: Log entry verification failed")
    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    data = [[1, 2, 3], "hello, world", "INFO: System ready"]
    processors = [numeric_processor, text_processor, log_processor]
    for i, d in enumerate(data, start=1):
        for p in processors:
            if p.validate(d):
                print(f"Result {i}: {p.process(d)}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
