"""
Testing out With & Open methods
"""

# 1:
txt_file = "devops_notes_6.txt"

txt_read = open("devops_notes_6.txt", "r")
print(txt_read.read())
txt_read.close()

