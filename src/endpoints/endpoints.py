from fastapi import APIRouter
from fastapi import Response
from fastapi import status
from fastapi import FastAPI
from bp import GetOrdenByIdUseCase
from bp import GetOrdenByIdParams
from data import OrdenRepositoryImp

router = APIRouter()


@router.get("/apis/orden/{orden_id}")

def get_orden_by_id(orden_id: str, response: Response):
    try:
        get_orden_by_id = GetOrdenByIdUseCase(
            OrdenRepositoryImp()
        )
        orden = get_orden_by_id.run(
            GetOrdenByIdParams(orden_id)
        )

        print(orden.to_json())
        return orden.to_json()
    except Exception as e:
        print(e)
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"code:", "message": str(e)}

def create_app():
    app = FastAPI()
    app.include_router(router)
    return app
