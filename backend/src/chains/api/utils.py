from rest_framework.response import Response

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass()
class JSONResponse:
    message: str = ""
    error: bool = False
    data: Optional[Dict[Any, Any]] = None

    def response(self) -> Response:
        return Response({
            "message": self.message,
            "error": self.error,
            "data": self.data
        })
