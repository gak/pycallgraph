from helpers import *


@pytest.fixture
def cli():
    return CommandLine()


def test_no_args(cli):
    with pytest.raises(SystemExit):
        cli.parse_args()
