import json
import os


here = os.path.dirname(os.path.abspath(__file__))
profiles_path = os.path.join(here, "profiles")


def start_employer_journey():
    print('حالت کارفرما انتخاب شد.')
    while True:
        print('یکی از گزینه های زیر را انتخاب کنید: ')
        print('۱: نمایش لیست پروفایل ها')
        print('۲: نمایش محتوای پروفایل مورد نظر')
        print('۳: جستجوی پروفایل ها بر اساس مهارت')
        print('۴: بازگشت به منوی قبل')

        menu_num = input('انتخاب شما: ')

        if menu_num == '1' or menu_num == '۱':
            if not os.listdir(profiles_path):
                print('هیچ پروفایلی ساخته نشده است.')
            else:
                print("لیست پروفایل های ساخته شده: ")
                for file_name in os.listdir(profiles_path):
                    print(file_name)

        elif menu_num == '2' or menu_num == '۲':
            user_input = input('برای مشاهده نام پروفایل مورد نظر را وارد کنید:')
            try:
                if user_input in os.listdir(profiles_path):
                    specific_file = os.path.join(profiles_path, user_input)
                    with open(specific_file, 'r') as f:
                        profile_data = json.load(f)

                        for key, value in profile_data.items():
                            print(f"{key},: {value}")
                else:
                    print('پروفایل مورد نظر پیدا نشد.')

            except FileNotFoundError:
                print(FileNotFoundError.__name__, "پیدا نشد.")

        elif menu_num == '3' or menu_num =='۳':
            found_profiles = []
            user_skill = input('لطفا نام مهارت مورد نظر را وارد بفرمایید: ')
            for profile in os.listdir(profiles_path):
                full_path = os.path.join(profiles_path, profile)
                with open(full_path, 'r', encoding='utf-8') as f:
                    profile_data = json.load(f)

                    if 'skills' in profile_data and isinstance(profile_data['skills'], list):
                        skills_in_profile = [skill.lower() for skill in profile_data['skills']]
                        if user_skill in skills_in_profile:
                            found_profiles.append(profile)
            if found_profiles:
                print('-'*50)
                print(f"\nپروفایل‌های یافت شده با مهارت '{user_skill}':")
                for profile in found_profiles:
                    print(f"- {profile}")
                print('-'*50)
            else:
                print(f"\nهیچ پروفایلی با مهارت '{user_skill}' یافت نشد.")


        elif menu_num == '4' or menu_num == '۴':
            print('یه منوی قبل برگشت داده خواهید شد.')
            break
        else:
            print('انتخاب اشتباهی داشته اید. لطفا در انتخاب گزینه ها دقت فرمایید.')
