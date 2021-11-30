# Homework / Task:
# Download dissertations and annotations with url:
# url = 'http://dspu.edu.ua/science/spec-rady/ukr-language/'

# dspu_edu_ua_ukr_language

# Задача:
# 1) Зберегти лінки на дві сторінки, - дисертацій та авторефератів
# 2) Опрацювати кожну з цих двох сторінок, зібравши всі лінки на файли з них
# 3) Порахувати загальний розмір файлів
# 4) Завантажити усі ті файли


import requests # для отримання html-коду веб-сторінки за її URL'ом
from bs4 import BeautifulSoup
import json

from datetime import datetime


# Отримуємо код html-сторінки
def get_html(url):
    header_s = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
    }
    r = requests.get(url, headers = header_s) # Response
    
    return r.text # повертає html-код сторінки (за адресою url)


# Запишемо зпарсені дані до JSON-файлу
def save_list_to_json_file(some_list, json_file_in):
    with open(json_file_in, "a", encoding="utf8") as write_file:
        json.dump(some_list, write_file, indent=4, ensure_ascii=False)


# Прочитаємо дані з JSON-файлу
def read_list_from_json_file(json_file_out):
    with open(json_file_out, encoding="utf8") as write_file:
        data = json.load(write_file)

    return data


def create_obj_bs4(base_url):
    html_doc = get_html(base_url)
    soup = BeautifulSoup (html_doc, 'html.parser')

    return soup


def get_size_of_file_before_downloading(url):
    size_file = int(requests.head(url).headers['Content-Length'])

    return size_file # in Mb


# Завантажуємо один pdf-файл
def pdf_file_to_save(url_dis_pdf, new_name_file):
    response = requests.get(url_dis_pdf)

    with open(new_name_file, 'wb') as f:
        f.write(response.content)


# Обчислення часу, витраченого на роботу вищенаведеного коду
def сalculation_of_time_spent_at_work(end, start):
    total = end - start
    print('Роботу виконано!')
    print('Час виконання роботи:')
    print(str(total) + ' сек')




def main():
    
    base_url = 'http://dspu.edu.ua/science/spec-rady/ukr-language/'
    response = requests.get(base_url)

    if response.status_code == 200:

# -------------------------------------------

#         start = datetime.now()                          # Початок заміру часу

#         soup = create_obj_bs4(base_url)
#         print("Проблем з інтернет-зв'язком немає")

#         link_to_page_diss = soup.find('div', {'class': 'entry-content'}).find_all('li')[2].find('span').find('a').get('href')

#         base_url = 'https://dspu.edu.ua' + link_to_page_diss
#         soup_diss = create_obj_bs4(base_url)


# # # 2) Опрацювати кожну з цих двох сторінок, зібравши всі лінки на файли з них

#         list_links_disserts = []
        
#         # Зберемо списки на файли дисертацій та авторефератів
#         for link_dissert in soup_diss.find('div', {'class': 'entry-content clearfix'}).find_all('a'):
#             link_dissert = link_dissert.get('href')
        
#             if link_dissert[0] == '/':
#                 link_dissert = 'https://dspu.edu.ua' + link_dissert
            
#             list_links_disserts.append(link_dissert)
        
#         print('...')

        
#         link_to_page_aref = soup.find('div', {'class': 'entry-content'}).find_all('li')[3].find('span').find('a').get('href')

#         base_url = 'https://dspu.edu.ua' + link_to_page_aref
#         soup_aref = create_obj_bs4(base_url)

#         list_links_arefs = []
        
#         # Зберемо списки на файли дисертацій та авторефератів
#         for link_aref in soup_aref.find('div', {'class': 'entry-content clearfix'}).find_all('a'):
#             link_aref = link_aref.get('href')
        
#             if link_aref[0] == '/':
#                 link_aref = 'https://dspu.edu.ua' + link_aref
            
#             list_links_arefs.append(link_aref)
        
#         # print('...')


#         # print('Тепер ми можемо дізнатись, скільки часу в нас пішло на виконання цього коду...')

#         end = datetime.now()

#         сalculation_of_time_spent_at_work(end, start)

# # -------------------------------------------

#         start = datetime.now()                          # Початок заміру часу
        
#         # А тепер, збережімо списки на файли дисертацій та авторефератів
#         print('Починаємо зберігати список лінків на файли дисертацій...')

#         json_file_list_disserts = 'Projects/Texty/json/dspu_edu_ua_ukr_language_disserts.json'
#         save_list_to_json_file(list_links_disserts, json_file_list_disserts)

#         print('Починаємо зберігати список лінків на файли авторефератів...')

#         json_file_list_arefs = 'Projects/Texty/json/dspu_edu_ua_ukr_language_arefs.json'
#         save_list_to_json_file(list_links_arefs, json_file_list_arefs)

#         print('Список лінків на файли зібрано.')
        
#         # print('Тепер ми можемо дізнатись, скільки часу в нас пішло на виконання цього коду...')

#         end = datetime.now()

#         сalculation_of_time_spent_at_work(end, start)

# # -------------------------------------------        

#         # Тепер, обчислимо загальний розмір PDF-файлів

#         start = datetime.now()                          # Початок заміру часу

#         json_file_out = 'Projects/Texty/json/dspu_edu_ua_ukr_language_disserts.json'
        
#         list_disserts_pdf = read_list_from_json_file(json_file_out)

#         total_size_pdf_files = 0
        
#         for dissert_file_pdf in list_disserts_pdf:
#             total_size_pdf_files += get_size_of_file_before_downloading(dissert_file_pdf)

#         print('Загальний розмір PDF-файлів дисертацій складає: ' + str(total_size_pdf_files) + ' bytes')
#         print('Загальний розмір PDF-файлів дисертацій складає: ' + str(total_size_pdf_files/(1024 * 1024)) + ' Mb')
#         # Результат обчислень:
#         # Загальний розмір PDF-файлів дисертацій складає: 49091687 bytes
#         # Загальний розмір PDF-файлів дисертацій складає: 46.81748104095459 Mb
            
#         # print('Тепер ми можемо дізнатись, скільки часу в нас пішло на виконання цього коду...')

#         end = datetime.now()

#         сalculation_of_time_spent_at_work(end, start)

# # ------------------------------------------
#         print('...')
#         print('...')
#         print('...')
#         print('А зараз ми можемо дізнатись, скільки часу в нас пішло на виконання цього коду...')
        
#         start = datetime.now()                          # Початок заміру часу
        
#         json_file_out = 'Projects/Texty/json/dspu_edu_ua_ukr_language_arefs.json'

#         list_arefs_pdf = read_list_from_json_file(json_file_out)
#         print('len(list_arefs_pdf): ', str(len(list_arefs_pdf)))

#         total_size_pdf_files = 0

#         for aref_file_pdf in list_arefs_pdf:
#             total_size_pdf_files += get_size_of_file_before_downloading(aref_file_pdf)
        
#         print('Загальний розмір PDF-файлів авторефератів складає: ' + str(total_size_pdf_files) + ' bytes')
#         print('Загальний розмір PDF-файлів авторефератів складає: ' + str(total_size_pdf_files/(1024 * 1024)) + ' Mb')
            # Загальний розмір PDF-файлів авторефератів складає: 778298 bytes
            # Загальний розмір PDF-файлів авторефератів складає: 0.7422428131103516 Mb
            
        # print('Тепер ми можемо дізнатись, скільки часу в нас пішло на виконання цього коду...')

        # end = datetime.now()

        # сalculation_of_time_spent_at_work(end, start)

        # Результат:

# # ------------------------------------------
# #         # Завантажуємо pdf-файли
        start = datetime.now()                          # Початок заміру часу


        json_file_out = 'Projects/Texty/json/dspu_edu_ua_ukr_language_disserts.json'
        list_disserts_pdf = read_list_from_json_file(json_file_out) # закоментуйте наступний рядок, щоб завантажити всі файли
        # list_disserts_pdf = read_list_from_json_file(json_file_out)[10:20] # for test (щоб не завантажувати всі файли)
        tmp_list_disserts_pdf = [link for link in list_disserts_pdf]
        
        json_file_out = 'Projects/Texty/json/dspu_edu_ua_ukr_language_arefs.json'
        list_arefs_pdf = read_list_from_json_file(json_file_out) # закоментуйте наступний рядок, щоб завантажити всі файли
        # list_arefs_pdf = read_list_from_json_file(json_file_out)[10:20] # for test (щоб не завантажувати всі файли)
        tmp_list_arefs_pdf = [link for link in list_arefs_pdf]
        
        list_disserts_pdf, list_arefs_pdf = tmp_list_disserts_pdf, tmp_list_arefs_pdf

        path_pdf_saving = 'Projects/Texty/pdf/dspu_edu_ua_ukr_language/'

        for link_dissert in list_disserts_pdf:
            pdf_file_to_save(link_dissert, path_pdf_saving + link_dissert[len(link_dissert) - link_dissert[::-1].find('/'):])

        print('Завантажили ' + str(len(list_disserts_pdf)) + ' дисертацій')
        
        for link_aref in list_arefs_pdf:
            pdf_file_to_save(link_aref, path_pdf_saving + link_aref[len(link_aref) - link_aref[::-1].find('/'):])
                    
        print('Завантажили ' + str(len(list_arefs_pdf)) + ' авторефератів')

        

        end = datetime.now()

        сalculation_of_time_spent_at_work(end, start)
# -------------------------------------------------------

    elif response.status_code == 404:
        print('Не знайдено сторінки!')
    
    else:
        print("Якась інша проблема з інтернет-зв'язком...")


if __name__ == '__main__':
    main()