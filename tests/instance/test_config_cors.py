from pathlib import Path
from plonectl import types
from plonectl.instance import config

import pytest


@pytest.fixture
def default_settings(settings_factory) -> Path:
    """Return the cors settings."""
    path = settings_factory("cors.yaml")
    return path


@pytest.mark.parametrize(
    "attr,exists,is_file",
    [
        ["corsconf", True, True],
        ["zcmlconf", True, True],
        ["wsgiconf", True, True],
        ["zopeconf", True, True],
    ],
)
def test_generate_config_files(
    instance_paths, settings, attr: str, exists: bool, is_file: bool
):
    result = config.generate_config_files(instance_paths, settings)
    assert isinstance(result, types.InstanceConfigFiles)
    path = getattr(result, attr)
    if path:
        assert isinstance(path, Path)
        assert path.exists() is exists
        assert path.is_file() is is_file
    else:
        assert bool(path) is exists
