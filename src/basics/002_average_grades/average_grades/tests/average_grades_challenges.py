from average_grades.main import main


def test_challenge_no_grades_displays_message(monkeypatch, capsys):
    """در صورت وارد نکردن هیچ نمره‌ای، پیام مناسب نمایش داده شود."""
    inputs = iter(["done"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = main()

    output = capsys.readouterr().out
    assert "No grades were entered" in output
    assert result is None


def test_challenge_d_without_grades(monkeypatch, capsys):
    """دستور d نیز بدون نمره نباید باعث خطای تقسیم بر صفر شود."""
    inputs = iter(["d"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = main()

    output = capsys.readouterr().out
    assert "No grades were entered" in output
    assert result is None


def test_challenge_invalid_grade_displays_message_and_continues(
    monkeypatch, capsys
):
    """ورودی غیرعددی پیام خطا بدهد و دریافت نمره‌ها ادامه پیدا کند."""
    inputs = iter(["abc", "10", "20", "done"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = main()

    output = capsys.readouterr().out
    assert "Please enter a valid numeric grade" in output
    assert result == 15.0


def test_challenge_invalid_grade_does_not_affect_average(
    monkeypatch, capsys
):
    """ورودی نامعتبر نباید در محاسبه میانگین دخالت داشته باشد."""
    inputs = iter(["abc", "18", "done"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    result = main()

    output = capsys.readouterr().out
    assert "Please enter a valid numeric grade" in output
    assert result == 18.0
