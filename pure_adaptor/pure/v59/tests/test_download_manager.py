import pytest
import shutil
import os
from collections import namedtuple

from ..download_manager import PureDownloadManager


@pytest.fixture
def mock_pure_api():
    MockAPI = namedtuple('MockAPI', ['download_file'])
    return MockAPI(
        lambda url, dest: shutil.copyfile(url, dest)
    )


@pytest.fixture
def mock_url_name_pairs():
    fixtures_dir = os.path.join(os.path.dirname(__file__), 'fixtures')
    files = ['test_dataset_file_one.txt', 'test_dataset_file_two.txt']
    return [(os.path.join(fixtures_dir, f), f) for f in files]


def test_download_manager(mock_pure_api, mock_url_name_pairs):
    download_manager = PureDownloadManager(mock_pure_api)
    local_files = [download_manager.download_file(*pair)
                   for pair in mock_url_name_pairs]
    for f_path in local_files:
        assert os.path.exists(f_path) is True
