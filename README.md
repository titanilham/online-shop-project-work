<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Josefin+Sans&size=28&pause=1000&color=00F7F0&center=true&width=435&lines=Online-shop" alt="Typing SVG" />
</div>

<div align="center">

[![Django](https://img.shields.io/badge/Django-%23092E20.svg?logo=django&logoColor=white)](#)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=000)](#)
[![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)](#)
[![HTML](https://img.shields.io/badge/HTML-%23E34F26.svg?logo=html5&logoColor=white)](#)
[![CSS](https://img.shields.io/badge/CSS-1572B6?logo=css3&logoColor=fff)](#)
[![SQLite](https://img.shields.io/badge/SQLite-%2307405e.svg?logo=sqlite&logoColor=white)](#)

</div>

## План разработки:

### 1) Создать пустой проект на Django:
* Создать все необходимые файлы в проекте Django(html, js, css, sqlite, папку с фотографиями)

### 2) Написать верстку:
* Написать разметку на html, сделать несколько страниц, добавить стили и js
* Использовать SVG, а не PNG
* Добавить шрифты
* Добавить адаптивность
* Не забыть добавлять переменные, которые могут в будущем пригодиться
  

### 3) Добавить форму регистрации:
* Сделать дизайн формы регистрации
* Добавить хеширование паролей или интегрировать регистрацию через сторонние аккаунты

### 4) Подключить базу данных:
* Определить, какие данные будут храниться в базе данных (данные о товарах, фотографии, пароли, логины, товары в корзине). Решить, какие товары будут на сайте и как их добавлять (через админ-панель или другими способами)
  
### 5) Поместить сайт на vps:
* Настроить VPS и скачать все необходимые пакеты
* Создать виртуальное окружение
* Переместить проект на vps
* Настроить и запустить Gunicorn
* Настроить Nginx
* Установить HTTPS:
  + Установить Certbot
  + Настроить SSL

### 6) Проверить на наличие багов и показать преподавателю

## Стек:

### **Frontend**:
1. **HTML**: Создание структуры страниц.
2. **CSS**: 
   - Для стилизации страниц.
   - Подключение шрифтов 
   - Реализация адаптивности
3. **JavaScript**:
   - Реализация интерактивности 
   - Использование библиотек 
4. **AJAX**: Для отправки и получения данных без перезагрузки страницы (например, добавление товаров в корзину).



### **Backend**:
1. **Django**: Основной фреймворк для разработки бэкенда.
   - Управление логикой приложения.
   - Работа с базой данных.
   - Работа с шаблонами через Django Template Engine.
3. **Django Admin**: Для управления контентом (добавление/редактирование товаров и категорий).



### **Database (База данных)**:
1. **SQLite**:



### **DevOps**:
1. **Gunicorn**:
   - WSGI-сервер для работы Django.
2. **Nginx**:
   - Веб-сервер для обработки запросов и управления статическими файлами.
3. **Certbot**:
   - Для настройки HTTPS (SSL-сертификатов).



### **Библиотеки и пакеты Django**:
1. **django-allauth**:
   - Для аутентификации через социальные сети.
2. **django-filter**:
   - Для фильтрации товаров (по цене, категории и другим параметрам).
3. **Pillow**:
   - Для работы с изображениями.

---

## Процесс разработки:

### День первый: 
Написал план разработки и стек, который буду использовать. Создал проект Django, добавил все файлы, которые могут понадобиться в будущем. Добавил шрифты и в коде записал все цвета, которые буду использовать, добавил библиотеку Typpy.js.

На этом этапе сайт выглядит так:

![Screenshot_26-ноя_15-28-02_5279](https://github.com/user-attachments/assets/f7b6fb28-2622-4d81-995c-8b95e1c8240f)








## Заметки во время разработки:

### Цвета для сайта:
<img src="https://visme.co/blog/wp-content/uploads/2016/09/website12-1024x512.jpg"/>

### Шрифты для сайта:
Для заголовка - Nunito

Для остального текста - Nunito Sans

### Что дополнительно можно добавить на сайт?
1. Tippy.js


### Какие страницы нужно сверстать:
1. Форму регистрации или 2 кнопку с регистрацией через дургие аккаунты
2. Главное меню с товарами
3. Страница товара
4. Корзина
-----

### Что не так важно:
1. Админ-панель
2. Избранные
3. Профиль 

