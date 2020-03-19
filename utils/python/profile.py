from tabulate import tabulate
from mdutils.mdutils import MdUtils
from .telugu import chars
from itertools import chain


def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)


def create_profile(data):
    # Create file
    md_file = MdUtils(
        file_name='{}-profile'.format(data[0][1]), title='Profile of {}'.format(data[0][1]))

    # Insert basic information of the participant
    md_file.new_header(level=1, title='Participant information')
    md_file.write('\n')
    md_file.insert_code(tabulate(data[:-1]))

    # Insert rdm
    md_file.new_line()
    md_file.new_header(level=1, title='RDM fo the participant')
    md_file.new_line()
    rdm = data[-1].tolist()
    for row, char in zip(rdm, chars):
        row.insert(0, char)
    chars.insert(0, ' ')
    md_file.new_line('{}'.format(tabulate(rdm, chars, tablefmt='github')))

    # End file
    md_file.create_md_file()
