from hello import cool


def test_cool():
    assert cool("Miley") == "Cool!"
    assert cool("Bubble") == "Not cool at all.."
