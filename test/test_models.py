import pytest
from bot.models import Position, PositionDuplicated, PositionOccupied, PositionUnavailable, Team

# @pytest.fixture
# def empty_data() -> Team:
#     team = Team()

def test_team_join():
    team = Team()
    team.join(Position.CBR, 'John', Position.NOBAL)

    assert team.positions[Position.CBR] == ('John', Position.NOBAL)

def test_team_join_occupied_position():
    team = Team()
    team.join(Position.CBR, 'John', None)

    with pytest.raises(PositionOccupied):
        team.join(Position.CBR, 'Ron', None)

def test_team_join_unavailable_position():
    team = Team()

    with pytest.raises(PositionUnavailable):
        team.join(Position.NOBAL, 'John', 'None')

def test_team_join_different_position_after_already_joined():
    team = Team()
    team.join(Position.CBR, 'John', None)

    with pytest.raises(PositionDuplicated):
        team.join(Position.CF, 'John', None)