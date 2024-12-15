nosolid.py is written without **solid principles**.

First principle we will look at it is **single responsibility**, 
which means each class is responsible for one thing only.
For that purpose, we have split into PaymentProcessor and Order class.

Second principle is **open/closed**, which means code is open for extension
but closed for modification. So you can add new functionality without
impacting existing code.
In order to do that, we have made PaymentProcessor an abstract class
and created further classes for different payment types like
debit payment, credit payment and paypal

Third principle is **Liskov principle** which means you can replace objects
with instances of their sub classes without altering correctness of program.
For this purpose, differentiating parameter (security code/email) is put into initialiser

Fourth principal is **interface segregation** which means it is better to have
several **interfaces** rather than one single.
For example we can use **inheritence** by creating sub class for payment processor with sms authentication
And we use this subclass where required, in this case in debit payment processor.
Another option is to user **composition** which is to create a class for sms authorization
and pass this to payment class as argument, which is used in paypal payment processor.

Fifth principal is **Dependency inversion** which means classes to depend on **abstractions**,
not on concrete subclasses. So we can make an abstract class Authorizer and different implementations
can be inheriting on that like sms auth and not a robot classes

