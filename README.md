![logo](glossarize.jpg)

# glossarize
Using statistics to automatically generate possible glossaries for architectural documentation in enterprise applications.

## Usage

To use the tool in your code simply import `glossarize`.

```python
import glossarize, pathlib, os

my_project_directory = pathlib.Path(os.getcwd())

glossary = glossarize(my_project_directory)
```
