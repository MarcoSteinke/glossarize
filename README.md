![logo](glossarize.jpg)

(image generated by AI)

# glossarize
Using frequencies to automatically generate possible glossary expressions for architectural documentation in enterprise applications.

## Usage

To use the tool in your code simply import `glossarize`.

```python
import glossarize, pathlib, os

my_project_directory = pathlib.Path(os.getcwd())

glossary = glossarize(my_project_directory)
```
