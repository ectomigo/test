"""
ectomigo testing
"""

A_CONST_QUERY = "SELECT * FROM one"
ANOTHER_CONST_QUERY = """
SELECT o.id, o.val, t.id, t.val
FROM one AS o
CROSS JOIN two AS t
"""

def a_method(val):
    run_query("INSERT INTO one (val) VALUES (%s)", val)
