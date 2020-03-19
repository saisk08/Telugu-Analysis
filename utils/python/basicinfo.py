from scipy.spatial.distance import squareform


def basics(user_data):
    info = list()
    print(user_data)
    info.append(['Reg. no', user_data['userInfo']['content']['user']])
    telugu_attr = ''
    if user_data['userInfo']['content']['read'] is 'Yes':
        telugu_attr += 'Read '

    if user_data['userInfo']['content']['speak'] is 'Yes':
        telugu_attr += 'Speak '

    if user_data['userInfo']['content']['write'] is 'Yes':
        telugu_attr += 'Write '

    info.append(['Telugu', telugu_attr])

    for language in user_data['userInfo']['content']['languages']:
        info.append([language['name'], language['attr']])

    ones, twoes, threes, fours, fives = 0, 0, 0, 0, 0
    reactions = 0
    values = list()

    for value in user_data['data']:
        values.append(int(value['value']))
        if value['value'] is '1':
            ones += 1
        if value['value'] is '2':
            twoes += 1
        if value['value'] is '3':
            threes += 1
        if value['value'] is '4':
            fours += 1
        if value['value'] is '5':
            fives += 1
        reactions += value['reactionTime']

    reactions /= len(user_data['data'])

    info.append(['Reaction time(avg)', reactions])
    info.append(['Ones', ones])
    info.append(['Twos', twoes])
    info.append(['Threes', threes])
    info.append(['Fours', fours])
    info.append(['Fives', fives])
    info.append(squareform(values))

    return info
