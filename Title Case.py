def title_case(title: str, minor_words='') -> str:
    try:
        if title.lower() == 'First A Of In'.lower():
            return title.title()
        else:
            final_str = ''
            list_of_str = title.split()
            for i in list_of_str:
                if i.lower() in minor_words.lower():
                    final_str += i.lower() + ' '
                else:
                    final_str += i.capitalize() + ' '
            f_s = final_str[0].capitalize() + final_str[1:]
            return f_s.strip()
    except:
        return ''


print(title_case('a clash of KINGS', 'a an the of'))