<div align="center">
<img src="https://readme-typing-svg.demolab.com?font=Josefin+Sans&size=28&pause=1000&color=00F7F0&center=true&width=435&lines=Online-shop" alt="Typing SVG" />
</div>

## План разработки:

### 1) Создать пустой проект на Django:
* Созадть все необходимые файлы в проекте Django(html, js, css, sqlite, папку с фотографиями)

### 2) Сделать простую верстку:
* Написать разметку на html, сделать несколько страниц, добавить стили и js
* Использовать SVG, а не PNG
* Добавить шрифты
* Добавить адаптивность
* Не забыть добавлять переменные, которые могут в будущем пригодиться
  

### 3) Добавить форму регистрации:
* Сделать дизайн формы регистрации
* Добавить хеширование или сдлеать регистрацию через другие аккаунты

### 4) Подключить базу данных:
* Определить какие данные будуд храниться в БД(данные о товаре, фотография, пароли, логины, какие товары в корзине) и решить какие товары будут на сайте и как их добавлять(через админ панель или как то иначе)

### 5) Поместить сайт на vps:
* Настроить VPS и скачать все необходимые пакеты
* Создать виртуальное окружение
* Переместить проект на vps
* Настроить и запустить Gunicorn
* Настроить Nginx
* Установить HTTPS:
  + Установить Certbot
  + Настроить SSL

### 6) Проверить на наличие багов и показать преподу

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

## Заматки во время разработки:

### Цвета для сайта:
<img src="https://visme.co/blog/wp-content/uploads/2016/09/website12-1024x512.jpg"/>

### Шрифты для сайта:
Для заголовок - Nunito

Для остальногое текста - Nunito Sans


