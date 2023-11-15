# Python Regular Expressions

[Back to README](README.md)

## Regular Expressions

Regex, or regular expressions (REs), are special sequences used to find or match patterns in strings. These sequences use metacharacters and other syntax to represent sets, ranges, or specific characters. For example, the expression `[0-9]` matches the range of numbers between 0 and 9, and `humor|humour` matches both the strings "humor" and "humour".

Regular expressions have many real world uses cases, which include:
- form input validation
- `grep`ing for passwords on a target system
- web scraping
- search and replace
- filtering for information in massive text files such as logs

They may look complicated and intimidating for new users. Take a look at this example:

`/^[a-zA-Z0-9.!#$%&’*+/=?^_{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/`

It just looks like garbled text. But don’t despair, there’s method behind this madness.

To continue learning about Regular Expressions, it is best to be able to do it interactively. **Please follow along with the [Learn Regex: A Beginner's Guide](https://www.sitepoint.com/learn-regex/) SitePoint article**.

> Instead of selecting Javascript flavor like mentioned in the article's "Basics" section, use Python flavor instead.

## Using Regular Expressions in Python

REs are implemented in Python through the `re` python module. Regular expression patterns are compiled into a series of bytecodes which are then executed by a matching engine written in C.

Because of this, in order to do a pattern match in Python you first have to *compile* the RE.

### Compiling Regular Expressions

Regular expressions are compiled into pattern objects, which have methods for various operations such as searching for pattern matches or performing string substitutions.

```py
>>> import re
>>> p = re.compile('ab*')
>>> p
re.compile('ab*')
```

`re.compile()` also accepts an optional flags argument, used to enable various special features and syntax variations. We’ll go over the available settings later, but for now a single example will do:

```py
>>> p = re.compile('ab*', re.IGNORECASE)
```

#### The Backslash Plague

Regular expressions use the backslash character (`\`) to indicate special forms or to allow special characters to be used without invoking their special meaning. This conflicts with Python’s usage of the same character for the same purpose in string literals.

Let’s say you want to write a RE that matches the string "`\section`", which might be found in a LaTeX file. To figure out what to write in the program code, start with the desired string to be matched. Next, you must escape any backslashes and other metacharacters by preceding them with a backslash, resulting in the string "`\\section`". The resulting string that must be passed to `re.compile()` must be "`\\section`". However, to express this as a Python string literal, both backslashes must be escaped again.

| Characters      | Stage                                    |
| --------------- | ---------------------------------------- |
| `\section`      | Text string to be matched                |
| `\\section`     | Escaped backslash for `re.compile()`     | 
| `"\\\\section"` | Escaped backslashes for a string literal |

### Performing Matches
Once you have an object representing a compiled regular expression, what do you do with it? Pattern objects have several methods and attributes. Only the most significant ones will be covered here; consult the [re](https://docs.python.org/3/library/re.html#module-re) docs for a complete listing.

| Method/Attribute | Purpose |
| ---------------- | ---------------- |
| `match()`        | Determine if the RE matches at the beginning of the string. |
| `search()`       | Scan through a string, looking for any location where this RE matches. |
| `findall()`      | Find all substrings where the RE matches, and returns them as a list. |
| `finditer()`     | Find all substrings where the RE matches, and returns them as an iterator. |

`match()` and `search()` return `None` if no match can be found. If they’re successful, a match object instance is returned, containing information about the match: where it starts and ends, the substring it matched, and more.

```py
>>> import re
>>> p = re.compile('[a-z]+')  # Look for 1 or more lowercase
>>> type(p)       
<class 're.Pattern'>
>>> print( p.match("") )      # 0 lowercase letters
None
>>> print( p.match("h") )     # 1 lowercase letters
<re.Match object; span=(0, 1), match='h'>
>>> print( p.match("H0wdy Ags!") )  # RE doesn't match *at the beginning* of the string
None
>>> print( p.match("h0wdy!") )      # Since this *begins* with a lowercase, we get a match
<re.Match object; span=(0, 1), match='h'>
>>> m = p.match("")         # assign the match result to a var
>>> print( type(m) )        # no match
<class 'NoneType'>
>>> m = p.match("h")        # match!
>>> print( type(m) ) 
<class 're.Match'>
```

### `re.Match` Objects

Match objects can be queried for information about the matching string. Match object instances also have several methods and attributes; the most important ones are:

| Method/Attribute | Purpose |
| ---------------- | ------- |
| `group()`        | Return the string matched by the RE |
| `start()`        | Return the starting position of the match | 
| `end()`          | Return the ending position of the match |
| `span()`         | Return a tuple containing the (start, end) positions of the match |


To try these query methods out, lets assume we're looking for a password in some text file. The below code walks you through setting up the `Match` object:
```py
>>> import re
>>> p = re.compile('password:?\s*(\w+)')    # password:<wildcard>
>>> data = "blah blah blah ..... password:NCWDG_420 ... blah blah blah" # assumed file contents
>>> m = p.search(data)                     # setup the match object
>>> type(m)
<class 're.Match'>                        # NOTE: Its still a Match object, even though we didn't use the match() function (we used search())
```

Then, we can try all the newly introduced query methods:
```py
>>> m               # holds everything
<re.Match object; span=(21, 39), match='password:NCWDG_420'>
>>> m.group()
'password:NCWDG_420'
>>> m.start()
21
>>> m.end() 
39
>>> m.span()
(21, 39)
```

## Sources

- [Pydocs - Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
- [SitePoint - Learn Regex](https://www.sitepoint.com/learn-regex/)

## Resources

- [RegexOnce- Learn Regex with simple interactive exercises](https://regexone.com/)

[Back to README](README.md)