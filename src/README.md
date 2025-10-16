# CLI Tool
Проєкт демонструє три підходи до створення CLI-інструментів на Python: `sys.argv`, `click` та `fire`.

## Вимоги
- Python 3.8+

## Структура
- `src/sys_tool.py`: Виводить "командна строка" при прямому запуску. Підтримує `--help`.
- `src/click_tool.py`: CLI-утиліта на `click` з командою `say` та опцією `--name`.
- `src/fire_expose.py`: Експортує функції з `utils.py` через `fire` для CLI.

## Використання

### sys_tool.py
```bash
python src/sys_tool.py
# Вивід: командна строка

python src/sys_tool.py --help
# Виводить підказку
