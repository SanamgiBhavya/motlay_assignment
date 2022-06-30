class GetErrorResponseObject:

    @staticmethod
    def get_error_response_object(error_constant):
        import json
        from django.http.response import HttpResponse

        data = {
            "status_code": error_constant[2],
            "message": error_constant[0],
            "res_status": error_constant[1]
        }
        return HttpResponse(content=json.dumps(data), status=error_constant[2])
