# coding=utf-8
import pyrebase
import random


def noquote(s):
    return s
pyrebase.pyrebase.quote = noquote


def init_firebase():
    firebaseConfig = {'apiKey': "AIzaSyCcFUTbszDhbcZxCuXqM85MWr80FPhvY58",
                      'authDomain': "dormitory-c5829.firebaseapp.com",
                      'databaseURL': "https://dormitory-c5829.firebaseio.com",
                      'projectId': "dormitory-c5829",
                      'storageBucket': "dormitory-c5829.appspot.com",
                      'messagingSenderId': "282371830331",
                      'appId': "1:282371830331:web:c8c5c754d20184a045221e",
                      'measurementId': "G-QZSM07QZ73"}
    firebase = pyrebase.initialize_app(firebaseConfig)
    return firebase.database()


# функции общежития
def add_dormitory(number, address):
    db = init_firebase()
    dormitoryData = {'number': number, 'rooms': {0: ''}, 'name': 'Общежитие ' + str(number), 'Адрес': address}
    db.child("dormitories").child('dormitory' + str(number)).set(dormitoryData)
    dorm_num = number
    for number in range(100, 106):
        capacity = random.randint(2, 3)
        room_data = {'capacity': capacity, 'occupied': 0, 'number': number, 'status': 'свободна', 'gender': '',
                     'residents': {}}
        db.child('dormitories').child('dormitory' + str(dorm_num)).child('rooms').child(number).set(room_data)

    for number in range(200, 206):
        capacity = random.randint(2, 3)
        room_data = {'capacity': capacity, 'occupied': 0, 'number': number, 'status': 'свободна', 'gender': '',
                     'residents': {}}
        db.child('dormitories').child('dormitory' + str(dorm_num)).child('rooms').child(number).set(room_data)

    for number in range(300, 306):
        capacity = random.randint(2, 3)
        room_data = {'capacity': capacity, 'occupied': 0, 'number': number, 'status': 'свободна', 'gender': '',
                     'residents': {}}
        db.child('dormitories').child('dormitory' + str(dorm_num)).child('rooms').child(number).set(room_data)

    for number in range(400, 406):
        capacity = random.randint(2, 3)
        room_data = {'capacity': capacity, 'occupied': 0, 'number': number, 'status': 'свободна', 'gender': '',
                     'residents': {}}
        db.child('dormitories').child('dormitory' + str(dorm_num)).child('rooms').child(number).set(room_data)

    for number in range(500, 506):
        capacity = random.randint(2, 3)
        room_data = {'capacity': capacity, 'occupied': 0, 'number': number, 'status': 'свободна', 'gender': '',
                     'residents': {}}
        db.child('dormitories').child('dormitory' + str(dorm_num)).child('rooms').child(number).set(room_data)


def list_of_dormitories():
    """отдает массив формата [(dormitory$, {все данные}),(dormitory$, {все данные})]"""
    dormitory_mas = []
    db = init_firebase()
    dormitories_data = db.child("dormitories").get()
    for dormitory in dormitories_data.each():
        dormitory_mas.append((dormitory.key(), dormitory.val()))
    return dormitory_mas


def update_number_of_rooms(dormitory = "all"):
    """обновляет поле количество комнат в общежитии"""
    db = init_firebase()
    if dormitory != "all":
        pass
    else:
        for dormitory in range(1,4):
            n_room = 0
            rooms = db.child("dormitories").child("dormitory"+str(dormitory)).child("rooms").get()
            for room in rooms.each():
                n_room += 1
            db.child("dormitories").child("dormitory"+str(dormitory)).update({"number_of_rooms":n_room-1})


# функции комнаты
def add_room(dormitory, number, capacity):
    db = init_firebase()
    roomData = {'number': number, 'capacity': capacity, 'occupied': 0, 'status': 'cвободна'}
    db.child("dormitories").child('dormitory' + str(dormitory)).child('rooms').child(roomData['number']).set(roomData)
    update_number_of_rooms(str(dormitory))

def remove_room(dormitory,room):
    db = init_firebase()
    db.child("dormitories").child('dormitory' + str(dormitory)).child('rooms').child(room).remove()



def list_of_all_rooms(dormitory = "all"):
    """
    если при вызове ничего не указывать вернет вообще все
    отдает массив формата [(общага, номер комнаты, {все данные}),(общага, номер комнаты, {все данные})]
    """
    room_mas = []
    db = init_firebase()
    if dormitory != "all":
        rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
        for room in rooms.each():
            room_mas.append((dormitory, room.key(), room.val()))
    else:
        for dormitory in range(1, 4):
            rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
            for room in rooms.each():
                room_mas.append((dormitory, room.key(), room.val()))
    return room_mas


def list_of_empty_rooms(dormitory = "all"):
    """отдает список свободных комнат
    если при вызове ничего не указывать вернет вообще все
    отдает массив формата [(общага, номер комнаты, {все данные}),(общага, номер комнаты, {все данные})]
    """
    room_mas = []
    db = init_firebase()
    if dormitory != "all":
        rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
        for room in rooms.each():
            if room.val()["status"] == "свободна":
                room_mas.append((dormitory, room.key(), room.val()))
    else:
        for dormitory in range(1, 4):
            rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
            for room in rooms.each():
                if room.val()["status"] == "свободна":
                    room_mas.append((dormitory, room.key(), room.val()))
    return room_mas

def list_of_empty_rooms_by_sex(sex,dormitory = "all"):
    """отдает список свободных комнат
    если при вызове ничего не указывать вернет вообще все
    отдает массив формата [(общага, номер комнаты, {все данные}),(общага, номер комнаты, {все данные})]
    """
    room_mas = []
    db = init_firebase()
    if dormitory != "all":
        rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
        for room in rooms.each():
            if room.val()["status"] == "свободна" and (room.val()["gender"] == sex or room.val()["gender"] == ""):
                room_mas.append((dormitory, room.key(), room.val()))

    else:
        for dormitory in range(1, 4):
            rooms = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").get()
            for room in rooms.each():
                if room.val()["status"] == "свободна" and (room.val()["gender"] == sex or room.val()["gender"] == ""):
                    room_mas.append((dormitory, room.key(), room.val()))
    return room_mas


def update_rooms_status(dormitory,room):
    """обновляет статус комнаты"""
    room_mas = []
    db = init_firebase()
    room_data = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).get()
    if room_data.val()["occupied"] == room_data.val()["capacity"]:
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).update({"status":"занята"})
    else:
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).update(
            {"status": "свободна"})

def update_room_occupied(dormitory,room):
    db = init_firebase()
    room_mas = []
    room_data = db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(int(room)).get()
    current_occupied = len(room_data.val()["members"])
    db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(int(room)).update({"occupied":current_occupied})
    update_rooms_status(dormitory,room)

def update_room_gender(dormitory,room,sex):
    db = init_firebase()
    db.child("dormitories").child("dormitory"+str(dormitory)).child("rooms").child(room).update({"gender":sex})

def edit_room(dormitory,room,capacity = None, gender = None, occupied = 0):
    db = init_firebase()
    if capacity:
        db.child("dormitories").child("dormitory"+str(dormitory)).child("rooms").child(room).update({"capacity":capacity})
    if gender:
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).update({"gender": gender})
    if occupied:
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).update(
            {"occupied": occupied})


# функции студента
def add_student(fio, phone, passport, address, educ_form, gender, dormitory = 0):
    """Все поля строки"""
    db = init_firebase()
    '''добавление студента'''
    student_data = {'ФИО': fio, 'Телефон': phone, 'Паспорт': passport, 'Адрес регистрации': address,
                    'Форма обучения': educ_form, 'Пол': gender, 'Комната': 'queue', 'Общежитие': dormitory}

    # добавление в бд клиентов
    key = db.generate_key()
    db.child('clients').child(key).set(student_data)

    if dormitory == '':
        db.child("dormitories").child("queue").child(key).set({"ФИО":fio})
    elif dormitory == -1:
        db.child("dormitories").child("buffer").child(key).set(student_data)
    else:
        db.child("dormitories").child("dormitory"+str(dormitory)).child("rooms").child("queue").child(key).set({"ФИО":fio})
    return key

def add_student_buffer(student_id,fio, phone, passport, address, educ_form, gender, dormitory):
    """Все поля строки"""
    db = init_firebase()
    '''добавление студента'''
    student_data = {'ФИО': fio, 'Телефон': phone, 'Паспорт': passport, 'Адрес регистрации': address,
                    'Форма обучения': educ_form, 'Пол': gender, 'Комната': 'queue', 'Общежитие': dormitory, }

    # добавление в бд клиентов
    db.child("dormitories").child("buffer").child(student_id).set(student_data)


def edit_student(student_id,room, fio = None, phone = None, passport = None, address = None, educ_form = None, gender = None, hostel = None):
    """Ecли какой-то параметр меняется его передаешь в формате fio = изменения, если нет то не указываешь"""
    db = init_firebase()
    if fio:
        db.child("clients").child(student_id).update({"ФИО":fio})
        db.child("dormitories").child(room).remove()  # возможно тут что-то не так
    if phone:
        db.child("clients").child(student_id).update({"Телефон":phone})
    if passport:
        db.child("clients").child(student_id).update({"Паспорт":passport})
    if address:
        db.child("clients").child(student_id).update({"Адрес регистрации":address})
    if educ_form:
        db.child("clients").child(student_id).update({"Форма обучения":educ_form})
    if gender:
        db.child("clients").child(student_id).update({"Пол":gender})
    if hostel:
        db.child("clients").child(student_id).update({"Общежитие":hostel})


def delete_student(student_id, room):
    '''удаление студента'''
    db = init_firebase()
    db.child("clients").child(student_id).remove()
    db.child("dormitories").child(room).remove()
    # добавить удаление из комнаты


def search_student_by_fio(fio):
    """отдает массив формата [(id, {все данные}),(id, {все данные})]"""
    db = init_firebase()
    searched_student_mas = []

    searched_names = db.child('clients').order_by_child('ФИО').equal_to(fio).get()

    for student in searched_names.each():
        searched_student_mas.append((student.key(), student.val()))
    return searched_student_mas

def search_student_by_id(student_id):
    """отдает массив формата (id,{все данные})"""
    db = init_firebase()
    student_data = db.child("clients").order_by_key().equal_to(student_id).get()
    for student in student_data.each():
        student_mas = (student.key(),student.val())
    return student_mas


def list_off_all_students():
    """отдает массив формата [(id, {все данные}),(id, {все данные})]"""
    students_mas = []
    db = init_firebase()
    students_data = db.child("clients").get()
    for student in students_data.each():
        students_mas.append((student.key(), student.val()))
    return students_mas

def remove_student_from_queue(student_id):
    db = init_firebase()
    student = search_student_by_id(student_id)
    dormitory = student[1]["Общежитие"]
    print(dormitory,"qe")
    if dormitory == 0 or '':
        db.child("dormitories").child("queue").child(student_id).remove()
    else:
        db.child("dormitories").child("dormitory"+str(dormitory)).child("rooms").child("queue").child(student_id).remove()


"""Функции договора"""


def add_contract(student_id, date_start, date_end, room, cost, sex, code= None):
    db = init_firebase()
    last_num = get_last_contract_num()

    contract_data = {"Шифр": code, "Дата начала": date_start, "Дата_конца": date_end, "Стоимость": cost}
    db.child("clients").child(student_id).child("Договор").set(contract_data)

    dormitory = search_student_by_id(student_id)[1]["Общежитие"]

    # удаляем человека из очереди
    remove_student_from_queue(student_id)

    # Обновляем комнаты
    db.child("clients").child(student_id).update({"Комната": room})
    db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).child("members").child(
        student_id).set(True)

    update_room_occupied(dormitory, room)
    update_room_gender(dormitory, room, sex)
    print(code[5:])
    if code[5:] == str(last_num+1):
        update_last_contract_num(last_num + 1)

def add_contract_buffer(student_id,fio,date_start, date_end, room, cost, code):
    db = init_firebase()
    last_num = get_last_contract_num()

    contract_data = {"ФИО": fio,"Шифр": code, "Дата начала": date_start, "Дата_конца": date_end, "Стоимость": cost,"Комната": room}
    db.child("dormitories").child("contract_buffer").child(student_id).set(contract_data)







def get_last_contract_num():
    """отдает номер последнего договора"""
    db = init_firebase()
    last_num = db.child("last_contract_num").get()
    return last_num.val()

def update_last_contract_num(num):
    db = init_firebase()
    db.update({"last_contract_num":num})



def check_fio(fio):
    pass

def check_phone_number(phone_number):
    pass

def buffer():
    # буфер, от сюда собственно и происходит закачка в red_client_2
    buffer_mas = []
    db = init_firebase()
    students_data = db.child("dormitories").child("buffer").get()
    for student in students_data.each():
        buffer_mas.append((student.key(), student.val()))
    return buffer_mas

def contract_buffer():
    # буфер, от сюда собственно и происходит закачка в red_client_2
    buffer_mas = []
    db = init_firebase()
    contract_data = db.child("dormitories").child("contract_buffer").get()
    for contract in contract_data.each():
        buffer_mas.append((contract.key(), contract.val()))
    return buffer_mas

def delete_buffer():
    db = init_firebase()
    db.child("dormitories").child("buffer").remove()


def edit_contract(code, date_start=None, date_end=None, room=None, cost=None):
    db = init_firebase()
    contract = search_contract_by_code(code)
    student_id = contract[0]
    dormitory = contract[1]
    student = search_student_by_id(student_id)
    room_old = student[1]["Комната"]
    sex = student[1]["Пол"]

    if date_start:
        db.child("clients").child(student_id).child("Договор").update({"Дата начала": date_start})
    if date_end:
        db.child("clients").child(student_id).child("Договор").update({"Дата конца": date_end})
    if room:
        db.child("clients").child(student_id).update({"Комната": room})
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room_old).child(
            "members").child(student_id).remove()
        db.child("dormitories").child("dormitory" + str(dormitory)).child("rooms").child(room).child("members").child(
            student_id).set(True)
        update_room_occupied(dormitory, room_old)
        update_room_occupied(dormitory, room)
        update_room_gender(dormitory, room, sex)
    if cost:
        db.child("clients").child(student_id).child("Договор").update({"Стоимость": str(cost)})


def search_contract_by_code(code):
    """возвращает данные формата (id_студента, номер общаги, {данные договора}"""
    student_mas = []
    db = init_firebase()
    students = db.child("clients").get()

    for student in students.each():
        if "Договор" in student.val():
            if code == student.val()["Договор"]["Шифр"]:
                student_mas = (student.key(), student.val()["Общежитие"], student.val()["Договор"])
    return student_mas

def get_students_contract_num(student_id):
    code = []
    db = init_firebase()
    student = search_student_by_id(student_id)
    if "Договор" in student[1]:
        code = student[1]["Договор"]["Шифр"]
    else:
        code = "ОБ - " + str(get_last_contract_num() + 1)
    print(code)
    return code

def list_of_contracts():
    """возвращает данные формата [(id_студента, номер общаги, {данные договора}),(id_студента, номер общаги, {данные договора})] """
    last_num = get_last_contract_num()
    contract_mas = []
    for contract_num in range(last_num+1):
        contract = search_contract_by_code("ОБ - " + str(contract_num))
        contract_mas.append(contract)
    return contract_mas

"""функции льгот/стоимостей"""

def add_facility(name,cost):
    """Добавляет новую льготу"""
    db = init_firebase()
    db.child("facilities").child(name).set({"Название":name,"Стоимость":cost})

def remove_facility(name):
    db = init_firebase()
    db.child("facilities").child(name).remove()

def edit_facility(name, cost = None):
    db = init_firebase()
    if cost:
        db.child("facilities").child(name).update({"Стоимость":cost})

def list_of_facilities():
    """возвращает список формата [('Без льгот', 550), ('Инвалид', 0), ('Сирота', 1), ('ЧАЭС', 0)]"""
    db = init_firebase()
    facilities = db.child("facilities").get()
    fac_mas = []
    for facility in facilities.each():
        fac_mas.append((facility.val()["Название"],facility.val()["Стоимость"]))
    return fac_mas



if __name__ == '__main__':
    db = init_firebase()
    #get_students_contract_num("-MOG-7AtIksBbmtkcNPN")
    # add_student("Романенко Владимир Юрьевич","94239423","423423","fdgfdgdf","mgkfdg","male","1")
    # st = db.child("clients").order_by_key().equal_to("-MO2ZXoFYxIRHsaST1G6").get()
    # print(st.val())
    # add_contract("-MO2ZXoFYxIRHsaST1G6","11.12.2018","11.12.2020",301,500,"муж")
    # print(search_student_by_id("-MO2ZXoFYxIRHsaST1G6"))
    # delete_student("-MNV8YOZ6F6Rqrwj5JRa")
    # update_number_of_rooms()
    # print(list_of_all_rooms())
    print(list_of_empty_rooms_by_sex("Мужской"))