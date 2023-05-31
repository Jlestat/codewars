import math

def predict_age(age_1, age_2, age_3, age_4, age_5, age_6, age_7, age_8):
    curr_list = [age_1, age_2, age_3, age_4,age_5, age_6, age_7, age_8]
    final_sum = 0
    for i in curr_list:
        final_sum += i * i
    s_sum = math.sqrt(final_sum)
    return int(s_sum // 2)



print(predict_age(65,60,75,55,60,63,64,45))