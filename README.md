# AmneziaWG Configuration QR Generator
<div align="center">
  <img src="logo/logo.png" alt="AmneziaWG Config to QR Logo" width="400"/>
  <p><i>Генератор QR-кодов для конфигураций AmneziaWG</i></p>
</div>

## 📋 О программе

**AmneziaWG Configuration QR Generator** — это десктопное приложение с графическим интерфейсом, созданное для упрощения переноса конфигураций AmneziaWG на мобильные устройства. Программа читает файл конфигурации (.conf) и генерирует QR-код, который можно отсканировать в приложении AmneziaWG на мобильном устройстве.

Поддерживаются все специфические параметры AmneziaWG, включая настройки "мусорных" пакетов (Jc, Jmin, Jmax) и динамические заголовки.

## ✨ Возможности

- **Простой интерфейс** — интуитивно понятное окно с кнопкой выбора файла и генерации QR-кода
- **Поддержка всех параметров AmneziaWG**:
  - `Jc`, `Jmin`, `Jmax` — настройки мусорных пакетов
  - `S1`, `S2`, `S3`, `S4` — максимальные длины пакетов
  - `H1`, `H2`, `H3`, `H4` — динамические заголовки
  - `I1`, `I2`, `I3`, `I4`, `I5` — сформированные UDP-пакеты (синтаксис CPS)
- **Предпросмотр** — QR-код отображается в отдельном окне с возможностью масштабирования
- **Информация о программе** — подробное описание всех параметров и инструкция по использованию
- **Современный интерфейс** — стильный дизайн на PyQt5 с использованием Fusion-стиля

## 📸 Скриншоты

<div align="center">
  <img src="screenshots/main_window.png" alt="Главное окно" width="300"/>
  <img src="screenshots/qr_dialog.png" alt="QR-код" width="300"/>
  <img src="screenshots/about.png" alt="О программе" width="300"/>
</div>


## 🚀 Запуск

### Предварительные требования

-   Python 3.6 или выше
-   pip (менеджер пакетов Python)

### Установка зависимостей

``` bash
pip install PyQt5 qrcode[pil]
```

### Запуск программы

``` bash
python awgqr.py
```


## 🔧 Сборка в исполняемый файл

Для создания standalone .exe файла (не требует установки Python):

``` bash
pip install pyinstaller
pyinstaller --onefile --windowed --icon=icon/icon.ico --add-data "icon;icon" --add-data "logo;logo" awgqr.py
```

После выполнения команды исполняемый файл будет находиться в папке
`dist/`.


## 📁 Структура проекта

    awgqr/
    ├── awgqr.py
    ├── icon/
    │   └── icon.ico
    ├── logo/
    │   └── logo.png
    ├── screenshots/
    ├── LICENSE
    └── README.md


## 🎯 Использование

1.  Запустите приложение
2.  Нажмите кнопку "Обзор"
3.  Выберите файл конфигурации AmneziaWG (.conf)
4.  Нажмите "Показать QR-код"
5.  Отсканируйте QR-код в мобильном приложении AmneziaWG


### ⚙️ Поддерживаемые параметры конфигурации

| Параметр | Описание |
|----------|----------|
| Jc | Количество "мусорных" пакетов после основной последовательности |
| Jmin | Минимальный размер "мусорных" пакетов (в байтах) |
| Jmax | Максимальный размер "мусорных" пакетов (в байтах) |
| S1 | Макс. длина пакетов инициализации (Init) |
| S2 | Макс. длина пакетов ответа (Response) |
| S3 | Макс. длина cookie-пакетов |
| S4 | Макс. длина пакетов с данными (Data) |
| H1 | Динамический заголовок Init (32 бит) |
| H2 | Динамический заголовок Response (32 бит) |
| H3 | Динамический заголовок cookie (32 бит) |
| H4 | Динамический заголовок Data (32 бит) |
| I1 | Сформированный UDP-пакет (CPS) |
| I2 | Сформированный UDP-пакет (CPS) |
| I3 | Сформированный UDP-пакет (CPS) |
| I4 | Сформированный UDP-пакет (CPS) |
| I5 | Сформированный UDP-пакет (CPS) |


## 📝 Версии AmneziaWG

-   ✅ AmneziaWG 1.0
-   ✅ AmneziaWG 1.5
-   ✅ AmneziaWG 2.0


## 🏷️ Теги

    amneziawg
    vpn
    qr-code
    wireguard
    pyqt5
    python
    configuration-generator
    windows-app
    qr-generator
    vpn-config


## 🤝 Вклад в проект

Если вы нашли баг или хотите предложить улучшение:

1.  Создайте Issue с описанием проблемы\
2.  Подробно опишите проблему\
3.  Приложите скриншоты при необходимости\
4.  Укажите версию программы и ОС

Или отправьте Pull Request:

1.  Форкните репозиторий\
2.  Создайте ветку\
3.  Отправьте pull request


## 🔜 Планы по развитию

-   Поддержка других форматов конфигураций
-   Сохранение QR-кода в файл
-   Редактирование параметров перед генерацией
-   Поддержка темной темы
-   Мультиязычный интерфейс


## 📄 Лицензия

MIT License

Copyright (c) 2026 Evgeny Khramtsov

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the
"Software"), to deal in the Software without restriction...


## 📊 Статус проекта

![status](https://img.shields.io/badge/status-stable-green)\
![release](https://img.shields.io/badge/release-v1.4-blue)\
![support](https://img.shields.io/badge/support-active-brightgreen)

------------------------------------------------------------------------

<div align="center">

<sub>Сделано с ❤️ для сообщества Amnezia</sub>  
<sub>© 2026 MacTep Yoba</sub>  
<sub>Версия 1.4</sub>

</div>
