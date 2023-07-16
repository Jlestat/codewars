def buy_tofu(cost: int, box: str):
    curr_list = box.split()
    final_coin = curr_list.count('mon') + curr_list.count('monme') * 60
    monme_coin = curr_list.count('monme')
    mon = curr_list.count('mon')
    fin_coin = 0
    count_of_coin = (cost // 60) + (cost % 60)
    if cost > final_coin:
        return 'leaving the market'
    while monme_coin > 0 and cost > 0:
        cost = cost // 60
        fin_coin += 1
        monme_coin -= 1
    fin_list = [mon, curr_list.count('monme'), final_coin, fin_coin]

    return fin_list


print(buy_tofu(124, "mon mon mon mon mon apple mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon monme mon mon mon mon cloth mon mon mon mon mon mon mon mon mon cloth mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon mon"))