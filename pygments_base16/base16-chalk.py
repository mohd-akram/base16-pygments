from pygments.style import Style
from pygments.token import (
    Comment, Error, Generic, Keyword, Literal, Name, Number, Operator, String, Text
)


class Base16Style(Style):
    base00 = '#151515'
    base01 = '#202020'
    base02 = '#303030'
    base03 = '#505050'
    base04 = '#b0b0b0'
    base05 = '#d0d0d0'
    base06 = '#e0e0e0'
    base07 = '#f5f5f5'
    base08 = '#fb9fb1'
    base09 = '#eda987'
    base0a = '#ddb26f'
    base0b = '#acc267'
    base0c = '#12cfc0'
    base0d = '#6fc2ef'
    base0e = '#e1a3ee'
    base0f = '#deaf8f'

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
    capwords('chalk', '-').replace('-', '')
)
globals()[Base16Style.__name__] = globals()['Base16Style']
del globals()['Base16Style']
del capwords
