from tabulate import tabulate
from .telugu import chars_pairs
from .basicinfo import overall_data


def create_profile(data, version):
    # Create file
    profile = open(
        'docs/Version-{}/Profiles/{}.md'.format(version, data['user']), 'w+')

    # Insert basic information of the participant
    profile.write('# Profile of {}\n\n'.format(data['user']))
    profile.write('## Basic information\n\n')
    profile.write(
        tabulate(data['info'], tablefmt='github', headers=['Meta', 'Value']))
    profile.write('\n\n')

    # Insert summary
    profile.write('## Summary of data\n\n')
    profile.write(tabulate(data['summary'], tablefmt='github', headers=[
                  'Score', 'Occurances', 'Mean reaction', 'Std reaction']))
    profile.write('\n\n')

    # Insert all ratings
    profile.write('## Ratings for all pairs\n\n')
    profile.write(tabulate(data['scores'], tablefmt='github', headers=[
                  'Pair', 'Rating', 'Reaction time']))
    profile.write('\n\n')

    # End file
    profile.close()


def create_readme(user_data, version):
    data = overall_data(user_data)
    readme = open('docs/Version-{}/index.md'.format(version), 'w+')
    readme.write('# Analysis for version {}\n\n'.format(version))
    readme.write(
        '''A profile for each participant has been created. In this document,
        we look at measures that give an overall description of the data.\n\n''')
    readme.write(
        '**Total number of participants**: {}\n\n'.format(len(user_data)))
    readme.write('## Summary of the participation\n\n')
    readme.write(tabulate(data['scores'], tablefmt='github', headers='keys'))
    readme.write('\n\n')
    readme.write('''
!!! tip "About agreement percentages and majority"
    Agreement percentage is defined as the percentage of participants that
    rated a pair a particular score (`1` or `2` or `3` or `4` or `5`). Therefore, agreement
    percentage is calculated for each score of each pair. If the maximum agreement percentage of
    a pair is more than 50%, then the pair has a **majority**.
    ''')
    readme.write('\n\n')
    readme.write('''
!!! info
    * All reaction times are given in seconds.
    * The mean and standard deviation below are of the reaction times.
    ''')
    readme.write('\n\n')
    readme.write('## Summary of agreement between participants\n\n')
    readme.write('''
* Total pairs: 300
* Percentage in majority: {6:.3f}%
* Percentage in minority: {7:.3f}%
* Majority exists: {0}
* Number of pairs with:
    * Majority having score of 1: {1}
    * Majority having score of 2: {2}
    * Majority having score of 3: {3}
    * Majority having score of 4: {4}
    * Majority having score of 5: {5}
    \n\n'''.format(data['agreement'].sum(), *data['agreement'], (data['agreement'].sum() / 300) * 100,
                   100 - ((data['agreement'].sum() / 300) * 100)))
    readme.write('## Agreeement percentages and reaction times\n\n')
    index = 0
    for pair, info_vec in zip(chars_pairs, data['overall']):
        readme.write('\n\n')
        readme.write('### {}\n\n'.format(pair))
        readme.write('* **Median score**: {}\n\n'.format(info_vec[4]))
        readme.write('* **Majority score**: {}\n\n'.format(info_vec[5]))
        readme.write(
            '* **Mean reaction time**: {}\n\n'.format(data['pair_rec'][index]))
        readme.write(
            '* **Std of reaction time**: {}\n\n'.format(data['pair_std'][index]))
        index += 1
        head = ['Score', 1, 2, 3, 4, 5]
        count = ['Count', *info_vec[0]]
        percentages = ['Agreement %', *info_vec[1]]
        mean = ['Mean', *info_vec[2]]
        std = ['Std', *info_vec[3]]
        readme.write(tabulate([count, percentages, mean,
                               std], tablefmt='github', headers=head))

    readme.close()
