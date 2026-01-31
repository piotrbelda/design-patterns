from typing import Any, Protocol

type Data = list[dict[str, Any]]


class Extractor(Protocol):
    def extract(self) -> Data:
        ...


class Transformer(Protocol):
    def transform(self, data: Data) -> Data:
        ...


class Loader(Protocol):
    def load(self, data: Data) -> None:
        ...


class Pipeline:
    def __init__(self, extractor: Extractor, transformers: list[Transformer], loader: Loader) -> None:
        self._extractor = extractor
        self._transformers = transformers
        self._loader = loader

    def run(self) -> None:
        data = self._extractor.extract()
        for transformer in self._transformers:
            data = transformer.transform(data)
        self._loader.load(data)


class WebScraper:
    def extract(self) -> Data:
        return [
            {
                "Content": "Some HTML...",
                "Headers": "Some headers..."
            }
        ]


class FilterTransformer:
    def transform(self, data: Data) -> Data:
        return [x for x in data if x.get("Headers") is not None]


class PostgresLoader:
    def load(self, data: Data) -> None:
        print(f"Loading data to DB: {data}")


def main() -> None:
    pipeline = Pipeline(
        WebScraper(),
        [FilterTransformer()],
        PostgresLoader(),
    )
    pipeline.run()


if __name__ == "__main__":
    main()
