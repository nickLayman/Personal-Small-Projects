from CV import data_for_cv


# cv = True
# resume = False
typeface = 'mathptmx'  # options are default, helvetica, newcent, and mathptmx
name = 'Nicholas Layman'
email = 'laymann@mail.gvsu.edu'
cell = '(708) 955-7275'
address = '4295 Campus View Dr. \\\\ Allendale, MI 49401'


def preamble():
    preamble_str = f"""LaTeX file for CV
% This file uses the resume document class (res.cls)

\\documentclass[margin]{{res}}
% the margin option causes section titles to appear to the left of body text 
\\textwidth=5.2in % increase textwidth to get smaller right margin
\\usepackage{{{typeface}}} % sets typeface / font
\\usepackage{{enumitem}}

\\begin{{document}}
"""
    return preamble_str


def contact_info():
    contact_info_str = f"""
\\name{{\Huge {name} \\\\[12pt]}} % the \\\\[12pt] adds a blank line after name

\\address{{{{\\bf Contact Information}} \\\\ Email: {email} \\\\ Cell: {cell}}}
\\address{{{{\\bf Present Address}} \\\\ {address}}}


% to change the text/column widths, line 271 in res.cls
"""
    return contact_info_str


def main(cv_name='CV 0.0.0 - never.txt'):
    CV_file = open(cv_name, 'w')
    CV_file.write(preamble())
    CV_file.write(contact_info())
    CV_file.write('\n\\begin{resume}\n\n\n')
    CV_file.write('\n\end{resume} \n\end{document}')



if __name__ == '__main__':
    version: str = '3.0.0'
    date: str = 'August 2021'
    main(f"CV {version} - {date}.txt")
