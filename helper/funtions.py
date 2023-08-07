class ResponseHandling:
    def failure_response_message(detail,result):
        """
        error message for failure
        :param detail: message to show in detail
        :param result : message or result to show
        :returns: dictionary
        """
        return {'detail' : detail, 'result' : result}

    def success_response_message(detail,result):
        """
        success message for Success
        :param detail: message to show in detail
        :param result : message or result to show
        :returns: dictionary
        """
        return {'detail' : detail, 'result' : result}
    
def error_message_function(errors):
    """
    return error message when serializer is not valid
    :param errors: error object
    :returns: string
    """
    for key, values in errors.items():
        error = [value[:] for value in values]
        err = ' '.join(map(str,error))
        return err
