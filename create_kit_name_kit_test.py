import data
import sender_stand_request

#Определяю переменные для длинных значений
symbol511 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
symbol512 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"


#Получаю обновленный kid_body
def get_kit_body(name):
	current_kit_body = data.kit_body.copy()
	current_kit_body["name"] = name
	return current_kit_body


#Позитивные проверки
def positive_assertion(name):
	kit_body_positive = get_kit_body(name)
	kit_response_positive = sender_stand_request.post_new_client_kit(kit_body_positive)
	assert kit_response_positive.json()["name"] == name
	assert kit_response_positive.status_code == 201


#Негативные проверки с полем имени в kit_body
def negative_assertion(name):
	kit_body_negative = get_kit_body(name)
	kit_response_negative = sender_stand_request.post_new_client_kit(kit_body_negative)
	assert kit_response_negative.status_code == 400


#Негативные проверки с ошибкой в имени kit_body
def negative_assertion_no_name(kit_body):
	kit_response_negative_no_name = sender_stand_request.post_new_client_kit(kit_body)
	assert kit_response_negative_no_name.status_code == 400


#Допустимое количество символов (1)
def test_create_kit_1_symbol_in_name_get_success_response():
	positive_assertion("a")


#Допустимое количество символов (511)
def test_create_kit_511_symbols_in_name_get_success_response():
	positive_assertion(symbol511)


#Количество символов меньше допустимого (0)
def test_create_kit_empty_name_get_error_response():
	negative_assertion("")


#Количество символов больше допустимого (512)
def test_create_kit_512_symbols_in_name_get_error_response():
	negative_assertion(symbol512)


#Разрешены английские буквы
def test_create_kit_english_letters_in_name_get_success_response():
	positive_assertion("QWErty")


#Разрешены русские буквы
def test_create_kit_russian_letters_in_name_get_success_response():
	positive_assertion("Мария")


#Разрешены спецсимволы
def test_create_kit_has_special_symbols_in_name_get_success_response():
	positive_assertion('"№%@,"')


#Разрешены пробелы
def test_create_kit_has_space_in_name_get_success_response():
	positive_assertion("Человек и КО")


#Разрешены цифры
def test_create_kit_has_number_in_name_get_success_response():
	positive_assertion("123")


#Параметр не передан в запросе
def test_create_kit_no_name_get_error_response():
	current_kit_body_negative_no_name = data.kit_body.copy()
	#Удаляю поле из запроса
	current_kit_body_negative_no_name.pop("name")
	negative_assertion_no_name(current_kit_body_negative_no_name)


#Передан другой тип параметра (число)
def test_create_kit_numeric_type_name_get_error_response():
	negative_assertion(123)