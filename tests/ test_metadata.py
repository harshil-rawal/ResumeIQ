import glob

from utils.metadata import get_file_info


def test_get_file_info():
    """
    Test metadata extraction using any PDF present
    in the uploads folder.
    """

    pdf_files = glob.glob("uploads/*.pdf")

    # Skip the test if no PDF exists
    assert pdf_files, "No PDF file found in uploads/"

    metadata = get_file_info(pdf_files[0])

    assert isinstance(metadata, dict)

    # Required keys
    assert "filename" in metadata
    assert "extension" in metadata
    assert "filesize_kb" in metadata
    assert "pages" in metadata
    assert "created_at" in metadata
    assert "modified_at" in metadata
    assert "encrypted" in metadata
    assert "title" in metadata
    assert "author" in metadata
    assert "creator" in metadata
    assert "producer" in metadata

    # Value checks
    assert metadata["extension"] == ".pdf"
    assert metadata["pages"] >= 1
    assert metadata["filesize_kb"] > 0