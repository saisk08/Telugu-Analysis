from tabulate import tabulate
from .telugu import chars_pairs
from .plotter import preprocess


def create_profile(data):
    # Create file
    profile = open('Profiles/{}.md'.format(data['user']), 'w+')

    # Insert basic information of the participant
    profile.write('# Participant profile\n')
    profile.write('## Basic information\n')
    profile.write('\n')
    profile.write(
        tabulate(data['info'], tablefmt='github', headers=['Meta', 'Value']))
    profile.write('\n')

    # Insert summary
    profile.write('\n')
    profile.write('## Summary of data\n')
    profile.write(tabulate(data['summary'], tablefmt='github', headers=[
                  'Score', 'Occurances', 'Mean reaction', 'Std reaction']))
    profile.write('\n')

    # Insert all ratings
    profile.write('## Ratings for all pairs\n')
    profile.write(tabulate(data['scores'], tablefmt='github', headers=[
                  'Pair', 'Rating', 'Reaction time']))
    profile.write('\n')

    # End file
    profile.close()


def create_readme(data):
    counts = preprocess(data)
    readme = open('Profiles/README.md')

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
