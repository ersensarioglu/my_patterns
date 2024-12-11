In this folder we are using Model-View-Controller pattern.
nomvc.py has an implementation which doesn't use any pattern.
We have split the same functionality into four code
mymodel.py is responsible for data
myview.py is responsible for presentation of function
mycontroller.py has the application logic that coordinates data and presentation
This application is run by mymvc.py

Also we have implemented strategy pattern for deciding which format to use for generation of uuid
uuid_strategy.py is the abstract for the strategy
3 different strategy is available inside uuid1_uuid_strategy.py, uuid4_uuid_strategy.py and simple_uuid_strategy_py.
main application mymvc.py is using uuid4 strategy.
We can add another strategy without changing any code, by simply adding another class file with details of strategy.
So there is a big advantage as we are not touching any code implementing other strategies, which means no regression impact