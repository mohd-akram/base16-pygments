from pygments.style import Style
from pygments.token import (
    Comment, Error, Generic, Keyword, Literal, Name, Number, Operator, String, Text
)


class Base16Style(Style):
    base00 = '#f8f8f8'
    base01 = '#e8e8e8'
    base02 = '#d8d8d8'
    base03 = '#b8b8b8'
    base04 = '#585858'
    base05 = '#383838'
    base06 = '#282828'
    base07 = '#181818'
    base08 = '#fa8480'
    base09 = '#ffaa61'
    base0a = '#ffdc61'
    base0b = '#a0d2c8'
    base0c = '#a2d6f5'
    base0d = '#a0a7d2'
    base0e = '#c8a0d2'
    base0f = '#d2b2a0'

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

        String: base0b,  # .s
        String.Interpol: base0f,  # .si
        String.Regex: base0c,  # .sr
        String.Symbol: base09,  # .ss

        # Generic: ,                            # .g
        Generic.Deleted:     base08,            # .gd
        # Generic.Emph: ,                       # .ge
        # Generic.Error: ,                      # .gr
        Generic.Heading:     base05 + ' bold',  # .gh
        Generic.Inserted:    base0b,            # .gi
        # Generic.Output: ,                     # .go
        # Generic.Prompt: ,                     # .gp
        # Generic.Strong: ,                     # .gs
        Generic.Subheading:  base0d,            # .gu
        # Generic.Traceback: ,                  # .gt
    }


from string import capwords  # noqa: E402
Base16Style.__name__ = 'Base16{}Style'.format(
    capwords('sagelight', '-').replace('-', '')
)
globals()[Base16Style.__name__] = globals()['Base16Style']
del globals()['Base16Style']
del capwords
