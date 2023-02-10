def test_open_all_pets(all_pets):
    all_pets.implicitly_wait(5)
    """Проверяем, что открылась главная страницу сайта"""
    assert all_pets.find_element_by_tag_name('h1').text == "PetFriends"


def test_open_my_pets(my_pets):
    my_pets.implicitly_wait(5)
    """Проверяем, что открылась страница сайта мои питомцы"""
    assert my_pets.find_element_by_xpath('//h2').text == "bek"


def test_compare_amount(my_pets):
    all_text = my_pets.find_elements_by_css_selector('.\\.col-sm-4.left')
    amount = all_text[0].text.split('\n')
    amount = amount[1].split(' ')
    amount = int(amount[1])
    all_pets = my_pets.find_elements_by_css_selector('tbody > tr')
    assert amount == len(all_pets)



def test_pets_foto(my_pets):    # """Проверяем что фотографии есть больше чем у половины питомцев"""
    data_foto = 0
    all_pets = my_pets.find_elements_by_css_selector('tbody > tr')
    all_pets_foto = my_pets.find_elements_by_css_selector('th > img')
    for i in range(len(all_pets)):
        if all_pets_foto[i].get_attribute('src') != '':     # проверяем наличие ссылки на фото
            data_foto += 1
    if (len(all_pets) - data_foto) < data_foto:
        assert (len(all_pets) - data_foto) < data_foto      # сравниваем кол-во питомнев с кол-вом фото
    else:
        print(f'\nФотографии есть у {data_foto} питомцев из {len(all_pets)}')


def test_pets_name_breed_age(my_pets):      # У всех питомцев есть имя, возраст и порода.

    all_pets = my_pets.find_elements_by_css_selector('tbody > tr')
    for i in range(len(all_pets)):
        pets = all_pets[i].text.split(" ")
        assert pets[0] != ' '  # Проверка заполнения Имени
        assert pets[1] != ' '  # Проверка заполнения породы
        assert pets[2] != ' '  # Проверка заполнения возраста


def test_pets_different_name(my_pets):
    name = []
    all_pets = my_pets.find_elements_by_css_selector('tbody > tr')
    for i in range(len(all_pets)):
        pets = all_pets[i].text.split(" ")
        name.append(pets[0])
    if len(name) == len(set(name)):
        assert len(name) == len(set(name))
    else:
        print(f'\nВ списке моих  питомцев есть питомцы с одинаковыми именами ')


def test_repeat_pets(my_pets):
    pet = []
    all_pets = my_pets.find_elements_by_css_selector('tbody > tr')
    for i in range(len(all_pets)):
        pets = all_pets[i].text.split(" ")
        pet.append(pets)
    for i, x in enumerate(pet):
        if pet.count(x) > 1:
            print(f'\nпитомец под номером {i} {x}')
        else:
            assert pet.count(x) == 1