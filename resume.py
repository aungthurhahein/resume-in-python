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
    '1.Name\t': "Aung Thu Rha Hein",
    '2.Email\t': "aungthurhahein@gmail.com",
    '3.Blog\t': "aungthurhahein@github.io",
    '4.Porfolio\t': "aungthurhahein.me",
    '5.Address\t':"somewhere at Bangkok"
}

# Education
ucsy = {
    '1.1.School\t': "University of Computer Studies",
    '1.2.Location\t': "Yangon, MM",
    '1.3.Program\t': "BS Computer Science",
    '1.4.Start\t': "August 2005",
    '1.5.End\t': "November 2008",
    '1.6.Description\t': " focus on software engineering and software development courses"
}

mahidol = {
    '2.1.School\t': "Mahidol University",
    '2.2.Location\t': "Bangkok, TH",
    '2.3.Program\t': "MS Computer Science",
    '2.4.Start\t': "August 2012",
    '2.5.End\t': " May 2015",
    '2.6.Description\t': " focus on software engineering, security and research on digital forensic"
}
education = {
    'Bachelor': ucsy,
    'Master': mahidol
}

# Skills
tech_skill = {
    '1.1.Programming': 'CFML, Python, C#, Bash',
    '1.2.Environment': 'Windows, Linux',
    '1.3.Database': 'MySQL, MSSQL',
    '1.4.Web': 'HTML, CSS, Javascript',
    '1.5.Tools': 'Sublime Text, VIM, PyCharms, Visual Studio'
}
pract_skill = {
    '2.1.Language': 'Burmese, English',
    '2.2.Interests': 'Web Development, Security, Digital Forensic, Bioinformatics',
}

skill = {
    '1.Technical skills': tech_skill,
    '2.Practical skills': pract_skill
}

# Experience
web_developer = {
    '1.1.Company': "Inforithm Maze Co.Ltd",
    '1.2.Location': 'Yangon, MM',
    '1.3.Position': "Web Developer",
    '1.4.Start': "December 2010",
    '1.5.End': "June 2010",
    '1.6.Description': "Implementing, designing and maintaining mid-size & largescale web applications."
                   "Design database & friendly user interface for theprojects."
}
Bioinformatician = {
    '2.1.Company': "CentexShrmip, Mahidol University",
    '2.2.Location': "Bangkok, TH",
    '2.3.Position': "Bioinformatics research assistant",
    '2.4.Start': "February 2013",
    '2.5.End': "Current",
    '2.6.Description': "Data analyzing, Data processing, Project development & Server administration. Implementing"
                   "DNA assembly pipelines and programs to achieve particular project goalsData analyzing, "
                   "Data processing,Project development & Server administration. "
                   "Implementing DNA assembly pipelines and programs to achieve particular project goals.."
}
experience = {
    '1.2008-2012': web_developer,
    '2.2013-Current': Bioinformatician
}

# arguments parser
def parse_command_line():
    parser = argparse.ArgumentParser('Terminal Resume Viewer')
    parser.add_argument('-tldr', '--tldr', action='store_true', help="Too Long; Don't read version")
    parser.add_argument('-con', '--contact', action='store_true', help="Contact")
    parser.add_argument('-edu', '--education', action='store_true', help="Formal Education")
    parser.add_argument('-sk', '--skill', action='store_true', help="Technical Skills")
    parser.add_argument('-xp', '--experience', action='store_true', help="Work Expereince")
    args_pass = parser.parse_args()
    return args_pass

# printing stuff
def print_dict(dict_obj):

    for key in sorted(dict_obj.iterkeys()):
        if isinstance(dict_obj[key], dict):
            print_dict(dict_obj[key])
            print "#----------------------------------------------------------------#"
        else:
            print key, '\t', dict_obj[key]


def main(tldr, con, educ, sk, xp):
    if tldr:
        # Brief Bio
        print "My name is Aung Thu Rha Hein."
        print "I am a web application developer with strong academic background, " \
              "who is capable of implementing both frontend and backend development. "
        print "I also have R&D experiences in Digital Forensic and Bioinformatics field."
    elif con:
        print_dict(contact)
    elif educ:
        print_dict(education)
    elif sk:
        print_dict(skill)
    elif xp:
        print_dict(experience)
    else:
        print "Try with '-h'. It will give you some thing for sure."


if __name__ == "__main__":
    args = parse_command_line()
    main(args.tldr, args.contact, args.education, args.skill, args.experience)
