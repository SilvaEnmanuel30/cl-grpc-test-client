import grpc
import app.schemas.alert.alert_pb2 as alert__pb2
import app.schemas.alert.alert_pb2_grpc as alert__pb2_grpc

with grpc.insecure_channel('localhost:50051') as channel:
    data = {
        "id": 1,
        "code": "trastienda",
        "schedule": {
            "monday": {
                "start_time": "08:00:00",
                "end_time": "18:00:00"
            },
            "tuesday": {
                "start_time": "08:00:00",
                "end_time": "18:00:00"
            },
            "wednesday": {
                "start_time": "08:00:00",
                "end_time": "18:00:00"
            },
            "thursday": {
                "start_time": "08:00:00",
                "end_time": "18:00:00"
            },
            "friday": {
                "start_time": "08:00:00",
                "end_time": "18:00:00"
            },
            "saturday": {
                "start_time": "08:00:00",
                "end_time": "18:00:00"
            },
            "sunday": {
                "start_time": "08:00:00",
                "end_time": "18:00:00"
            }
        }
    }
    stub = alert__pb2_grpc.AlertTypeControllerStub(channel)
    response = stub.UpdateAlertTypeSchedule(
        alert__pb2.AlertTypeScheduleRequest(**data)
    )
    print(response)
