"""Data models for O'Reilly book content."""

from dataclasses import dataclass, field


@dataclass
class Chapter:
    """Represents a book chapter."""

    id: str
    title: str
    url: str
    content_url: str
    order: int
    html_content: str = ""

    def __str__(self) -> str:
        return f"Chapter({self.order}: {self.title})"


@dataclass
class BookMetadata:
    """Metadata for an O'Reilly book."""

    id: str
    title: str
    authors: list[str]
    publisher: str
    description: str
    cover_url: str
    isbn: str = ""
    language: str = "en"

    def __str__(self) -> str:
        authors_str = ", ".join(self.authors)
        return f"{self.title} by {authors_str}"


@dataclass
class Image:
    """Represents an image in the book."""

    url: str
    filename: str
    data: bytes = b""
    media_type: str = "image/png"


@dataclass
class Book:
    """Complete book with metadata and chapters."""

    metadata: BookMetadata
    chapters: list[Chapter] = field(default_factory=list)
    cover_image: bytes = b""
    images: dict[str, Image] = field(default_factory=dict)  # url -> Image

    def __str__(self) -> str:
        return f"Book({self.metadata.title}, {len(self.chapters)} chapters)"
