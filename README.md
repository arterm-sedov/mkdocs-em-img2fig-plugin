# MkDocs Em-Img2Fig Plugin

This [MkDocs](https://www.mkdocs.org) plugin converts markdown encoded images surrounded by two asterisks or two underscores like

``` markdown
*![An image caption](images/my-image.png)*
```
OR
``` markdown
_![An image caption](images/my-image.png)_

```

into `<figure>` notation with inline markdown for the image itself:

``` html
<figure markdown>
  ![Image caption](/images/my-image.png)
  <figcaption>Image caption</figcaption>
</figure>
```

## Requirements

This package requires:
* Python >=3.9 and MkDocs version 1.0 or higher.  
* `md_in_html` extension enabled in your MkDocs configuration.

## Installation

Install the package with pip:
  
``` cmd
pip install mkdocs-em-img2fig-plugin
```

Enable the mkdocs-em-img2fig-plugin plugin and md_in_html extension in your `mkdocs.yml`:

``` yaml
plugins:
  - search
  - autolinks
  - em-img2fig
markdown_extensions:
  - md_in_html
```
**Note:** If you use autolinks or similar plugin declare em-img2fig after it, not before for correct precedence.

**Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

More information about plugins in the [MkDocs documentation](https://www.mkdocs.org/user-guide/plugins/)

## Credits
This plugin is a fork of the https://github.com/stuebersystems/mkdocs-img2fig-plugin which does not require the two asterisks or two underscores
