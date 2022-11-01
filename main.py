import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from enums import *
from random import random

intro_uic = uic.loadUiType("intro.ui")[0]
type_uic = uic.loadUiType("type.ui")[0]
bread_uic = uic.loadUiType("menu_bread.ui")[0]
meat_uic = uic.loadUiType("menu_meat.ui")[0]
cheese_uic = uic.loadUiType("menu_cheese.ui")[0]
vegetable_uic = uic.loadUiType("menu_vegetable.ui")[0]
sauce_uic = uic.loadUiType("menu_sauce.ui")[0]
set_uic = uic.loadUiType("set.ui")[0]
beverage_uic = uic.loadUiType("beverage.ui")[0]
check_order_uic = uic.loadUiType("check_order.ui")[0]
payment_uic = uic.loadUiType("payment.ui")[0]
complete_uic = uic.loadUiType("complete.ui")[0]


class IntroWindow(QMainWindow, intro_uic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.OrderButton.clicked.connect(self.set_widget_index)

    def init_values(self):
        widget.order_type = None
        widget.bread_type = None
        widget.meat_type = None
        widget.cheese_type = None
        widget.vegetable_list = []
        widget.sauce_list = []
        widget.set_type = None
        widget.beverage = None

        menu_vegetable.LettuceButton.setChecked(False)
        menu_vegetable.AvocadoButton.setChecked(False)
        menu_vegetable.OliveButton.setChecked(False)
        menu_vegetable.OnionButton.setChecked(False)
        menu_vegetable.TomatoButton.setChecked(False)

        menu_sauce.MayonnaiseButton.setChecked(False)
        menu_sauce.ChiliButton.setChecked(False)
        menu_sauce.SrirachaButton.setChecked(False)
        menu_sauce.RanchButton.setChecked(False)
        menu_sauce.KetchupButton.setChecked(False)

    def set_widget_index(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)
        self.init_values()


class OrderTypeWindow(QMainWindow, type_uic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.goHomeButton.clicked.connect(self.get_previous_page)
        self.eatHereButton.clicked.connect(lambda: self.set_order_type(OrderType.EAT_HERE))
        self.takeOutButton.clicked.connect(lambda: self.set_order_type(OrderType.TO_GO))

    def get_previous_page(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def set_order_type(self, order):
        widget.order_type = order
        widget.setCurrentIndex(widget.currentIndex() + 1)


class MenuBreadWindow(QMainWindow, bread_uic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.BackButton.clicked.connect(self.get_previous_page)
        self.WheatBreadButton.clicked.connect(lambda: self.set_bread(Bread.WHEAT))
        self.WholeWheatBread.clicked.connect(lambda: self.set_bread(Bread.WHOLE_WHEAT))
        self.RiceBreadButton.clicked.connect(lambda: self.set_bread(Bread.RICE))

    def get_previous_page(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def set_bread(self, bread):
        widget.bread_type = bread
        widget.setCurrentIndex(widget.currentIndex() + 1)


class MenuMeatWindow(QMainWindow, meat_uic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.BackButton.clicked.connect(self.get_previous_page)
        self.SalmonButton.clicked.connect(lambda: self.set_meat(Meat.SALMON))
        self.ChickenButton.clicked.connect(lambda: self.set_meat(Meat.CHICKEN))
        self.HamButton.clicked.connect(lambda: self.set_meat(Meat.HAM))
        self.SteakButton.clicked.connect(lambda: self.set_meat(Meat.STEAK))

    def get_previous_page(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def set_meat(self, meat):
        widget.meat_type = meat
        widget.setCurrentIndex(widget.currentIndex() + 1)


class MenuCheeseWindow(QMainWindow, cheese_uic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.BackButton.clicked.connect(self.get_previous_page)
        self.AmericanButton.clicked.connect(lambda: self.set_cheese(Cheese.AMERICAN))
        self.CheddarButton.clicked.connect(lambda: self.set_cheese(Cheese.CHEDDAR))
        self.MozzarellaButton.clicked.connect(lambda: self.set_cheese(Cheese.MOZZARELLA))

    def get_previous_page(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def set_cheese(self, cheese):
        widget.cheese_type = cheese
        widget.setCurrentIndex(widget.currentIndex() + 1)


class MenuVegetableWindow(QMainWindow, vegetable_uic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.BackButton.clicked.connect(self.get_previous_page)
        self.SelectCompleteButton.clicked.connect(self.check_clicked_buttons)

    def get_previous_page(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def check_clicked_buttons(self):
        widget.vegetable_list = []
        if self.LettuceButton.isChecked():
            widget.vegetable_list.append(Vegetable.LETTUCE)
        if self.AvocadoButton.isChecked():
            widget.vegetable_list.append(Vegetable.AVOCADO)
        if self.OliveButton.isChecked():
            widget.vegetable_list.append(Vegetable.OLIVE)
        if self.OnionButton.isChecked():
            widget.vegetable_list.append(Vegetable.ONION)
        if self.TomatoButton.isChecked():
            widget.vegetable_list.append(Vegetable.TOMATO)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class MenuSauceWindow(QMainWindow, sauce_uic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.BackButton.clicked.connect(self.get_previous_page)
        self.SelectCompleteButton.clicked.connect(self.check_clicked_buttons)

    def get_previous_page(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def check_clicked_buttons(self):
        widget.sauce_list = []
        if self.MayonnaiseButton.isChecked():
            widget.sauce_list.append(Sauce.MAYONNAISE)
        if self.ChiliButton.isChecked():
            widget.sauce_list.append(Sauce.CHILI)
        if self.SrirachaButton.isChecked():
            widget.sauce_list.append(Sauce.SRIRACHA)
        if self.RanchButton.isChecked():
            widget.sauce_list.append(Sauce.RANCH)
        if self.KetchupButton.isChecked():
            widget.sauce_list.append(Sauce.KETCHUP)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class SetTypeWindow(QMainWindow, set_uic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.goBackButton.clicked.connect(self.get_previous_page)
        self.SingleButton.clicked.connect(lambda: self.set_type(SetType.SINGLE))
        self.SetButton.clicked.connect(lambda: self.set_type(SetType.SET))

    def get_previous_page(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def set_type(self, order):
        widget.beverage = None
        if order == SetType.SET:
            widget.set_type = SetType.SET
            widget.setCurrentIndex(widget.currentIndex() + 1)
        if order == SetType.SINGLE:
            widget.set_type = SetType.SINGLE
            widget.setCurrentIndex(widget.currentIndex() + 2)
            check_order.order_list()


class BeverageWindow(QMainWindow, beverage_uic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.BackButton.clicked.connect(self.get_previous_page)
        self.CokeButton.clicked.connect(lambda: self.set_beverage(Beverage.COKE))
        self.CiderButton.clicked.connect(lambda: self.set_beverage(Beverage.CIDER))
        self.CoffeeButton.clicked.connect(lambda: self.set_beverage(Beverage.COFFEE))
        self.WaterButton.clicked.connect(lambda: self.set_beverage(Beverage.WATER))

    def get_previous_page(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def set_beverage(self, beverage):
        widget.beverage = beverage
        check_order.order_list()
        widget.setCurrentIndex(widget.currentIndex() + 1)


class CheckOrderWindow(QMainWindow, check_order_uic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.goBackButton.clicked.connect(self.get_previous_page)
        self.PayButton.clicked.connect(self.payment_index)

        self.BreadButton.clicked.connect(lambda: self.page_move(2))
        self.MeatButton.clicked.connect(lambda: self.page_move(3))
        self.CheeseButton.clicked.connect(lambda: self.page_move(4))
        self.VegatableButton.clicked.connect(lambda: self.page_move(5))
        self.SauceButton.clicked.connect(lambda: self.page_move(6))
        self.BeverageButton.clicked.connect(lambda: self.page_move(8))


    def page_move(self, page):
        widget.setCurrentIndex(page)

    def order_list(self):

            if widget.order_type == OrderType.TO_GO:
                self.typeLabel.setText("테이크 아웃")
            elif widget.order_type == OrderType.EAT_HERE:
                self.typeLabel.setText("매장에서 식사")

            self.set_button(self.BreadButton, widget.bread_type)
            self.set_button(self.MeatButton, widget.meat_type)
            self.set_button(self.CheeseButton, widget.cheese_type)

            if widget.set_type == SetType.SINGLE:
                self.BeverageButton.hide()
            elif widget.set_type == SetType.SET:
                self.BeverageButton.show()
                self.set_button(self.BeverageButton, widget.beverage)

    def set_button(self, button, value):
        elem = type(value)
        button.setText(elem.get_meta(value)[0])
        button.setIcon(QIcon(elem.get_meta(value)[1]))

    def get_previous_page(self):
       widget.setCurrentIndex(widget.currentIndex() - 2)

    def payment_index(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)
        payment.re_draw_form()


class PaymentWindow(QMainWindow, payment_uic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.goBackButton.clicked.connect(self.get_previous_page)
        self.CompleteButton.clicked.connect(self.set_complete_index)

    def get_price(self):
        price = Bread.get_meta(widget.bread_type)[-1] + Meat.get_meta(widget.meat_type)[-1] + Cheese.get_meta(
            widget.cheese_type)[-1] + Vegetable.get_price() + Sauce.get_price()

        if widget.beverage:
            price += Beverage.get_meta(widget.beverage)[-1]
        return price

    def get_detail(self):

        if widget.order_type == OrderType.TO_GO:
            text = "테이크 아웃\n\n"
        elif widget.order_type == OrderType.EAT_HERE:
            text = "매장에서 식사\n\n"

        text += "{} \t {}원\n".format(Bread.get_meta(widget.bread_type)[0], Bread.get_meta(widget.bread_type)[-1])
        text += "{} \t {}원\n".format(Meat.get_meta(widget.meat_type)[0], Meat.get_meta(widget.meat_type)[-1])
        text += "{} \t {}원\n".format(Cheese.get_meta(widget.cheese_type)[0], Cheese.get_meta(widget.cheese_type)[-1])

        temp = ""
        for item in widget.vegetable_list:
            temp += Vegetable.get_title(item)
            temp += " "
        text += "{} \t {}원\n".format(temp.strip(), Vegetable.get_price())

        temp = ""
        for item in widget.sauce_list:
            temp += Sauce.get_title(item)
            temp += " "
        text += "{} \t {}원\n".format(temp.strip(), Sauce.get_price())

        if widget.beverage:
            text += "{} \t {}원\n".format(Beverage.get_meta(widget.beverage)[0],
                                         Beverage.get_meta(widget.beverage)[-1])

        return text

    def re_draw_form(self):
        self.PriceLabel.setText("{}원을 결제합니다.".format(self.get_price()))
        self.DetailLabel.setText(self.get_detail())

    def get_previous_page(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def set_complete_index(self):
        widget.setCurrentIndex(widget.currentIndex() + 1)
        complete.re_draw_page()


class CompleteWindow(QMainWindow, complete_uic):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.InitButton.clicked.connect(self.set_widget_index)

    def re_draw_page(self):
        self.OrderNumLabel.setText(str(int(random() * 10000)))

    def set_widget_index(self):
        widget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QStackedWidget()

    widget.order_type = None
    widget.bread_type = None
    widget.meat_type = None
    widget.cheese_type = None
    widget.vegetable_list = list()
    widget.sauce_list = list()
    widget.set_type = None
    widget.beverage = None

    intro = IntroWindow()
    order_type = OrderTypeWindow()
    menu_bread = MenuBreadWindow()
    menu_meat = MenuMeatWindow()
    menu_cheese = MenuCheeseWindow()
    menu_vegetable = MenuVegetableWindow()
    menu_sauce = MenuSauceWindow()
    set_type = SetTypeWindow()
    beverage_type = BeverageWindow()
    check_order = CheckOrderWindow()
    payment = PaymentWindow()
    complete = CompleteWindow()

    widget.addWidget(intro)
    widget.addWidget(order_type)
    widget.addWidget(menu_bread)
    widget.addWidget(menu_meat)
    widget.addWidget(menu_cheese)
    widget.addWidget(menu_vegetable)
    widget.addWidget(menu_sauce)
    widget.addWidget(set_type)
    widget.addWidget(beverage_type)
    widget.addWidget(check_order)
    widget.addWidget(payment)
    widget.addWidget(complete)

    widget.show()
    app.exec_()