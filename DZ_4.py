from datetime import datetime


# 1. Создайте словарь email,
email = {
    "subject": " Quarterly Report ",
    "from": " Alice.Cooper@Company.ru ",
    "to": "  bob_smith@Gmail.com  ",
    "body": "Hello Bob,\n\tHere is the quarterly report.\n\tPlease review and let me know your feedback.\n\nBest,\nAlice"
}

# 2. Добавьте дату отправки

email["date"] = send_date = datetime.now().strftime("%y-%m-%d")


#3. Нормализуйте e-mail адреса отправителя и получателя:

email["from"] = email["from"].strip().lower()
email["to"] = email["to"].strip().lower()

#4. Извлеките логин и домен отправителя в две переменные login и domain.
login = email["from"].split('@')[0]
domain = email["from"].split('@')[-1]

# Создайте сокращённую версию текста: возьмите первые 10 символов email["body"] и добавьте многоточие "...".
 Сохраните в новый ключ словаря: email["short_body"].

email["body"] = email["body"][:10] + "..."

# Списки доменов: создайте список личных доменов

domain_personal = ['gmail.com','list.ru', 'yahoo.com','outlook.com','hotmail.com','icloud.com','yandex.ru','mail.ru','list.ru','bk.ru','inbox.ru','company.ru']
domain_corporate = ['company.ru','corporation.com','university.edu','organization.org','company.ru', 'business.net']
domain_personal = list(set(domain_personal))
domain_corporate = list(set(domain_corporate))

# 7. Проверьте что в списке личных и корпоративных доменов нет пересечений: ни один домен не должен входить в оба списка одновременно.

common_domains = set(domain_personal) & set(domain_corporate)



