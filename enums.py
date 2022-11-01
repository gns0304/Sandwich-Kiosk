from enum import Enum


class OrderType(Enum):
    EAT_HERE = 0
    TO_GO = 1


class Bread(Enum):
    WHEAT = 0
    WHOLE_WHEAT = 1
    RICE = 2

    @staticmethod
    def get_meta(item):
        if item == Bread.WHEAT:
            return ("밀빵", "src/images/assets/bread/wheat_bread.png", 1000)
        elif item == Bread.WHOLE_WHEAT:
            return ("통밀빵", "src/images/assets/bread/whole_wheat_bread.png", 1000)
        elif item == Bread.RICE:
            return ("쌀빵", "src/images/assets/bread/rice_bread.png", 1000)


class Meat(Enum):
    SALMON = 0
    HAM = 1
    CHICKEN = 2
    STEAK = 3

    @staticmethod
    def get_meta(item):
        if item == Meat.SALMON:
            return ("연어", "src/images/assets/meat/salmon.png", 1000)
        elif item == Meat.HAM:
            return ("햄", "src/images/assets/meat/ham.png", 1000)
        elif item == Meat.CHICKEN:
            return ("닭가슴살", "src/images/assets/meat/chicken_breast.png", 1000)
        elif item == Meat.STEAK:
            return ("스테이크", "src/images/assets/meat/steak.png", 1000)



class Cheese(Enum):
    AMERICAN = 0
    CHEDDAR = 1
    MOZZARELLA = 2

    @staticmethod
    def get_meta(item):
        if item == Cheese.AMERICAN:
            return ("아메리칸", "src/images/assets/cheese/american.png", 1000)
        elif item == Cheese.CHEDDAR:
            return ("체다", "src/images/assets/cheese/cheddar.png", 1000)
        elif item == Cheese.MOZZARELLA:
            return ("모짜렐라", "src/images/assets/cheese/mozzarella.png", 1000)


class Vegetable(Enum):
    LETTUCE = 0
    AVOCADO = 1
    OLIVE = 2
    ONION = 3
    TOMATO = 4

    @staticmethod
    def get_price():
        return 1000

    @staticmethod
    def get_title(item):
        if item == Vegetable.LETTUCE:
            return "양상추"
        elif item == Vegetable.AVOCADO:
            return "아보카도"
        elif item == Vegetable.OLIVE:
            return "올리브"
        elif item == Vegetable.ONION:
            return "적양파"
        elif item == Vegetable.TOMATO:
            return "토마토"


class Sauce(Enum):
    MAYONNAISE = 0
    CHILI = 1
    SRIRACHA = 2
    RANCH = 3
    KETCHUP = 4

    @staticmethod
    def get_price():
        return 1000

    @staticmethod
    def get_title(item):
        if item == Sauce.MAYONNAISE:
            return "마요네즈"
        elif item == Sauce.CHILI:
            return "칠리"
        elif item == Sauce.SRIRACHA:
            return "스리라차"
        elif item == Sauce.RANCH:
            return "랜치"
        elif item == Sauce.KETCHUP:
            return "케첩"


class SetType(Enum):
    SINGLE = 0
    SET = 1


class Beverage(Enum):
    COKE = 0
    CIDER = 1
    COFFEE = 2
    WATER = 3

    @staticmethod
    def get_meta(item):
        if item == Beverage.COKE:
            return ("콜라", "src/images/assets/beverage/coke.png", 1000)
        elif item == Beverage.CIDER:
            return ("사이다", "src/images/assets/beverage/cider.png", 1000)
        elif item == Beverage.COFFEE:
            return ("아메리카노", "src/images/assets/beverage/coffee.png", 1000)
        elif item == Beverage.WATER:
            return ("생수", "src/images/assets/beverage/water.png", 1000)

