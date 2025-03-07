def is_float(str_num):
    try:
        float(str_num)
        return True
    except:
        return False


def create_answer_04(weight, doze):
    ans_list = []
    if doze == 0.4:
        if (weight >= 50) and (weight < 55):
            ans_list.append("1 капсула 16 мг и 1 капсула 8 мг")
            ans_list.append("8 месяцев")
        elif (weight >= 55) and (weight < 60):
            ans_list.append("1 капсула 16 мг и 1 капсула 8 мг")
            ans_list.append("9 месяцев")
        elif (weight >= 60) and (weight < 65):
            ans_list.append("1 капсула 16 мг и 1 капсула 8 мг")
            ans_list.append("10 месяцев")
        elif (weight >= 65) and (weight < 70):
            ans_list.append("2 капсулы 16 мг")
            ans_list.append("8 месяцев")
        elif (weight >= 70) and (weight < 80):
            ans_list.append("2 капсулы 16 мг")
            ans_list.append("9 месяцев")
        elif (weight >= 80) and (weight < 85):
            ans_list.append("2 капсулы 16 мг")
            ans_list.append("10 месяцев")
        elif (weight >= 85) and (weight < 90):
            ans_list.append("2 капсулы 16 мг и 1 капсула 8 мг")
            ans_list.append("8 месяцев")
        elif (weight >= 90) and (weight < 95):
            ans_list.append("2 капсулы 16 мг и 1 капсула 8 мг")
            ans_list.append("9 месяцев")
        elif weight >= 95:
            ans_list.append("2 капсулы 16 мг и 1 капсула 8 мг")
            ans_list.append("10 месяцев")
    elif doze == 0.6:
        if (weight >= 50) and (weight < 55):
            ans_list.append("2 капсулы 16 мг")
            ans_list.append("6 месяцев")
        elif (weight >= 55) and (weight < 60):
            ans_list.append("2 капсулы 16 мг")
            ans_list.append("7 месяцев")
        elif (weight >= 60) and (weight < 70):
            ans_list.append("2 капсулы 16 мг и 1 капсула 8 мг")
            ans_list.append("6 месяцев")
        elif (weight >= 70) and (weight < 75):
            ans_list.append("2 капсулы 16 мг и 1 капсула 8 мг")
            ans_list.append("7 месяцев")
        elif (weight >= 75) and (weight < 80):
            ans_list.append("3 капсулы 16 мг")
            ans_list.append("6 месяцев")
        elif (weight >= 80) and (weight < 90):
            ans_list.append("3 капсулы 16 мг")
            ans_list.append("7 месяцев")
        elif weight >= 90:
            ans_list.append("3 капсулы 16 мг и 1 капсула 8 мг")
            ans_list.append("7 месяцев")
    elif doze == 0.8:
        if (weight >= 50) and (weight < 60):
            ans_list.append("2 капсулы 16 мг и 1 капсула 8 мг")
            ans_list.append("5 месяцев")
        elif (weight >= 60) and (weight < 70):
            ans_list.append("3 капсулы 16 мг")
            ans_list.append("5 месяцев")
        elif (weight >= 70) and (weight < 80):
            ans_list.append("3 капсулы 16 мг и 1 капсула 8 мг")
            ans_list.append("5 месяцев")
        elif (weight >= 80) and (weight < 90):
            ans_list.append("4 капсулы 16 мг")
            ans_list.append("5 месяцев")
        elif (weight >= 90) and (weight < 100):
            ans_list.append("4 капсулы 16 мг и 1 капсула 8 мг")
            ans_list.append("5 месяцев")
        elif weight >= 100:
            ans_list.append("5 капсул 16 мг")
            ans_list.append("5 месяцев")
    return ans_list
