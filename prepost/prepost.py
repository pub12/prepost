
class PreCond():
    ####################################################################################
    @classmethod
    def equals(cls, test_args ):
        def main_decorator(original_func):
            def wrapper_func(*args, **kwargs):

                test_ok = True
                for test_arg_item in test_args:
                    if test_arg_item in kwargs:
                        if kwargs[ test_arg_item ] != test_args[ test_arg_item ]:
                            raise Exception(f"Error in args - for {test_arg_item} expect [{test_args[ test_arg_item ]}] input [{kwargs[ test_arg_item ]}]" )
                return original_func(*args, **kwargs)
                    
            return wrapper_func
        return main_decorator

    ####################################################################################
    @classmethod
    def not_null(cls, test_args ):
        def main_decorator(original_func):
            def wrapper_func(*args, **kwargs):

                test_ok = True
                for test_arg_item in test_args:
                    if test_arg_item in kwargs:
                        if kwargs[ test_arg_item ] == None and kwargs[ test_arg_item ] == '' :
                            raise Exception(f"Error in args - for {test_arg_item} expect to be not empty" )
                
                return original_func(*args, **kwargs)
                
            return wrapper_func
        return main_decorator

class PostCond():
    ####################################################################################
    @classmethod
    def not_null(cls ):
        def main_decorator(original_func):
            def wrapper_func(*args, **kwargs):
                ret_value = original_func(*args, **kwargs)
                if ret_value == None: raise Exception(f"Error in return value - expect not null" )
                return ret_value
            return wrapper_func
        return main_decorator