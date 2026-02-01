from typing import Any, Protocol

from bs4 import BeautifulSoup


class Config(Protocol):
    def get(self, key: str) -> Any | None:
        pass


class XMLAdapter:
    _EXTENSION = "xml"

    def __init__(self, data: str):
        self.bs = BeautifulSoup(data, XMLAdapter._EXTENSION)

    def get(self, key: str) -> Any | None:
        if (tag := self.bs.find(key)) is None:
            return None

        return tag.get_text()


class Pipeline:
    def __init__(self, config: Config):
        self._config = config

    def run(self) -> None:
        learning_rate = self._config.get("learning_rate")
        epochs = self._config.get("epochs")
        batch_size = self._config.get("batch_size")

        print(f"Running pipeline with params: {learning_rate}, {epochs}, {batch_size}")


def main() -> None:
    with open("settings.xml", encoding="utf8") as f:
        config = f.read()

    xml_adapter = XMLAdapter(config)
    pipeline = Pipeline(xml_adapter)
    pipeline.run()


if __name__ == "__main__":
    main()
