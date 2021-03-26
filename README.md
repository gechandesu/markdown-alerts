# markdown-alerts

Python-Markdown Admonition alternative extension with a shortened syntax. Depends [Python-Markdown](https://pypi.org/project/Markdown/).

This extension supports one-line and multi-line text. The end of the remark block is an empty line.

Example:

```
:::info This is an one-line admonition!

:::info This is a
multi-line
admonition!

:::info
It works too!

This paragraph is not an admonition's part.
```

There can be an arbitrary number of spaces between the admonition start character `:::` and the admonition type designation.

Supported admonition types:

```
:::info
:::note
:::tip
:::success
:::warning
:::danger
```

## Installation and usage

Installation:

```
pip install markdown-alerts
```

Usage:

```python
from markdown import Markdown

html = Markdown(extensions=['markdown_alerts'])
```

## Configuration

By default, the extension installs the following CSS classes for div blocks. For example for `:::note`:

```html
<div class="alert note">
<p>This is note!</p>
</div>
```

You can override these classes by adding your own configuration. Example for **Bootstrap 5**:

```python
ext_configs = {
    'markdown_alerts': {
        'info': 'alert alert-info',
        'note': 'alert alert-primary',
        'tip': 'alert alert-success',
        'success': 'alert alert-success',
        'warning': 'alert alert-warning',
        'danger': 'alert alert-danger'
    }
}

html = Markdown(
            extensions=['markdown_alerts'],
            extension_configs=ext_configs
        )
```

## License

This software is provided under The Unlicense. See [LICENSE](LICENSE) for details.