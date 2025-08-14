from employee import start_employee_journey
from employer import start_employer_journey


def main():
    while True:
        print('\n' + '-'*50)
        print('به پروفایل ساز خوش آمدید.')
        print('-'*50+'\n')
        print('لطفا یکی از حالات زیر را انتخاب کنید.')
        print('۱: حالت کارمند')
        print('۲: حالت کارفرما')
        print('۳: خروج')

        choice = input("انتخاب شما از بین گزینه ها:")
        if choice == '1' or choice == '۱':
            start_employee_journey()
        elif choice == '2' or choice == '۲':
            start_employer_journey()
        elif choice == '3' or choice == '۳':
            print('خدا نگهدار')
            break
        else:
            print('انتخاب اشتباهی داشته اید. لطفا در انتخاب گزینه ها دقت فرمایید.')

if __name__ == '__main__':
    main()