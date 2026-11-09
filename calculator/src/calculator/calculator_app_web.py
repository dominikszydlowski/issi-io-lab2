from flask import Flask, request
from .calculator import Calculator

app = Flask(__name__)


@app.route("/calculate")
def calculate():
    op = request.args.get("op", type=str)
    arg1 = request.args.get("arg1", type=int)
    arg2 = request.args.get("arg2", type=int)

    if op is None or arg1 is None or arg2 is None:
        return {"error": "Missing or invalid parameters"}, 400

    calc = Calculator(arg1, arg2)
    op_txt = ""

    match op:
        case "sum":
            op_txt = "+"
            result = calc.sum()
        case "sub":
            op_txt = "-"
            result = calc.subtract()
        case "mul":
            op_txt = "*"
            result = calc.multiply()
        case "div":
            op_txt = "/"
            if arg2 == 0:
                return {"error": "Division by zero"}, 400
            result = calc.divide()
        case _:
            return {"error": "Unknown operation"}, 400

    return f"{arg1} {op_txt} {arg2} = {result}"
    
