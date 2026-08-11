login = 'qwerty'
password = 'qwerty'
balance = 0


while True:

    print('Банкомат: GreeWorlds\nАвторизация!\n')
    login_user = input('Введите логин: ')
    password_user = input('Введите пароль: ')

    if login_user == login and password_user == password:
        print('\nВы успешно авторизовались!\n')
        while True:

            print('Добрый день, Денис!')
            print('Ваш баланс:', balance)
            print('\n1. Внести средства.')
            print('2. Снять средства.')
            print('3. Перевести средства.')
            print('4. Выйти из банкомата.')
            number_menu = int(input('Выберите действие: '))

            if number_menu == 1:
                add_money = int(input('\nВведите сумму, которую хотите внести: '))
                if add_money > 0:
                    balance += add_money
                    print('Средства успешно зачислены на вашу карту, в размере:', add_money, 'рублей.\n')
                else:
                    print('Ошибка транзакции! Вы ввели некорректную сумму!\n')

            elif number_menu == 2:
                delete_money = int(input('\nВведите сумму, которую хотите снять: '))

                if delete_money <= 0:
                    print('Ошибка: сумма должна быть больше нуля.\n')
                    continue

                if delete_money > balance:
                    print('Ошибка транзакции! У вас недостаточно средств!\n')
                else:
                    balance -= delete_money
                    print('Средства успешно списаны с вашей карты, в размере:', delete_money, 'рублей.\n')

            elif number_menu == 3:
                number_friends = int(input('\nВведите ID-клиента, которому хотите перевести средства: '))
                choice_money = int(input('Введите сумму, которую хотите перевести: '))
                print('Перевод подтвержден! ID-клиента:', number_friends, ', сумма:', choice_money, 'рублей.\n')
                balance -= choice_money

            elif number_menu == 4:
                print('\nВсего доброго, Денис! До встречи..\n')
                break

            else:
                print('\nНет такой операции, попробуйте заново!\n')
    else:
        print('\nВы неправильно ввели логин или пароль, попробуйте заново!\n')

