from pygments.style import Style
from pygments.token import (
    Comment, Error, Generic, Keyword, Literal, Name, Number, Operator, String, Text
)


class Base16Style(Style):
    base00 = '#212121'
    base01 = '#303030'
    base02 = '#353535'
    base03 = '#4A4A4A'
    base04 = '#B2CCD6'
    base05 = '#EEFFFF'
    base06 = '#EEFFFF'
    base07 = '#FFFFFF'
    base08 = '#F07178'
    base09 = '#F78C6C'
    base0a = '#FFCB6B'
    base0b = '#C3E88D'
    base0c = '#89DDFF'
    base0d = '#82AAFF'
    base0e = '#C792EA'
    base0f = '#FF5370'

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
    capwords('material-darker', '-').replace('-', '')
)
globals()[Base16Style.__name__] = globals()['Base16Style']
del globals()['Base16Style']
del capwords
