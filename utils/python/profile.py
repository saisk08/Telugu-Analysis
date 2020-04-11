from tabulate import tabulate
from .telugu import chars_pairs
from .basicinfo import overall_data


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


def create_readme(user_data):
    data = overall_data(user_data)
    readme = open('Profiles/README.md')
    readme.write('# Analysis of experiment-version 1\n')
    readme.write(
        '''A profile for each participant has been created. In this document,
        we look at the measures that give an overall description of the data\n\n''')
    readme.write('## Summary of the participation\n\n')
    readme.write(tabulate(data['scores'], tablefmt='github', headers='keys'))
    readme.write('\n')
    readme.write('## Agreeement percentages and reaction times\n')
    readme.write('''
    !!! tip "About agreement percentages"
        Agreement percentage is defined as the percentage of participants that
        rated a pair a particular score (`1` or `2` or `3` or `4` or `5`). Therefore, agreement
        percentage is calculated for each score of each pair.
    ''')
    readme.write('\n\n')
    readme.write('''
    !!! info
        * All reaction times are given in seconds.
        * The mean and standard deviation below are of the reaction times.
    ''')
    for pair, info_vec in zip(chars_pairs, data['overall']):
        readme.write('\n\n')
        readme.write('### {}\n'.format(pair))
        head = ['Score', 1, 2, 3, 4, 5]
        count = ['Count', *info_vec[0]]
        percentages = ['Agreement %', *info_vec[1]]
        mean = ['Mean', *info_vec[2]]
        std = ['Std', *info_vec[3]]
        readme.write(tabulate([count, percentages, mean,
                               std], tablefmt='github', headers=head))

    readme.close()
