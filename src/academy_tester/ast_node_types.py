import ast
from typing import Type

AST_EXPR_CONTEXT_NODES: tuple[Type[ast.expr_context], ...] = (
    ast.Load,   # e.g., `x = 5` (x is loaded to be assigned to)
    ast.Store,  # e.g., `x = 5` (5 is stored into x)
    ast.Del,    # e.g., `del x`
)

AST_BOOL_OP_NODES: tuple[Type[ast.boolop], ...] = (
    ast.And,    # e.g., `a and b`
    ast.Or,     # e.g., `a or b`
)

AST_BINARY_OP_NODES: tuple[Type[ast.operator], ...] = (
    # Arithmetic Operators
    ast.Add,       # +
    ast.Sub,       # -
    ast.Mult,      # *
    ast.MatMult,   # @ (matrix multiplication, Python 3.5+)
    ast.Div,       # /
    ast.Mod,       # %
    ast.Pow,       # **
    ast.FloorDiv,  # //

    # Bitwise Operators
    ast.LShift,    # <<
    ast.RShift,    # >>
    ast.BitOr,     # |
    ast.BitXor,    # ^
    ast.BitAnd,    # &
)

AST_UNARY_OP_NODES: tuple[Type[ast.unaryop], ...] = (
    ast.Invert,    # ~ (bitwise NOT)
    ast.Not,       # not (logical NOT)
    ast.UAdd,      # Unary + (e.g., +x)
    ast.USub,      # Unary - (e.g., -x)
)

AST_COMPARISON_OP_NODES: tuple[Type[ast.cmpop], ...] = (
    ast.Eq,      # ==
    ast.NotEq,   # !=
    ast.Lt,      # <
    ast.LtE,     # <=
    ast.Gt,      # >
    ast.GtE,     # >=
    ast.Is,      # is
    ast.IsNot,   # is not
    ast.In,      # in
    ast.NotIn,   # not in
)