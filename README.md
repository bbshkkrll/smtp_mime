# SMTP-mime

SMTP-mime - консольная утилита, которая отправляет получателю все картинки из указанного (или рабочего) каталога в
качестве вложения.

## Поддерживаемые форматы файлов

Поддерживается отправка трех форматов файлов: jpg, png, gif. Все файлы с данным форматом из указанной директории будут
вложены в письмо.

## Парамеиры запуска

    --from адрес отправителя

    --to адрес получателя

    --ssl использование защищенного соединения

    --auth запрос авторизации

    --verbose отображать работу с сервером

    --subject установить тему пистьма

    --server имя и порт сервера 

    --directory директория, из которой будут браться файлы

## Запуск

python -m modules -s smtp.mail.ru:25 -f example@mail.ru -t example@mail.ru -v --ssl --auth --d [_path to directory with
files_]
