# 导入表示子类的类型提示


class BaseShape:
    """形状检测体的基类
    子类必须定义自己的collision_fun变量
    self.name: 名称
    self.contrary: 一个布尔值，用于确定是否将结果取反。如果它被设置为True，判定结果将被取反，默认值到False(可选)
    self.point: 表示坐标的元组
    self.collision_fun: 碰撞函数
    """

    def __new__(cls, *args, **kwargs):
        if cls is BaseShape:
            raise ValueError("BaseShape can't be instantiated")
        shape = super().__new__(cls)
        shape.name = cls.__name__
        return shape

    def __init__(self, point=(0, 0), contrary=False):
        """形状检测体的基类

        :param point: 表示坐标的元组
        :param contrary: 一个布尔值，用于确定是否将结果取反。如果它被设置为True，判定结果将被取反，默认值到False(可选)
        """
        self.name = None
        self.contrary = contrary
        self.point = point
        self.collision_fun = None

    def get_key(self):
        """获取关键数据"""
        pass

    def collision(self, point: tuple[float, float]) -> bool:
        """检测是否碰撞

        :param point: 点坐标
        :return: 返回一个布尔值，表示是否碰撞
        """
        return self.collision_fun(self.get_key(), point)

    def get_mbr(self) -> tuple[tuple[float, float], tuple[float, float]]:
        """获取最小外接矩形

        :return: 返回一个元组，包含最小外接矩形的左上角和右下角的坐标
        """
        pass

    def copy(self):
        """复制

        :return: 返回一个新的形状检测体
        """
        pass
