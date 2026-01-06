# Import the grade calculation function from main program
from student import calculate_grade

# ---------------- GRADE S TEST CASES ----------------

def test_grade_S_lower_boundary():
    assert calculate_grade(90) == "S"

def test_grade_S_middle_value():
    assert calculate_grade(95) == "S"

def test_grade_S_upper_boundary():
    assert calculate_grade(100) == "S"

# ---------------- GRADE A TEST CASES ----------------

def test_grade_A_lower_boundary():
    assert calculate_grade(80) == "A"

def test_grade_A_middle_value():
    assert calculate_grade(85) == "A"

def test_grade_A_upper_boundary():
    assert calculate_grade(89.99) == "A"

# ---------------- GRADE B TEST CASES ----------------

def test_grade_B_lower_boundary():
    assert calculate_grade(65) == "B"

def test_grade_B_middle_value():
    assert calculate_grade(72) == "B"

def test_grade_B_upper_boundary():
    assert calculate_grade(79.99) == "B"

# ---------------- GRADE C TEST CASES ----------------

def test_grade_C_lower_boundary():
    assert calculate_grade(50) == "C"

def test_grade_C_middle_value():
    assert calculate_grade(58) == "C"

def test_grade_C_upper_boundary():
    assert calculate_grade(64.99) == "C"

# ---------------- GRADE D TEST CASES ----------------

def test_grade_D_lower_boundary():
    assert calculate_grade(40) == "D"

def test_grade_D_middle_value():
    assert calculate_grade(45) == "D"

def test_grade_D_upper_boundary():
    assert calculate_grade(49.99) == "D"

# ---------------- GRADE F TEST CASES ----------------

def test_grade_F_below_40():
    assert calculate_grade(30) == "F"
