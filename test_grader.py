import sympy as sp
from student_code import q1_determinant, q2_matrix_inverse

# ---------------------------------------------------------------
# 批改第 1 题：行列式
# ---------------------------------------------------------------
def test_q1_determinant():
    ans = q1_determinant()
    # 检查是否没填
    assert ans is not None, "❌ 题目 1 未填写答案"
    # 检查答案是否为 -2
    assert int(ans) == -2, f"❌ 题目 1 答案错误，期望 -2，实际得到 {ans}"

# ---------------------------------------------------------------
# 批改第 2 题：逆矩阵
# ---------------------------------------------------------------
def test_q2_matrix_inverse():
    ans = q2_matrix_inverse()
    # 检查是否没填
    assert ans is not None, "❌ 题目 2 未填写答案"
    # 标准答案矩阵 [[1, -2], [0, 1]]
    expected = sp.Matrix([[1, -2], [0, 1]])
    actual = sp.Matrix(ans)
    # 用 SymPy 校验矩阵是否完全等价
    assert actual == expected, "❌ 题目 2 逆矩阵计算错误"
