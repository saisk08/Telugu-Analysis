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
    profile = MdUtils(
        file_name='Profiles/{}'.format(data[0][1]))

    # Insert basic information of the participant
    profile.new_header(level=1, title='Profile of {}'.format(data[0][1]))
    profile.new_header(level=2, title='Participant information')
    profile.write('\n')
    profile.insert_code(tabulate(data[:-1]))

    # Insert rdm
    profile.new_line()
    profile.new_header(level=2, title='RDM fo the participant')
    profile.new_line()
    rdm = data[-1].tolist()
    temp = chars.copy()
    for row, char in zip(rdm, temp):
        row.insert(0, '**{}**'.format(char))
    temp.insert(0, ' ')
    profile.new_line('{}'.format(tabulate(rdm, temp, tablefmt='github')))

    # End file
    profile.create_md_file()


def create_readme(data):
    counts = preprocess(data)
    readme = MdUtils(file_name='Profiles/README')

    readme.new_header(level=1, title='Analysis')
    readme.new_line(
        '''A profile for each participant has been created. In this document,
        we look at the measures that give an overall look of the data''')
    readme.new_header(level=2, title='Links to indvidual profile')
    for user in data:
        readme.new_line(''' * [{0}]({0}.md)'''.format(user))
    readme.new_header(level=2, title='Agreement on pairs ratings')
    for pair, ratings_count in zip(chars_pairs, counts):
        readme.new_header(level=3, title='**{}**:'.format(pair))
        for idx, count in enumerate(ratings_count):
            readme.new_line('Score {}: {}, ({:.2f} %)'.format(
                idx + 1, count, (count / sum(ratings_count)) * 100))

    readme.new_table_of_contents(table_title='Contents', depth=2)
    readme.create_md_file()
