ADD_FIRST_PLAYLIST = (
    "🎵 Добавь свой плейлист!\n\n"
    "Отправь ссылку на плейлист из Yandex Music, например:\n"
    "<i>https://music.yandex.ru/users/username/playlists/123</i>"
)

INTRO_MESSAGE_TEXT = (
    "🎉 Добро пожаловать в ConcertBot! 🎶\n\n"
    "Тот самый бот для поиска концертов. Мы покажем вам все яркие события от ваших любимых исполнителей по вашей Яндекс Музыке. "
    "Не упустите шанс быть в курсе самых горячих концертов! 🔥\n\n"
    "Выберите действие ниже, чтобы начать:"
)

CONCERT_MESSAGE_TEMPLATE = (
    "{counter_text}"
    "🎤 <b>Артист:</b> {concert_title}\n"
    "📅 <b>Дата:</b> {formatted_date}\n"
    "🏢 <b>Площадка:</b> {place}\n"
    "📍 <b>Адрес:</b> {address}\n\n"
    "Нажмите <a href=\"{afisha_url}\">тык</a> для покупки билета 🎟️"
)

HELP_TEXT = (
    "🎵 Что умеет бот:\n\n"
    "• Добавлять ваши плейлисты с Яндекс.Музыки.\n"
    "• Находить концерты ваших любимых артистов в указанном городе.\n"
    "• Отображать информацию о предстоящих концертах.\n\n"
    "Если у вас возникли вопросы или нужна помощь, нажмите 'Написать в поддержку'."
)

ERROR_EDIT_USER_MESSAGE = "Ошибка при редактировании сообщения:"
ERROR_DELETE_USER_MESSAGE = "Ошибка при удалении сообщения пользователя:"
ERROR_DELETING_PLAYLIST_REQUEST_MESSAGE = 'Ошибка при удалении сообщения с запросом плейлиста:'
ERROR_DELETING_USER_PLAYLIST_MESSAGE = 'Ошибка при удалении сообщения пользователя с плейлистом:'
ERROR_DELETE_CITY_REQUEST = "Ошибка при удалении сообщения с запросом города:"
SEARCH_CONCERTS_WAIT = "⏳ Подождите, идёт поиск концертов..."
ERROR_DELETE_WAIT_MESSAGE = "Ошибка при удалении сообщения об ожидании:"
ERROR_DELETE_PLAYLIST_REQUEST_MESSAGE = "Ошибка при удалении сообщения с запросом плейлиста:"
ERROR_ADD_PLAYLIST = "Ошибка при добавлении плейлиста:"
ERROR_ADD_PLAYLIST_TRY_AGAIN = "Произошла ошибка при добавлении плейлиста. Попробуйте снова."

FAVORITE_ARTISTS_CONCERTS = "🎉 Вот концерты ваших любимых артистов:"
WAIT_CONCERT_SEARCH = (
    "⏳ Подождите, идёт поиск концертов...\n"
    "Это займет около 30 секунд\n"
)

ENTER_CITY_PROMPT = "🏙️ Введите город, в котором проживаете:"
INVALID_PLAYLIST_LINK = "❌ Это не ссылка на плейлист из Yandex Music. Попробуйте снова."
INVALID_CITY = "❌ Мы не знаем такого города. Проверьте написание."
NEXT_CONCERT_MESSAGE = '➡️ Следующее'
LAST_CONCERT_MESSAGE = "Это был последний концерт!"

SHOW_EVENTS_BUTTON = "📅 Показать мои события"
ADD_PLAYLIST_BUTTON = "➕ Добавить плейлист"
CHANGE_CITY_BUTTON = "🌍 Изменить город"
BACK_BUTTON_TEXT = "⬅️ На главный экран"
CLEAN_PLAYLIST_BUTTON = "🧹 Очистить мои события"
SUPPORT_BUTTON_TEXT = "💬 Написать в поддержку"
SUPPORT_BUTTON_URL = "https://t.me/qlqlqlqqq"
BOT_CAPABILITIES_BUTTON_TEXT = "ℹ️ Что умеет бот"

# Callback data для кнопок
SHOW_EVENTS_CALLBACK = "show_my_events"
ADD_PLAYLIST_CALLBACK = "add_playlist"
BACK_BUTTON_CALLBACK = "back_to_intro"
CLEAN_PLAYLIST_CALLBACK = "clean_playlist"
NEXT_CONCERT_CALLBACK = "next_concert"
WHAT_BOT_CAN_DO_CALLBACK = "what_bot_can_do"

PLAYLIST_SAVE_SUCCESS_MESSAGE = "Плейлист успешно добавлен и артисты сохранены!"
PLAYLIST_DELETE_SUCCESS = "Ваш плейлист успешно очищен."

