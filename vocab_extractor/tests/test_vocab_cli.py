from io import StringIO

from vocab_extractor.vocab_cli import check_db_name, parse_args


# Test parse_args
def test_parse_args():
    test_args = ["--batch-size", "200", "--db-name", "test.db"]
    parsed_args = parse_args(test_args)

    assert parsed_args.batch_size == 200
    assert parsed_args.db_name == "test.db"


# Test check_db_name
def test_check_db_name_existing(monkeypatch, tmp_path):
    db_name = tmp_path / "existing.db"
    db_name.touch()

    monkeypatch.setattr("sys.stdin", StringIO("c\n"))
    result_db_name = check_db_name(str(db_name))
    assert result_db_name == str(db_name)


def test_check_db_name_existing_prompt(monkeypatch, capsys, tmp_path):
    db_name = tmp_path / "existing.db"
    db_name.touch()

    monkeypatch.setattr("sys.stdin", StringIO("c\n"))
    check_db_name(str(db_name))
    out, err = capsys.readouterr()
    assert f"Warning: The specified database '{db_name}' already exists." in out


def test_check_db_name_new(monkeypatch, tmp_path):
    existing_db_name = tmp_path / "existing.db"
    existing_db_name.touch()

    new_db_name = tmp_path / "new.db"
    monkeypatch.setattr("sys.stdin", StringIO(f"{new_db_name}\n"))
    result_db_name = check_db_name(str(existing_db_name))
    assert result_db_name == str(new_db_name)
