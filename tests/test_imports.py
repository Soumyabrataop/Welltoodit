import sys
import os

def test_imports():
    print(f"Current Working Directory: {os.getcwd()}")
    print(f"sys.path: {sys.path}")
    import app
    import downloader
    assert hasattr(app, 'app')
    assert hasattr(downloader, 'list_formats')
    assert hasattr(downloader, 'download_video')