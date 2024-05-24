from ...lib.action import Action
from pydantic import BaseModel, Field


class CalculatorRequest(BaseModel):
    operation: str = Field(..., description="A mathematical expression, a couple examples are `200*7` or `5000/2*10`")


class CalculatorResponse(BaseModel):
    result: str = Field(..., description="Result of the calculation")


class Calculator(Action):
    """
    Useful to perform any mathematical calculations, like sum, minus, multiplication, division, etc.
    """
    _display_name = "Make a calculation"
    _request_schema = CalculatorRequest
    _response_schema = CalculatorResponse
    _tags = ["calculation"]

    def execute(self, request_data: _request_schema, authorisation_data: dict = {}):
        operation_str = request_data.dict()["operation"]
        try:
            result = eval(operation_str)
            execution_details = {"executed": True}
            response_data = result
        except Exception as e:
            execution_details = {"executed": False}
            response_data = {"error": e}

        return {
            "execution_details": execution_details,
            "response_data": response_data
        }
