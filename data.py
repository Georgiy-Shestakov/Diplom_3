SERVICE_BASE_URL = 'https://stellarburgers.nomoreparties.site'

class Urls:
    login_page = f'{SERVICE_BASE_URL}/login'
    main_page = f'{SERVICE_BASE_URL}/'
    order_history_page = f'{SERVICE_BASE_URL}/account/order-history'
    order_feed_page = f'{SERVICE_BASE_URL}/feed'
    profile_page = f'{SERVICE_BASE_URL}/account/profile'
    recover_password_reset_page = f'{SERVICE_BASE_URL}/reset-password'
    recover_password_forgot_page = f'{SERVICE_BASE_URL}/forgot-password'
    

class User:
    login = 'gshestakov@ya.ru'
    password = '123456_qwerty'


INGREDIENT_NAMES = [
    'Флюоресцентная булка R2-D3',
    'Соус Spicy-X',
    'Сыр с астероидной плесенью'
    ]


drag_and_drop_js_script = """
const source = arguments[0];
const target = arguments[1];

const dataTransfer = new DataTransfer();
const dragStartEvent = new DragEvent('dragstart', { bubbles: true, cancelable: true, dataTransfer });
source.dispatchEvent(dragStartEvent);

const dragOverEvent = new DragEvent('dragover', { bubbles: true, cancelable: true, dataTransfer });
target.dispatchEvent(dragOverEvent);

const dropEvent = new DragEvent('drop', { bubbles: true, cancelable: true, dataTransfer });
target.dispatchEvent(dropEvent);

const dragEndEvent = new DragEvent('dragend', { bubbles: true, cancelable: true, dataTransfer });
source.dispatchEvent(dragEndEvent);
"""
