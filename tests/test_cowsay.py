import sys
from unittest.mock import patch

from pycowsay import main


def test_cowsay(capsys):
    with patch.object(sys, "argv", ["cowsay", "px moo!"]):
        main.main()
        captured = capsys.readouterr()
        assert (
            "  -------\n"
            "< px moo! >\n"
            "  -------\n"
            "   \\   ^__^\n"
            "    \\  (oo)\\_______\n"
            "       (__)\\       )\\/\\\n"
            "           ||----w |\n"
            "           ||     ||\n"
        ) in captured.out
