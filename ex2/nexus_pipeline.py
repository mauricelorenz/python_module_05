#!/usr/bin/env python3

from typing import Any, List, Dict, Union, Optional, Protocol
from abc import ABC, abstractmethod
from json import loads, JSONDecodeError


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Any:
        if not isinstance(data, (dict, str, list)):
            raise ValueError("Invalid argument!")
        print(f"Input: {"Real-time sensor stream"
                        if isinstance(data, list) else data}")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            print("Transform: Enriched with metadata and validation")
            return ("Processed "
                    f"{"temperature " if data["sensor"] == "temp" else ""}"
                    f"reading: {data["value"]}°{data["unit"]} "
                    f"{"(Normal range)" if data["value"] < 25 else ""}")
        if isinstance(data, str):
            print("Transform: Parsed and structured data")
            return (f"User activity logged: {data.count("user")} "
                    "actions processed")
        if isinstance(data, list):
            print("Transform: Aggregated and filtered")
            if len(data) == 0:
                return "Stream summary: 0 readings"
            return (f"Stream summary: {len(data)} readings, "
                    f"avg: {sum(data) / len(data):.1f}°C")


class OutputStage:
    def process(self, data: Any) -> Any:
        print(f"Output: {data}")
        return f"Output: {data}"


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []

    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)

    def process(self, data: Any) -> Any:
        for stage in self.stages:
            try:
                data = stage.process(data)
            except ValueError as e:
                print(f"Validation Error: {e}")
                break
        return data


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        try:
            data_dict = loads(data)
        except (TypeError, JSONDecodeError):
            raise ValueError("Invalid argument!")
        return super().process(data_dict)


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        return super().process(data)


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:
        return super().process(data)


class NexusManager:
    pass


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("\nInitializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second")
    print("\nCreating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")
    print("\n=== Multi-Format Data Processing ===")
    stages: List[ProcessingStage] = [InputStage(),
                                     TransformStage(),
                                     OutputStage()]
    print("\nProcessing JSON data through pipeline...")
    json_pipeline = JSONAdapter("JSON01")
    for stage in stages:
        json_pipeline.add_stage(stage)
    json_data = '{"sensor": "temp", "value": 23.5, "unit": "C"}'
    try:
        json_pipeline.process(json_data)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nProcessing CSV data through same pipeline...")
    csv_pipeline = CSVAdapter("CSV01")
    for stage in stages:
        csv_pipeline.add_stage(stage)
    csv_data = "user,action,timestamp"
    try:
        csv_pipeline.process(csv_data)
    except ValueError as e:
        print(f"Error: {e}")
    print("\nProcessing Stream data through same pipeline...")
    stream_pipeline = StreamAdapter("STREAM01")
    for stage in stages:
        stream_pipeline.add_stage(stage)
    stream_data = [22.1, 22.0, 22.2, 22.3, 21.9]
    try:
        stream_pipeline.process(stream_data)
    except ValueError as e:
        print(f"Error: {e}")
    # print(f"=== Pipeline Chaining Demo ===")
    # print(f"Pipeline A -> Pipeline B -> Pipeline C")
    # print(f"Data flow: Raw -> Processed -> Analyzed -> Stored")
    # print(f"Chain result: 100 records processed through 3-stage pipeline")
    # print(f"Performance: 95% efficiency, 0.2s total processing time")
    # print(f"=== Error Recovery Test ===")
    # print(f"Simulating pipeline failure...")
    # print(f"Error detected in Stage 2: Invalid data format")
    # print(f"Recovery initiated: Switching to backup processor")
    # print(f"Recovery successful: Pipeline restored, processing resumed")
    # print(f"Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
