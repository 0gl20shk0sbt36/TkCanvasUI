import inspect

def my_function():
    caller = inspect.stack()[1]
    caller_frame = caller[0]
    caller_globals = caller_frame.f_globals
    caller_locals = caller_frame.f_locals
    variable_name = "my_variable"
    if variable_name in caller_locals:
        caller_locals[variable_name] = "new value"
    elif variable_name in caller_globals:
        caller_globals[variable_name] = "new value"
