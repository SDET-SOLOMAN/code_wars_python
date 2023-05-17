# DESCRIPTION:
#
# Given an array (arr) as an argument complete the function countSmileys that should return the
# total number of smiling faces.
#
# Rules for a smiling face:
#
# Each smiley face must contain a valid pair of eyes. Eyes can be marked as : or ;
# A smiley face can have a nose but it does not have to. Valid characters for a nose are - or ~
# Every smiling face must have a smiling mouth that should be marked with either ) or D
# No additional characters are allowed except for those mentioned.
#
# Valid smiley face examples: :) :D ;-D :~)
# Invalid smiley faces:  ;( :> :} :]
#
# Example
#
# countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
# countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
# countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;


def count_smileys(arr):
    print(arr)
    smiles = [':D',':~)',';~D',':)', ';-D', ";)", ";D", ':-D' ]
    return len(list(filter(lambda x: x in smiles, arr)))


# more complex loop and cond. logic structure:
def count_smileys2(arr):
    counting = 0
    for num in arr:
        if len(num) == 3:
            if num[1] == '~' or num[1] == '-':
                new_num = num[0] + num[2]
                if (new_num[0] == ":" or new_num[0] == ";") and (new_num[1] == 'D' or new_num[1]==')'):
                    counting += 1
        if (num[0] == ":" or num[0] == ";") and (num[1] == 'D' or num[1]==')'):
                counting += 1
    return counting