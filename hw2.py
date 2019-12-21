
import Techniovision as Tv
from builtins import len, open

FILE = "input.txt"

STAFF = "staff"
INSIDE_CONTEST = "inside"
NOT_EXIST = 'not_exist'

# create a dictonary of each faculty and its programs
def setup_faculty_program_list(file_name):
    file = open(file_name, "r")
    faculty_dictionary = {}
    for line in file:
        words = line.split()
        if words[0] == STAFF:
            del words[0]
            del words[0]
            faculty = words.pop(len(words) - 1)
            programs = []
            for program in words:
                programs.append(program)
            faculty_dictionary.setdefault(faculty, programs)
    file.close()
    return faculty_dictionary

# return a dictionary of each faculty and its winning program
def inside_contests_results(file_name, faculty_dictionary):
    results_dictionary = {}
    for faculty in faculty_dictionary.keys():
        winning_program = inside_contest(faculty, file_name)
        results_dictionary.setdefault(faculty, winning_program)
    return results_dictionary

# return the facult that the program belomgs to
def find_faculty(faculty_dictionary, program):
    for faculty, programs in faculty_dictionary.items():
        if program in programs:
            return faculty
    return NOT_EXIST

# return the key of max value
def find_max_value_in_dict(dict):
    values = list(dict.values())
    max_index = values.index(max(values))
    keys = list(dict.keys())
    return keys[max_index]

# return the winning program for each faculty
def inside_contest(faculty, file_name):
    file = open(file_name, "r")
    faculty_programs = {}
    used_ids = []
    for line in file:
        words = line.split()
        if words[0] == STAFF and words[-1] == faculty:
            if words[2] not in faculty_programs:
                faculty_programs.setdefault(words[2], 20)
            else:
                faculty_programs[words[2]] += 20
        if words[0] == INSIDE_CONTEST and words[-1] == faculty:
            if words[2] not in used_ids:
                used_ids.append(words[2])
                if words[3] not in faculty_programs:
                    faculty_programs.setdefault(words[3], 1)
                else:
                    faculty_programs[words[3]] += 1
            else:
                continue
    return find_max_value_in_dict(faculty_programs)


facultyDictionary = setup_faculty_program_list(FILE)
winningPrograms = inside_contests_results(FILE, facultyDictionary)
techniovision = Tv.TechniovisionCreate()
file = open(FILE, "r")
for line in file:
    words = line.split()
    if words[0] == "techniovision":
        id = words[1]
        chosenProgram = words[2]
        studentFaculty = words[3]
        chosenFaculty = find_faculty(facultyDictionary, chosenProgram)
        if studentFaculty == chosenFaculty or chosenFaculty == NOT_EXIST:
            continue

        winningProgram = winningPrograms[chosenFaculty]
        if winningProgram != chosenProgram:
            continue
        Tv.TechniovisionStudentVotes(techniovision, int(id),\
                                     str(studentFaculty), str(chosenFaculty))
Tv.TechniovisionWinningFaculty(techniovision)
Tv.TechniovisionDestroy(techniovision)
