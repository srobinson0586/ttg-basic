#!/bin/python
"""
dev_add_files.py - Creates boilerplate for JQR sections

The two functions you'll probably use are `make_section()` and 
`make_next_section()`

Example: execute the below line to create section 1.07 - Debugging

make_section("1.07_debugging", "Python")
"""
import os
from pathlib import Path
from inspect import cleandoc

def make_section(foldername: str, language: str):
    folder = Path(foldername)
    folder.mkdir()
    section_name = ' '.join(x.title() for x in folder.name.split('_')[1:])
    write_readme(folder, language, section_name)
    write_section_content(folder, language, section_name)
    write_knowledge_check(folder, language, section_name)
    if language.lower() == 'python':
        write_application_py(folder, section_name)
        write_pytest(folder, section_name)

def write_readme(folder: Path, language: str, title: str):
    file_name = '_'.join(folder.name.split('_')[1:])
    readme = folder / 'README.md'
    readme.touch()
    readme_text = cleandoc(f"""# {language} {title} - README
    Complete the following tasks:
    - [ ] Read through [{title}]({file_name}.md)
    - [ ] Complete [Knowledge Check](knowledge_check.md)
    - [ ] Complete [application.py](application.py)
    - [ ] Run `pytest` in your current directory.  If there are no errors, you completed this section.
    """)
    readme.write_text(readme_text)

def write_section_content(folder: Path, language: str, title: str):
    file_name = '_'.join(folder.name.split('_')[1:])
    content = folder / f'{file_name}.md'
    content.touch()
    content_text = cleandoc(f"""# {language} {title}

    [Back to README](README.md)

    """)
    content.write_text(content_text)

def write_knowledge_check(folder: Path, language: str, title: str):
    knowledge_check = folder / 'knowledge_check.md'
    knowledge_check.touch()
    knowledge_text = cleandoc(f"""# {language} {title} - Knowledge Check

    [Back to README](README.md)

    """)
    knowledge_check.write_text(knowledge_text)

def write_knowledge_check(folder: Path, language: str, title: str):
    knowledge_check = folder / 'knowledge_check.md'
    knowledge_check.touch()
    knowledge_text = cleandoc(f"""# {language} {title} - Knowledge Check

    [Back to README](README.md)

    """)
    knowledge_check.write_text(knowledge_text)

def write_pytest(folder: Path, title: str):
    file_name = '_'.join(folder.name.split('_')[1:])
    pytest = folder / 'test_application.py'
    pytest.touch()
    pytest_text = cleandoc(f"""#!/bin/python
    # Python {title} - Pytest Suite

    def test_{file_name}():
        pass
    """)
    pytest.write_text(pytest_text)

def write_application_py(folder: Path, title: str):
    application = folder / 'application.py'
    application.touch()
    application_text = cleandoc(f"""#!/bin/python
    # Python {title} - Application

    """)
    application.write_text(application_text)

def make_next_section(language: str):
    os.chdir(Path(__file__).parent)
    file_path = Path('dev_python_files.txt')
    folder_paths = [Path(x.split()[0]) for x in file_path.read_text().splitlines()]
    sections_to_create = [folder for folder in folder_paths if not folder.exists()]
    if len(sections_to_create):
        next_section = str(sections_to_create[0])
        make_section(next_section, language)
    
if __name__ == '__main__':
    make_next_section('Python')