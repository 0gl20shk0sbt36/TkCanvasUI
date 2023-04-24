# 导入表示子类的类型提示


class BaseShape:
    """形状检测体的基类"""

    def __init__(self, point=(0, 0), centre=(0, 0), contrary=False):
        """形状检测体的基类

        :param point: 表示坐标的元组
        :param centre: 中心点坐标，它是一个包含中心点的x和y坐标的元组
        :param contrary: 一个布尔值，用于确定是否将结果取反。如果它被设置为True，旋转将在相反的方向，默认值到False(可选)
        """
        self.contrary = contrary
        self.point = point
        self.centre = centre
        self.collision_fun = None

    def get_key(self):
        """获取关键数据"""
        pass

    def collision(self, point: tuple[float, float]) -> bool:
        """检测是否碰撞

        :param point: 点坐标
        :return: 返回一个布尔值，表示是否碰撞
        """
        pass

    def get_mbr(self) -> tuple[tuple[float, float], tuple[float, float]]:  # type: ignore
        """获取最小外接矩形

        :return: 返回一个元组，包含最小外接矩形的左上角和右下角的坐标
        """
        pass

    def copy(self):
        """复制

        :return: 返回一个新的形状检测体
        """
        pass
