from pygments.style import Style
from pygments.token import (
    Comment, Error, Keyword, Literal, Name, Number, Operator, Punctuation, String, Text
)


class Base16Style(Style):
    base00 = '#101010'
    base01 = '#252525'
    base02 = '#464646'
    base03 = '#525252'
    base04 = '#ababab'
    base05 = '#b9b9b9'
    base06 = '#e3e3e3'
    base07 = '#f7f7f7'
    base08 = '#7c7c7c'
    base09 = '#999999'
    base0a = '#a0a0a0'
    base0b = '#8e8e8e'
    base0c = '#868686'
    base0d = '#686868'
    base0e = '#747474'
    base0f = '#5e5e5e'

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
    capwords('grayscale-dark', '-').replace('-', '')
)
globals()[Base16Style.__name__] = globals()['Base16Style']
del globals()['Base16Style']
del capwords
