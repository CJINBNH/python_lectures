import modelSub as model
import view

def buttonClick():
    value_a = view.getValue()
    value_b = view.getValue()
    model.init(value_a, value_b)
    result = model.do()
    view.viewData(result, "результат действия")