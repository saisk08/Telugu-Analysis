import numpy as np
from tabulate import tabulate
from .basicinfo import overall_data
from .telugu import chars_pairs


def minority_report(input_data, version):
    data = overall_data(input_data)
    bins = [[], [], [], [], []]
    min_report = open(
        'docs/Version-{}/minority_report.md'.format(version), 'w+')
    min_report.write('# Minority Report\n\n')
    min_report.write('This report consists all the pairs which have their highest \
    agreement percentage, less that 50\%\n\n')
    min_report.write('## Summary table\n\n')
    for index, arr in enumerate(data['overall']):
        high = max(arr[1])
        if high <= 10:
            bins[0].append(index)
        elif high > 10 and high <= 20:
            bins[1].append(index)
        elif high > 20 and high <= 30:
            bins[2].append(index)
        elif high > 30 and high <= 40:
            bins[3].append(index)
        elif high > 40 and high <= 50:
            bins[4].append(index)
    table = [['[0, 10]', len(bins[0])],
             ['(10, 20]', len(bins[1])],
             ['(20, 30]', len(bins[2])],
             ['(30, 40]', len(bins[3])],
             ['(40, 50]', len(bins[4])]]
    min_report.write(
        tabulate(table, headers=['Range', 'Count'], tablefmt='github'))
    min_report.write('\n\n')
    min_report.write('## List of pairs\n\n')
    for indx, pairs in enumerate(bins):
        min_report.write('### Range {}0-{}0\n\n'.format(indx, indx + 1))
        for pair in pairs:
            min_report.write('* {}\n'.format(chars_pairs[pair]))
        min_report.write('\n')
    min_report.close()
    return


def majority_report(input_data, version):
    data = overall_data(input_data)
    bins = [[], [], [], [], []]
    max_report = open(
        'docs/Version-{}/majority_report.md'.format(version), 'w+')
    max_report.write('# Majority Report\n\n')
    max_report.write('This report consists all the pairs which have their highest \
    agreement percentage, greater that 50\%\n\n')
    max_report.write('## Summary table\n\n')
    for index, arr in enumerate(data['overall']):
        high = max(arr[1])
        if high > 50 and high <= 60:
            bins[0].append(index)
        elif high > 60 and high <= 70:
            bins[1].append(index)
        elif high > 70 and high <= 80:
            bins[2].append(index)
        elif high > 80 and high <= 90:
            bins[3].append(index)
        elif high > 90 and high <= 100:
            bins[4].append(index)
    table = [['[50, 60]', len(bins[0])],
             ['(60, 70]', len(bins[1])],
             ['(70, 80]', len(bins[2])],
             ['(80, 90]', len(bins[3])],
             ['(90, 100]', len(bins[4])]]
    max_report.write(
        tabulate(table, headers=['Range', 'Count'], tablefmt='github'))
    max_report.write('\n\n')
    max_report.write('## List of pairs\n\n')
    for indx, pairs in enumerate(bins):
        max_report.write('### Range {}0-{}0\n\n'.format(indx + 5, indx + 6))
        for pair in pairs:
            max_report.write('* {}\n'.format(chars_pairs[pair]))
        max_report.write('\n')
    max_report.close()
    return
