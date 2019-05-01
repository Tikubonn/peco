# Peco

| [日本語](README.ja.md) | English |

Peco is a small template engine for HTML that written in Python.
this template engine support HTML-comment-like syntax for don't break page layout when it has not rendered yet.

```html
<!DOCTYPE html>
<html>
  <head>
    <title>$title</title>
  </head>
  <body>
    <!-- @for post in posts -->
      <!-- @if post.publish -->
        <h1>$post.title</h1>
        @sanitize $post.about
      <!-- @endif -->
    <!-- @endfor -->
  </body>
</html>
```

## How to install Peco?

Peco has a `setup.py`, so you can install with this commands.

```sh
python setup.py install
```

## Use to library

you can get a template object with `parse()` and `parse_string()` those published by `peco.parser` package.
template object has `.render()` and `.render_string()` those can expand template with call. you can expand template with them.

```python
from peco.parser import parse, parse_string

template = parse_string("Hello, $name!")
template.render_string(name = "tikubonn") ## Hello, tikubonn!
```

## Use with shell

Peco install global command of `peco` to your computer when installed Peco. 
so you can use Peco like as command line tools.

```shell
peco --parameter '{"person": {"name": "tikubonn"}}'
```

```shell
peco 'input.html' --parameter-file 'parameter.json' --output-file 'output.html'
```

```shell
python -m peco 'input.html' --parameter-file 'parameter.json' --output-file 'output.html'
```

`peco` command has supported there arguments.

| Argument | Description |
| ---- | ---- |
| `input file` | tell an input file name to Peco. it have not to be `.html` file format, but it must obey the Peco's syntax. if you didn't use this option, Peco use the *standard-input*. |
| `--output-file` or `-o` | tell an output file name to Peco. it have not to be `.html` file format, but it must obey the Peco's syntax. if you didn't use this option, Peco use the *standard-output*. | 
| `--parameter-file` | tell a parameter file name to Peco. it use to expand template. it must be `.json` file format. if didn't use this option, Peco use empty associative-array as parameter. | 
| `--parameter` | tell a parameter to Peco. it used to expand template. it must be `JSON` format. if didn't use this option, Peco use empty associative-array as parameter. if Peco took `--parameter-file` and this option, it is undefined what Peco which use. |
| `--version` or `-v` | print version information then exit. |
| `--help` or `-h` | print help information then exit. |

## Basic Syntax

### Escape reserved character

Peco has reserved two characters that are `$` and `@`.
so some cases you need escape those characters.
you can escape reserved character by repeat it twice.

```html
$$ <!-- will be $ after extended -->
@@ <!-- will be @ after extended -->
$$$$ <!-- will be $$ after extended -->
@@@@ <!-- will be @@ after extended -->
```

### Expand parameter

write parameter name after `$` then Peco will expand parameter to there.
you can use characters for parameter name that are alphabets and underbar.

```html
$name
$age
```

### Accessing to attribute

write `.` and attribute name after parameter reference then the Peco expand will expand parameters attribute.
useable characters for attribute name is same as parameter name.

```html
$person.name
$person.age
```

### If statement

`@if` statement choose one content by condition then expand.
`@else` statement have not to exists if you do not necessary it.
Peco has no comparing  operator for this statement, 
so if you want to use it, you should extend this template engine.

```html
<input value="@if $value true @else true @endif">
```

if you want to expand HTML structure without breaking page layout, 
I recommend using block-statement like this code.

```html
<!-- @if $value -->
  <div>
    true
  </div>
<!-- @else -->
  <div>
    false
  </div>
<!-- @endif -->
```

### Iterate collection

`@for` statement repeat expand content while assign parameters element to variable. 
now version, this cannot use multiple value bind, but I want to support it if I could.

```html
<input value="@for $element in $iter $element @endfor">
```

this has supported block-statement like as `@if`.

```html
<!-- @for $element in $iter -->
  $element
<!-- @endfor -->
```

## Builtin filters

filter is transform parameter value before expanding.
basically, it like as control statements, but there can nest another filter.
this example, concatenate persons nicknames by comma, then remove both sides whitespac, then sanitize.

```html
@sanitize @trim @join , $person.nicknames
```

### Concatenating collection

`@join` filter take two arguments that are separator and parameter reference, 
then concatenate parameters value by separator.
if separator is control statement, this filters action is undefined.

```html
<meta name="keywords" content="@join , $keywords">
```

```html
<meta name="keywords" content="@join $keywords"> <!-- without separator -->
```

### Triming whitespace

`@trim` filter will remove parameters both side whitespace before expanding.

```html
@trim $value
```

### Sanitization

`@sanitize` filter will sanitize parameter before expanding.

```html
@sanitize $value
```

## License

Peco is released under the MIT License.  
you can read detail from [here](LICENSE).
