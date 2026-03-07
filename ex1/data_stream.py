#!/usr/bin/env python3

from typing import Any, List, Dict, Union, Optional, Tuple
from abc import ABC, abstractmethod


class DataStream(ABC):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.batch_len = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {self.stream_id: self.batch_len}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if (not isinstance(data_batch, list)
            or not any("temp" in data or "humidity" in data
                       or "pressure" in data for data in data_batch)):
            raise ValueError("Invalid argument!")
        temp_list = []
        for data in data_batch:
            try:
                if "temp" in data:
                    temp_list.append(data["temp"])
            except TypeError:
                pass
        avg_temp = (f"{sum(temp_list) / len(temp_list):.1f}"
                    if len(temp_list) else None)
        self.batch_len = len(data_batch)
        return f"{self.batch_len} readings processed, avg temp: {avg_temp}°C"

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high":
            high_temp = [data for data in data_batch
                         if "temp" in data and data["temp"] > 22]
            high_humidity = [data for data in data_batch
                             if "humidity" in data and data["humidity"] > 70]
            high_pressure = [data for data in data_batch
                             if "pressure" in data and data["pressure"] > 1100]
            return high_temp + high_humidity + high_pressure
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if (not isinstance(data_batch, list)
            or not any("buy" in data or "sell" in data
                       for data in data_batch)):
            raise ValueError("Invalid argument!")
        net_flow = 0
        for data in data_batch:
            try:
                if "buy" in data:
                    net_flow += data["buy"]
                elif "sell" in data:
                    net_flow -= data["sell"]
            except TypeError:
                pass
        self.batch_len = len(data_batch)
        return (f"{self.batch_len} operations, net flow: "
                f"{"+" if net_flow > 0 else ""}{net_flow} units")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high":
            high_buy = [data for data in data_batch
                        if "buy" in data and data["buy"] > 100]
            high_sell = [data for data in data_batch
                         if "sell" in data and data["sell"] > 100]
            return high_buy + high_sell
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id)

    def process_batch(self, data_batch: List[Any]) -> str:
        if (not isinstance(data_batch, list)
                or not any(data in ("login", "error", "logout")
                           for data in data_batch)):
            raise ValueError("Invalid argument!")
        data_errors = [data for data in data_batch if data == "error"]
        self.batch_len = len(data_batch)
        return (f"{self.batch_len} events, {len(data_errors)} "
                f"{"error" if len(data_errors) == 1 else "errors"} detected")

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        if criteria == "high":
            return [data for data in data_batch if data == "critical"]
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return super().get_stats()


class StreamProcessor:
    def __init__(self, streams: List[DataStream]) -> None:
        self.streams = streams

    def process_all(self, data_batches: List[List[Any]]) -> Tuple[Dict, Dict]:
        process_results: Dict[DataStream, int] = {}
        filter_results: Dict[DataStream, int] = {}
        for batch in data_batches:
            for stream in self.streams:
                try:
                    stream.process_batch(batch)
                    if process_results.get(stream):
                        process_results[stream] += 1
                    else:
                        process_results[stream] = 1
                    filter_result = stream.filter_data(batch, "high")
                    if filter_results.get(stream):
                        filter_results[stream] += len(filter_result)
                    else:
                        filter_results[stream] = len(filter_result)
                    break
                except ValueError:
                    pass
        return process_results, filter_results


def main() -> None:
    pass


if __name__ == "__main__":
    main()
