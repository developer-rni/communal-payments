# Коммунальные платежи
> Программа для расчета коммунальных платежей. Эта программа создавалась под себя, для упрощения расчета.
___
## Установка
> Инструкция о том, как получить копию этого ПО и запустить его на локальном компьютере. 

**Linux**

- `git clone https://github.com/developer-rni/communal-payments.git`

Необходимо установить зависимости описанные в файле [requirements.txt](https://github.com/developer-rni/communal-payments/blob/master/requirements.txt "requirements.txt")  :

- Находиться в директории программы
- `pip  install  -r  requirements.txt`
- Запустить файл `communal_payments.py`


**Windows**

- `git clone https://github.com/developer-rni/communal-payments.git`
  - `(или нажать на "Code" => Download ZIP и распоковать архив)`

- Запустить файл `communal_payments.exe`
___
**Если нужно чтобы работал функционал бекапа базы данных в Google Drive**
> Для работы данной функции необходимо один раз настроить и произвести авторизацию с помощью google аккаунта.

1. Необходимо чтобы был установлен Python версии 3.6 и более
2. Установить зависимости описанные в файле [requirements.txt](https://github.com/developer-rni/communal-payments/blob/master/requirements.txt "requirements.txt")  :
   - Находиться в директории программы
   - `pip  install  -r  requirements.txt`
3. В файле [upload_gd](https://github.com/developer-rni/communal-payments/blob/master/upload_gd.py "upload_gd.py") изменить на свой ID строчку 29:
   - Переходите в папку Googe Drive куда нужно закачивать базу данных
   - ID Google Drive папки берется с сслыки.
   - Пример ссылки: https://drive.google.com/drive/folders/4tL-UI4TDsWSqK-I6cn9ikSHBAsgQsG2p где `4tL-UI4TDsWSqK-I6cn9ikSHBAsgQsG2p` - это ID

```Python
file1 = drive.CreateFile({'title': 'data_cp.db', "parents": [{"kind": "drive#fileLink","id": 'Тут ID папки Google Drive'}]})
```
**Пример:**
```Python
file1 = drive.CreateFile({'title': 'data_cp.db', "parents": [{"kind": "drive#fileLink","id": '4tL-UI4TDsWSqK-I6cn9ikSHBAsgQsG2p'}]})
```
4. В этом случае запуск программы происходит через файл `communal_payments.py`
5. Файл => Залить в облако(Google Drive) => Выбрать свой Google аккаунт => Дополнительные настройки => Перейти на страницу "communal-pay db upload" => Разрешить => Разрешить
6. Должна появиться надпись в браузере "The authentication flow has completed", а так же окно программы "успешно загружен"

## Программа созданна с помощью

- Python 3
- PyQt5
- Qt5 Desiner