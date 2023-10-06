from expression import evaluate, errors

# An example test that simple addition works as expected.
def test_add():
    assert evaluate("4 + 2") == 6

# An example test for mismatched grouping symbol errors.
def test_closing():
    try:
        evaluate("4 + )")
        # Now we assert False so that we break if no error was raised.
        assert False
    except errors.MismatchedGroupingSymbolError as exc:
        assert exc.idx == 4
        assert exc.kind == "closing"

