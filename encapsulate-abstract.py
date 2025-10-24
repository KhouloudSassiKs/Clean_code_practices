from abc import ABC, abstractmethod


class Document(ABC):
    """Abstract base class representing a generic document."""

    @abstractmethod
    def process(self) -> None:
        """Process the document."""
        pass

    def open(self) -> None:
        """Open the document."""
        print("Opening document")

    def close(self) -> None:
        """Close the document."""
        print("Closing document")


class TextDocument(Document):
    """Concrete class for text documents."""

    def process(self) -> None:
        print("Processing text document")


class SpreadsheetDocument(Document):
    """Concrete class for spreadsheet documents."""

    def process(self) -> None:
        print("Processing spreadsheet document")


def handle(document: Document) -> None:
    """Handle a document by opening, processing, and closing it."""
    document.open()
    document.process()
    document.close()


if __name__ == "__main__":
    text_document = TextDocument()
    spreadsheet_document = SpreadsheetDocument()

    handle(text_document)
    handle(spreadsheet_document)
