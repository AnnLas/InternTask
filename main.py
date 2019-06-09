# Constant for convering GiB into MiB
SCALER = 1024


def calculate(usb_size, memes):
    """
The function returns a tuple with the first element being the total value of all memes on
the USB stick, and the second being the set of names of the memes that should be copied
onto the USB stick to maximize its value.

    :param usb_size:int, size of the memes storage
    :param memes:List[Tuple[str,int,int]] name, size in MiB, price in caps
    :return: Tuple(int,set) int:memes size, set:names of the memes
    """
    usb_size = int(usb_size * SCALER + 1)
    memes_amount = len(memes)

    memes = list(set(memes))

    if len(memes) == 1 and memes[0][1] <= usb_size:
        return (memes[0][2], set(memes[0][0]))

    values_matrix = [[0 for x in range(usb_size)] for y in range(memes_amount)]

    for item in range(0, memes_amount):

        for weight in range(1, usb_size):
            if memes[item][1] <= weight:
                if (memes[item][2] + values_matrix[item - 1][weight - memes[item][1]]) > \
                        values_matrix[item - 1][weight]:
                    values_matrix[item][weight] = memes[item][2] + values_matrix[item - 1][weight - memes[item][1]]
                else:
                    values_matrix[item][weight] = values_matrix[item - 1][weight]
            else:
                values_matrix[item][weight] = values_matrix[item - 1][weight]

    return values_matrix[-1][-1], memes_names(values_matrix, memes)


def memes_names(values_matrix, memes):
    """
Helper function returns set which contains memes names

    :param values_matrix: List[][] values calculated in the previous step
    :param memes:List[Tuple[str,int,int]] name, size in MiB, price in caps
    :return: Set(str) names of the memes set
    """
    meme_list = set()
    item_number = len(values_matrix) - 1
    weight = len(values_matrix[0]) - 1
    max_value = values_matrix[-1][-1]

    while item_number > 0 and weight > 0:
        if values_matrix[item_number][weight] != values_matrix[item_number - 1][weight]:

            if values_matrix[item_number][weight] == max_value:
                meme_list.add(memes[item_number][0])
                max_value = max_value - memes[item_number][2]
                weight = weight - memes[item_number][1]
                item_number = item_number - 1
            else:
                weight = weight - 1

        else:
            item_number = item_number - 1

    if max_value != 0:
        meme_list.add(memes[0][0])

    return meme_list
