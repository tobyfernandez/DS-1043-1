from six import assertRaisesRegex

from lab4 import my_max, my_min, my_sum, my_average, my_median, my_mode, roll_dice

def test_my_max():
    assert my_max((1, 5, 3)) == 5
    try:
        my_max(())
    except ValueError:
        assert True
    else:
        assert False

test_my_max()

def test_my_min():
    assert my_min((1, 5, 3)) == 1
    try:
        my_min(())
    except ValueError:
        assert True
    else:
        assert False

test_my_min()

def test_my_sum():
    assert my_sum((1, 2, 3)) == 6
    try:
        my_sum(())
    except ValueError:
        assert True
    else:
        assert False

test_my_sum()

def test_my_average():
    assert my_average((1, 2, 3, 6)) == 3
    try:
        my_average(())
    except ValueError:
        assert True
    else:
        assert False

test_my_average()

def test_my_mode():
    assert my_mode((1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5)) == 4
    try:
        my_mode(())
    except ValueError:
        assert True
    else:
        assert False

test_my_mode()

def test_roll_dice():
   pass
