import unittest
from unittest.mock import MagicMock, mock_open


def side_effect(arg):
    if arg < 0:
        return 1
    else:
        return 2


mock = MagicMock()
mock.side_effect = side_effect

mock(-1)
mock(1)
