from pygments.style import Style
from pygments.token import (Keyword, Name, Comment, String, Literal, Error,
                            Number, Operator, Generic, Whitespace, Text,
                            Punctuation, Token
)


class Base16Style(Style):
    base00 = '#f1f1f1'
    base01 = '#e2e2e2'
    base02 = '#d4d4d4'
    base03 = '#777777'
    base04 = '#5e5e5e'
    base05 = '#474747'
    base06 = '#303030'
    base07 = '#1b1b1b'
    base08 = '#d02023'
    base09 = '#bf3e05'
    base0a = '#9d6f00'
    base0b = '#637200'
    base0c = '#007a72'
    base0d = '#0073b5'
    base0e = '#4e66b6'
    base0f = '#c42775'

    default_style = ''

    background_color = base00
    highlight_color = base02

    styles = {
        Text: base05,
        Token: base05,
        Error: base08,  # .err
        
        Punctuation: base05,
        Punctuation.Marker: base05,
        Whitespace: base01,

        Comment: "italic " + base03,  # .c
        Comment.Preproc: "noitalic " + base0f,  # .cp
        Comment.PreprocFile: base0b,  # .cpf
        Comment.Hashbang:          "noitalic bold " + base03,
        Comment.Special:           "noitalic bold " + base03,

        Keyword: base0e,  # .k
        Keyword.Type: "nobold " + base08,  # .kt
        Keyword.Constant: "bold " + base08,
        Keyword.Pseudo: "nobold ",

        Literal: base0b,  # .l
        Literal.Date: "bold " + base0b,

        Name:           base05,
        Name.Attribute: base0d,  # .na
        Name.Builtin: base0d,  # .nb
        Name.Builtin.Pseudo: base08,  # .bp
        Name.Class: base0d,  # .nc
        Name.Constant: base09,  # .no
        Name.Decorator: base09,  # .nd
        Name.Entity:               "bold " + base0f,
        #Name.Exception:            col14, # UNUSED SO FAR
        Name.Function: base0d,  # .nf
        Name.Label:                base0d,
        Name.Namespace: base0d,  # .nn
        Name.Tag: base0e,  # .nt
        Name.Variable: base0d,  # .nv
        Name.Variable.Instance: base08,  # .vi
        Name.Variable.Magic:       "bold",

        Number: base09,  # .m
        Number.Bin:	               base09,
        Number.Float:              base09,
        Number.Hex:                base09,
        Number.Integer:            base09,
        Number.Integer.Long:       base09,
        Number.Oct:                base09,

        Operator: base0c,  # .o
        Operator.Word: base0e,  # .ow

        String: base0b,  # .s
        String.Interpol: base0f,  # .si
        String.Regex: "bold " + base0c,  # .sr
        String.Symbol: base09,  # .ss
        String.Doc:                "italic",
        String.Escape:             "bold " + base0f,
        String.Affix:              "bold " + base0b,
        String.Delimiter:          "bold " + base05,
        String.Heredoc:            "bold " + base05,
        String.Backtick:    base09,
        String.Char:               base0b,
        String.Double:             base0b,
        String.Single:             base0b,
        String.Symbol:             base09,
        String.Other:              base0b,

        # Generic: ,                            # .g
        Generic.Heading:     base05 + ' bold',  # .gh
        Generic.Subheading:  base0d,            # .gu
        Generic.Deleted:     base08,            # .gd
        Generic.Inserted:    base0b,            # .gi
        Generic.Error:             base00 + " bg:" + base08,
        Generic.Emph:              "italic",
        Generic.Strong:            "bold",
        Generic.Prompt:            "bold",
        #Generic.Output:            base05,
        #Generic.Traceback:         base05,

    }


from string import capwords  # noqa: E402
Base16Style.__name__ = 'Base16{}Style'.format(
    capwords('equilibrium-gray-light', '-').replace('-', '')
)
globals()[Base16Style.__name__] = globals()['Base16Style']
del globals()['Base16Style']
del capwords
