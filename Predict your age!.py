import math

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    """

    :param age_1:
    :param age_2:
    :param age_3:
    :param age_4:
    :param age_5:
    :param age_6:
    :param age_7:
    :param age_8:
    :return:
    """
    curr_list = [age_1, age_2, age_3, age_4,age_5, age_6, age_7, age_8]
    final_sum = 0
    for i in curr_list:
        final_sum += i * i
    s_sum = math.sqrt(final_sum)
    return int(s_sum // 2)



print(predict_age(65,60,75,55,60,63,64,45))