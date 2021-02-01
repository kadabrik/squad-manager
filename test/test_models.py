import pytest
from bot.models import Position, PositionDuplicated, PositionOccupied, PositionUnavailable, Team


def test_team_join():
    team = Team()
    team.join(Position.CBR, 'John', Position.NOBAL)

    assert team._squad[Position.CBR] == ('John', Position.NOBAL)


def test_team_join_occupied_position():
    team = Team()
    team.join(Position.CBR, 'John', None)

    with pytest.raises(PositionOccupied):
        team.join(Position.CBR, 'Ron', None)


def test_team_join_unavailable_position():
    team = Team()

    with pytest.raises(PositionUnavailable):
        team.join(Position.NOBAL, 'John', None)


def test_team_join_different_position_after_already_joined():
    team = Team()
    team.join(Position.CBR, 'John', None)

    with pytest.raises(PositionDuplicated):
        team.join(Position.CF, 'John', None)


def test_team_join_same_position_to_update_hint():
    team = Team()
    team.join(Position.DMF, 'John', None)
    team.join(Position.DMF, 'John', Position.CMF)

    assert team._squad[Position.DMF] == ('John', Position.CMF)


def test_team_leave():
    team = Team()
    team.join(Position.CF, 'Ivan', None)
    team.leave('Ivan')

    assert team._squad[Position.CF] is None


def test_team_leave_without_assignment():
    team = Team()
    team.leave('Ivan')

    assert team._squad.items() == Team()._squad.items()


def test_team_clear():
    team = Team()
    team.join(Position.CF, 'Ivan', None)
    team.clear(Position.CF)

    assert team._squad[Position.CF] is None


def test_team_clear_empty_squad():
    team = Team()
    team.clear(Position.CF)

    assert team._squad[Position.CF] is None


def test_team_reset():
    team = Team()
    positions_players = [(team._formation[i], f"P{i}") for i in range(10)]
    for (position, name) in positions_players:
        team.join(position, name)

    team.reset()

    for v in team._squad.values():
        assert v is None
