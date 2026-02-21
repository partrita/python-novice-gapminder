import os
import re
import glob

episodes_dir = 'episodes'
mybook_dir = 'mybook'

# Get all md files, sort them
md_files = sorted(glob.glob(os.path.join(episodes_dir, '*.md')))

# Regex for python code blocks and output/error blocks
re_python = re.compile(r'^```python\s*$', re.MULTILINE)
re_output = re.compile(r'^```(output|error|test)\s*\n.*?\n```\s*$', re.MULTILINE | re.DOTALL)

chapters = ['index.qmd']

for f_path in md_files:
    fname = os.path.basename(f_path)
    qmd_name = fname.replace('.md', '.qmd')
    
    # skip index or similar if they clash, but these are numbers like 01-run-quit.md
    
    with open(f_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove output and error blocks before changing python blocks
    content = re_output.sub('', content)
    
    # Change ```python to ```{python}
    content = re_python.sub('```{python}', content)
    
    out_path = os.path.join(mybook_dir, qmd_name)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    chapters.append(qmd_name)

# Now also need to add data and fig directories to mybook or symlink it so execution works
if not os.path.exists(os.path.join(mybook_dir, 'data')):
    os.symlink(os.path.join('..', episodes_dir, 'data'), os.path.join(mybook_dir, 'data'))
if not os.path.exists(os.path.join(mybook_dir, 'fig')):
    os.symlink(os.path.join('..', episodes_dir, 'fig'), os.path.join(mybook_dir, 'fig'))
if not os.path.exists(os.path.join(mybook_dir, 'files')):
    os.symlink(os.path.join('..', episodes_dir, 'files'), os.path.join(mybook_dir, 'files'))

# Read _quarto.yml and replace chapters section
quarto_yml = os.path.join(mybook_dir, '_quarto.yml')
with open(quarto_yml, 'r', encoding='utf-8') as f:
    text = f.read()

chapters += ['summary.qmd', 'references.qmd']
# Replace everything under chapters:
new_chapters = "  chapters:\n"
for c in chapters:
    new_chapters += f"    - {c}\n"

text = re.sub(r'  chapters:\n(\s*- .*\n)*', new_chapters, text)

with open(quarto_yml, 'w', encoding='utf-8') as f:
    f.write(text)

print("Conversion complete.")
