# Repository Guidelines

## Project Structure & Module Organization

This repository is a small command-line CRUD application written in Python and backed by MySQL.

- `main.py`: application entry point, menu flow, and `customers` table creation.
- `database.py`: MySQL connection setup using environment variables.
- `metodos_crud.py`: create, read, update, and delete operations.
- `anotacoes`: informal development notes and pending work.
- `creating_mysql.png`: database setup reference image.
- `.env`: local database credentials; never commit this file.

There is currently no test directory. Add future tests under `tests/`, mirroring module names, such as `tests/test_metodos_crud.py`.

## Build, Test, and Development Commands

Create and activate a virtual environment, then install the current runtime dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install mysql-connector-python python-dotenv
```

Run the interactive application with:

```bash
python main.py
```

Check all modules for syntax errors without connecting to MySQL:

```bash
python -m py_compile main.py database.py metodos_crud.py
```

The project has no build step or automated test command yet. If pytest tests are added, run them with `python -m pytest` and record the dependency in a requirements file.

## Coding Style & Naming Conventions

Follow PEP 8: use four-space indentation, blank lines between top-level functions, and `snake_case` for functions and variables. Keep database access in `database.py` or `metodos_crud.py`; keep menu orchestration in `main.py`. Use parameterized SQL (`%s` placeholders), never string interpolation for user-provided values. Prefer Portuguese names consistently within the existing domain vocabulary.

No formatter or linter is configured. Keep changes focused and remove unused imports and commented-out experimental code when replacing it.

## Testing Guidelines

New CRUD behavior should include tests for successful operations, missing customers, duplicate emails, rollback behavior, and closed connections. Mock the MySQL connection for unit tests so tests do not modify a developer database. Name tests `test_<behavior>` and files `test_<module>.py`.

## Commit & Pull Request Guidelines

History uses short, descriptive Portuguese commit messages, for example `submenu corrigido` and `método update_customers commitando para salvar as alterações`. Continue with concise, imperative messages scoped to one change.

Pull requests should explain the behavior changed, list manual or automated verification, mention schema or `.env` changes, and link relevant issues. Include terminal output when it clarifies a changed user flow; screenshots are only needed for visual assets.

## Security & Configuration

Configure `DB_HOST`, `DB_USER`, `DB_PASSWORD`, and `DB_DATABASE` locally in `.env`. Do not commit credentials, database dumps, virtual environments, or generated `__pycache__` files.
