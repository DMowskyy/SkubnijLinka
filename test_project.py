from project import validate_format , validate_url , get_download_options
import pytest
from unittest.mock import patch

def test_validate_format(monkeypatch):
    monkeypatch.setattr("sys.argv", ["project.py", "https://www.youtube.com/watch?v=SgPJuWLZ60", "mp4"])
    link, file_type = validate_format()
    assert link == "https://www.youtube.com/watch?v=SgPJuWLZ60"
    assert file_type == "mp4"

def test_validate_url():
    assert validate_url("https://www.youtube.com/watch?v=SgPJuWnLZ60") == True
    assert validate_url("https://www.youtube.com/watch?v=PoP2Sa7wYNQ&list=RDPoP2Sa7wYNQ&start_radio=1") == True
    with pytest.raises(SystemExit):
        assert validate_url("https://www.tiktok.com/watch?v=SgPJuWnLZ60") == False
    with pytest.raises(SystemExit):
        assert validate_url("I don't know") == False

@patch("project.yt_dlp.YoutubeDL")
def test_get_download_options(mock_youtube_dl):
    get_download_options("https://www.youtube.com/watch?v=SgPJuWLZ60", "mp4")
    mock_youtube_dl.assert_called_once()
