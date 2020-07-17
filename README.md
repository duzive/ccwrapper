CCWrapper (v 1.0.0)
=================================================================================================================================================================================
** CCWrapper ** - это python модуль для упрощенной работы с CatCoin API
* [Сам модуль](./ccwrapper) (python3)

### Установка модуля
* Через pip из Pypi
```bash
pip install ccwrapper
```
* Через pip из GitHub
```bash
pip install https://github.com/Duzive/ccwrapper/archive/master.zip --upgrade
```
Работа с модулем
---
### Быстрый старт
***Для начала создадим экземпляр основного класса***
```python /* или python3 */
from ccwrapper import CatCoinWrapper

Wrapper = CatCoinWrapper(user_id = 12345678, token = "your_token")
```
* `user_id` - Ваш ID Вконтакте
* `token` - Ключ CatCoin Api(получаем [здесь](https://vk.com/app7044895#getapikey))


## Использование
### --> make_transfer
***Выполнить перевод CatCoin с вашего кошелька на другой***
##### Python
```python /* или python3 */
Wrapper.make_transfer(toid = 12345678, amount = 2, mark = 1)
```
* `toid` - id получателя 
* `amount` - сумма перевода
* `mark` - отображать название магазина в переводе(по умолчанию: 0)

### --> get_users_score
***Вывод баланса пользователя***
##### Python
```python /* или python3 */
Wrapper.get_users_score(user_ids = [12345678])
```
* `user_ids` - id пользователей, баланс которых нужно получить(обязательно массив)

### --> get_transfer_history
***Получить историю переводов***
##### Python
```python /* или python3 */
Wrapper.get_transfer_history(tx = 2)
```
* `tx` - парамент вывода истории переводов(по умолчанию: 1)

### --> set_shop_name
***Установить новое название магазина***
##### Python
```python /* или python3 */
Wrapper.set_shop_name(new_name = 'RadMate Shop')
```
* `new_name` - новое название

### --> set_callback
***Установить новый callback-сервер***
**Учтите, ваш сервер должен вернуть 'YES'**
```python /* или python3 */
Wrapper.set_callback(callback_url = "https:/radmate.ru/server")
```
* `callback_url` - адрес нового сервера

### --> get_lost_transfer
***Получить пропущенные переводы по callback***
```python /* или python3 */
Wrapper.get_lost_transfer()
```
* аргументы не требуются

### --> LongPolling
**модуль также нативно поддерживает простой LongPolling**
**Для этого используется отдельный класс "CCPoll" с передачей экземпляра класса "CatCoinWrapper"**
```python /* или python3 */
from ccwrapper import CCPoll

for payment in CCPoll(Wrapper).listen(sleep = 5):

    user_id = payment["id"]
    amount = payment["amount"]
    payload = payment["payload"]

    print(f'Получен платёж на сумму: {amount}, от @id{user_id}, payload: {payload}')
```
* `sleep` - период проверки платежей(по умолчанию: 3)

## Дополнительно
* [Разработчик](http://vk.com/duzive)
* [Официальная документация](https://documenter.getpostman.com/view/8482328/SVfGzCCM?version=latest)
* Буду рад 🌟
