


from base_response import BaseResponse


def health_check():
    return  BaseResponse(message="Servicio activo",status_code=200)