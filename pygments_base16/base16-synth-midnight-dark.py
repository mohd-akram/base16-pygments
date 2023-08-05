from pygments.style import Style
from pygments.token import (
    Comment, Error, Keyword, Literal, Name, Number, Operator, Punctuation, String, Text
)


class Base16Style(Style):
    base00 = '#050608'
    base01 = '#1a1b1c'
    base02 = '#28292a'
    base03 = '#474849'
    base04 = '#a3a5a6'
    base05 = '#c1c3c4'
    base06 = '#cfd1d2'
    base07 = '#dddfe0'
    base08 = '#b53b50'
    base09 = '#ea770d'
    base0a = '#c9d364'
    base0b = '#06ea61'
    base0c = '#42fff9'
    base0d = '#03aeff'
    base0e = '#ea5ce2'
    base0f = '#cd6320'

    default_style = ''

    background_color = base00
    highlight_color = base02

    styles = {
        Text: base05,
        Error: base08,  # .err

        Comment: base03,  # .c
        Comment.Preproc: base0f,  # .cp
        Comment.PreprocFile: base0b,  # .cpf

        Keyword: base0e,  # .k
        Keyword.Type: base08,  # .kt

        Name: base0d,  # .n
        Name.Attribute: base0d,  # .na
        Name.Builtin: base0d,  # .nb
        Name.Builtin.Pseudo: base08,  # .bp
        Name.Class: base0d,  # .nc
        Name.Constant: base09,  # .no
        Name.Decorator: base09,  # .nd
        Name.Function: base0d,  # .nf
        Name.Namespace: base0d,  # .nn
        Name.Tag: base0e,  # .nt
        Name.Variable: base0d,  # .nv
        Name.Variable.Instance: base08,  # .vi

        Number: base09,  # .m

        Operator: base0c,  # .o
        Operator.Word: base0e,  # .ow

        Literal: base0b,  # .l
        Punctuation: base0c,  # .p

        String: base0b,  # .s
        String.Interpol: base0f,  # .si
        String.Regex: base0c,  # .sr
        String.Symbol: base09,  # .ss
    }


from string import capwords  # noqa: E402
Base16Style.__name__ = 'Base16{}Style'.format(
    capwords('synth-midnight-dark', '-').replace('-', '')
)
globals()[Base16Style.__name__] = globals()['Base16Style']
del globals()['Base16Style']
del capwords
