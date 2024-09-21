from abc import ABC, abstractmethod
from typing import List


class DataSource(ABC):
    @abstractmethod
    def read_data(self) -> None:
        pass

    @abstractmethod
    def write_data(self, data: List[str]):
        pass


class FileDataSource(DataSource):
    def read_data(self) -> None:
        print('reading data...')

    def write_data(self, data: List[str]):
        return ['Write some data', *data]


class DataSourceDecorator(DataSource):
    def __init__(self, source: DataSource) -> None:
        self.source = source

    def read_data(self) -> None:
        self.source.read_data()

    def write_data(self, data: List[str]):
        return self.source.write_data(data)


class EncryptDataSourceDecorator(DataSourceDecorator):
    def read_data(self) -> None:
        print('Encrypting data...')
        return super().read_data()

    def write_data(self, data: List[str]) -> List[str]:
        return [f'Encrypted: {row}' for row in super().write_data(data)]


class CompressDataSourceDecorator(DataSourceDecorator):
    def read_data(self) -> None:
        print('Compressing data...')
        return super().read_data()

    def write_data(self, data: List[str]) -> List[str]:
        return [f'Compressed: {row}' for row in super().write_data(data)]


if __name__ == '__main__':
    source = FileDataSource()
    source = EncryptDataSourceDecorator(source)
    source = CompressDataSourceDecorator(source)
    source.read_data()
    results = source.write_data(['test', 'another test'])
    print(results)
