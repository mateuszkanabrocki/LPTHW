from nose.tools import *
from ex47.game_main_classes import Room, Engine


room1 = Room('room1')
room2 = Room('room2')
room3 = Room('room3')

room1.add_paths({'room2': room2})
room1.add_paths({'room3': room3})
room2.add_paths({'room1': room1, 'room2': room2})
room3.add_paths({})


def test_room():

    assert_equal(room1.name, 'room1')
    assert_equal(room2.name, 'room2')
    assert_equal(room3.name, 'room3')


def test_room_paths():

    assert_equal(room1.go('room2'), room2)
    assert_equal(room1.go('room3'), room3)
    assert_equal(room2.go('room1'), room1)
    assert_equal(room2.go('room2'), room2)
    assert_equal(room3.go('room1'), None)
    assert_equal(room1.go('room4'), None)


def test_engine():

    engine = Engine(room1)
    assert_equal(engine.game_intro, room1)