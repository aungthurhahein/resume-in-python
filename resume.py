# !/usr/bin/env python
"""
# This is my resume and you can read by code reviews
# OR
# $ resume.py -h
# __author__ = 'Aung'
# Date : 17032015
"""
import argparse

# contact
contact = {
    'name': "Aung Thu Rha Hein",
    'email': "aungthurhahein@gmail.com",
    'blog': "aungthurhahein@github.io",
    'Porfolio': "aungthurhahein.me",
    'address': "somewhere at Bangkok"
}

# Education
ucsy = {
    'school': "University of Computer Studies",
    'location': "Yangon, MM",
    'program': "BS Computer Science",
    'start': "August 2005",
    'end': "November 2008",
    'description': " focus on software engineering and development courses"
}
mahidol = {
    'school': "Mahidol University",
    'location': "Bangkok, TH",
    'program': "MS Computer Science",
    'start': "August 2012",
    'end': " May 2015",
    'description': " focus on software engineering, security and research on digital forensic"
}
education = {
    'bachelor': ucsy,
    'master': mahidol
}
# Skills
tech_skill = {
    'programming languages': 'CFML, Python, C#, Bash',
    'Environments': 'Windows, Linux',
    'Database': 'MySQL, MSSQL',
    'Web': 'HTML,CSS,Javascript',
    'Tools': 'Sublime Text, VIM, PyCharms, Visual Studio'
}
pract_skill = {
    'language': 'Burmese, English',
    'Interests': 'Web Development, Security, Digital Forensic, Bioinformatics',

}
skill = {
    'technical skills': tech_skill,
    'practical skills': pract_skill
}

# Experience


def parse_command_line():
    parser = argparse.ArgumentParser('Terminal Resume Viewer')
    parser.add_argument('-tldr', '--tldr', action='store_true', help="Too Long; Don't read version")
    parser.add_argument('-con', '--contact', action='store_true', help="Contact")
    parser.add_argument('-edu', '--education', action='store_true', help="Formal Education")
    parser.add_argument('-sk', '--skill', action='store_true', help="Technical Skills")
    parser.add_argument('-xp', '--experience', action='store_true', help="Work Expereince")
    args_pass = parser.parse_args()
    return args_pass

def main(tldr, con, educ, sk, xp):
    if tldr:
        # Brief Bio
        print "My name is Aung Thu Rha Hein."
        print "I am a web application developer with strong academic background, who"\
              "is capable of implementing both frontend and backend development. I"\
              "also have R&D experiences in Digital Forensic and Bioinformatics field"
    # elif contact:


if __name__ == "__main__":
    args = parse_command_line()
    main(args.tldr, args.contact, args.education, args.skill, args.experience)