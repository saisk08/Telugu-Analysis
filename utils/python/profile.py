from tabulate import tabulate
from mdutils.mdutils import MdUtils
from .telugu import chars, chars_pairs
from itertools import chain
from .plotter import preprocess


def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)


def create_profile(data):
    # Create file
    md_file = MdUtils(
        file_name='Profiles/{}-profile'.format(data[0][1]))

    # Insert basic information of the participant
    md_file.new_header(level=1, title='Profile of {}'.format(data[0][1]))
    md_file.new_header(level=2, title='Participant information')
    md_file.write('\n')
    md_file.insert_code(tabulate(data[:-1]))

    # Insert rdm
    md_file.new_line()
    md_file.new_header(level=2, title='RDM fo the participant')
    md_file.new_line()
    rdm = data[-1].tolist()
    for row, char in zip(rdm, chars):
        row.insert(0, char)
    chars.insert(0, ' ')
    md_file.new_line('{}'.format(tabulate(rdm, chars, tablefmt='github')))

    # End file
    md_file.create_md_file()


def create_readme(data):
    counts = preprocess(data)
    readme = MdUtils(file_name='README')

    readme.new_header(level=1, title='Analysis')
    readme.new_line(
        '''A profile for each participant has been created. In this document,
        we look at the measures that give an overall look of the data''')
    readme.new_header(level=2, title='Agreement on pairs ratings')
    for pair, ratings_count in zip(chars_pairs, counts):
        readme.new_header(level=3, title='**{}**:'.format(pair))
        for idx, count in enumerate(ratings_count):
            readme.new_line('Score {}: {}, ({})'.format(
                idx + 1, count, count / sum(ratings_count)))
    readme.new_header(level=2, title='Links to indvidual profile')
    for user in data:
        readme.new_line(''' * [{0}]({0}-profile.md)'''.format(user))
    readme.create_md_file()
