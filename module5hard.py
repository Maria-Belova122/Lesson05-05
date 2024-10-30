# ЗАДАНИЕ ПО ТЕМЕ "Модули и пакеты"

import time


class Video:

    def __init__(self, title, duration, adult_mode=False):
        self.title = title  # название
        self.duration = duration  # продолжительность, секунды
        self.adult_mode = adult_mode  # возрастное ограничение
        self.time_now = 0  # секунда остановки

    def __str__(self):
        return f'{self.title}'


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname  # ник пользователя
        self.password = hash(password)  # пароль в хэшированном виде
        self.age = age  # возраст

    def __str__(self):
        return f'{self.nickname}'


class UrTube:

    def __init__(self):
        self.users = []  # база пользователей
        self.videos = []  # база видеороликов
        self.current_user = None  # текущий пользователь

    def add(self, *args):
        for i in range(len(args)):
            video_title = args[i].title  # название видео
            # Если база видеороликов пустая, добавляем в нее видео
            if len(self.videos) == 0:
                self.videos.append(args[i])
                # print(f'ОК: Ролик "{video_title}" добавлен в базу видеороликов')
            # Если база видеороликов не пустая, добавляем в нее видео
            # только в том случае, если его названия еще нет в базе
            else:
                # Флаг = ИСТИНА, пока название видео не найдено в базе видеороликов
                # Флаг = ЛОЖЬ, если название видео найдено в базе видеороликов
                flag = True
                for j in range(len(self.videos)):
                    if video_title == self.videos[j].title:
                        # print(f'ОТКАЗ: Ролик "{video_title}" уже есть в базе видеороликов')
                        flag = False
                        break
                # Если ни одного совпадения по названию в базе видеороликов не найдено
                if flag:
                    self.videos.append(args[i])
                    # print(f'ОК: Ролик "{video_title}" добавлен в базу видеороликов')

    def get_videos(self, search_string):
        lower_string = search_string.lower()
        found_videos = []
        for i in range(len(self.videos)):
            video_title = getattr(self.videos[i], 'title')
            lower_video = video_title.lower()
            if lower_video.__contains__(lower_string):
                found_videos.append(video_title)
        return found_videos

    def watch_video(self, search_title):
        found_video = None
        # Проверка вошел ли пользователь в аккаунт
        if self.current_user is not None:
            # Поиск по названию в базе видеороликов
            for i in range(len(self.videos)):
                if search_title == self.videos[i].title:
                    found_video = self.videos[i]  # найденный в базе ролик
                    break
            # Если искомое название не найдено в базе видеороликов
            if found_video is None:
                print(f'Ролик "{search_title}" не найден')
            # Если искомое название найдено в базе видеороликов
            else:
                # Проверяем возраст пользователя, если у ролика есть ограничение по возрасту
                if found_video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    # found_video.time_now - Секунда, на которой включается ролик (= 0)
                    # found_video.duration - Продолжительность ролика
                    for j in range(found_video.time_now, found_video.duration):
                        time.sleep(1)  # остановка на 1 секунду
                        found_video.time_now += 1  # секунда остановки
                        print(found_video.time_now, end=' ')
                    print('Конец видео')
                    # print('секунда остановки -', found_video.time_now)
                    found_video.time_now = 0
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        # Если база пользователей пустая, добавляем пользователя
        if len(self.users) == 0:
            self.users.append(new_user)
            self.current_user = new_user
            # print(f'ОК: Пользователь {nickname} зарегистрирован')
        # Если база пользователей не пустая, проверяем ник на повтор
        else:
            # Флаг = ИСТИНА, если ник не найден в базе пользователей
            # Флаг = ЛОЖЬ, если ник найден в базе пользователей
            flag = True
            for i in range(len(self.users)):
                if nickname == self.users[i].nickname:
                    print(f'Пользователь {nickname} уже существует')
                    flag = False
                    break
            # Если совпадения по нику в базе пользователей не найдено
            # добавляем нового пользователя
            if flag:
                self.users.append(new_user)
                self.current_user = new_user
                # print(f'ОК: Пользователь {nickname} зарегистрирован')
        return self.current_user

    def log_in(self, nickname, password):
        # Если база пользователей пустая
        if len(self.users) == 0:
            print(f'Пользователь {nickname} не найден. Пожалуйста, зарегистрируйтесь.')
        # Если база пользователей не пустая, проверяем содержится ли в ней ник
        else:
            # Флаг = ИСТИНА, если ник не найден в базе пользователей
            # Флаг = ЛОЖЬ, если ник найден в базе пользователей
            flag = True
            for i in range(len(self.users)):
                if nickname == self.users[i].nickname:
                    # Если ник найден проверяем на совпадение пароль
                    if hash(password) == self.users[i].password:
                        print(f'Вход выполнен, пользователь - {nickname}')
                        self.current_user = self.users[i]
                        flag = False
                        break
                    else:
                        return print('Неверный пароль. Попробуйте войти еще раз')
            if flag:
                print(f'Пользователь {nickname} не найден. Пожалуйста, зарегистрируйтесь.')
        return self.current_user

    def log_out(self):
        print(f'Пользователь {self.current_user.nickname} вышел из аккаунта')
        self.current_user = None
        return self.current_user


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# v3 = Video('Лучший язык программирования 2024 года', 15)
# v4 = Video('Лучший язык программирования 2024 года!', 15)
# v5 = Video('Для чего девушкам парень программист!', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
# ur.add(v3, v4, v5)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
# ur.watch_video('Лучший язык программирования 2024 года!')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')

# Проверка входа в UrTube / выхода из UrTube
# ur.log_in('max_pupkin', 'F8098FM8fjm9jmi')
# ur.register('max_pupkin', 'F8098FM8fjm9jmi', 55)
# ur.log_out()
# ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
# ur.log_out()
# ur.log_in('vasya_pupkin', 'LolkekchebureK')
# print(ur.current_user)
