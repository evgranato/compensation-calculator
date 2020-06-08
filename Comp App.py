import ui

def calculator(myInterface):
	viewSelector = myInterface.superview
	cost = viewSelector["cost"].text
	margin = viewSelector["margin"].text
	answer = round(int(cost) / (1 - int(margin)/100), 2)
	compensation = round((answer-int(cost)) * .20, 2)
	viewSelector["answer"].text = f"The quoted price should be ${answer} and your compensation will be ${compensation}"
	#viewSelector["answer"].text = "yeat"
	

v = ui.load_view()
v.present('sheet')

