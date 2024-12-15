from orders import Order
from paypal_payment_processor import PaypalPaymentProcessor
from sms_auth import SMSAuth

order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("Monitor", 2, 100)
order.add_item("Mouse", 1, 25)

print(order.total_price())
authorizer = SMSAuth()
processor = PaypalPaymentProcessor("a@b.com", authorizer)
authorizer.verify_code("123456")
processor.pay(order)