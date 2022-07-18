from rest_framework.views import exception_handler

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        customized_response = {}
        customized_response['message'] = []

        for key, value in response.data.items():
            field = key
            field_value = value[0]
            if 'playerSkills' in key:
                field = 'skill'
                field_value = value[0]['skill'][0]

            error = f'Invalid value for {field}: {field_value}'
            customized_response['message'] = error

        response.data = customized_response

    return response