import grpc
import app.schemas.alert.alert_pb2 as alert__pb2
import app.schemas.alert.alert_pb2_grpc as alert__pb2_grpc

with grpc.insecure_channel('localhost:50051') as channel:
    data = {
        "alert_type": [
            "perimeter",
            "sala-venta",
            "trastienda"
        ]
    }
    stub = alert__pb2_grpc.AlertTypeControllerStub(channel)
    response = stub.ListAlertTypeSchedule(
        alert__pb2.ListAlertTypeScheduleRequest(**data)
    )
    print(response)
