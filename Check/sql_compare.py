# coding:utf-8
# @Author: wang_cong
from Check.compare_sql_result import compare_sql_result
from Utils.operation_log import initLogger

logger = initLogger(__file__)


def sql_compare(acture_result, operator, expected_value, extract_path):
    """
    比较预期结果和实际结果，返回比较失败或者成功
    :param acture_result: 实际结果
    :param operator: 操作器
    :param expected_value: 预期结果
    :param extract_path: 实际结果的提取路径
    :return: 返回SQL比较失败或者成功
    """
    try:
        # 注意：进行比较的实际结果和预期结果，传入这个方法时，皆为非空
        hang_count = len(acture_result)
        logger.info("当前SQL查询结果的总行数为：{}".format(hang_count))
        # 假设结果比较的值flag，默认是False
        flag = False
        # 从实际SQL返回值中，通过提取路径，得到准备需要进行SQL校验的数据
        # 先判断查询出来的实际结果，是否为空
        split_path = extract_path.split(".")
        if len(split_path) == 1:
            if split_path[0] == "$":
                logger.info("说明把整个SQL查询结果，当做实际结果，与预期结果进行比较")
                # 进行比较，此时的实际结果是极有可能不是特指某个字段的值，所以，数据类型是tuple，具体是几个字段，要看总列数
                logger.info("预期结果是：{}".format(expected_value))
                logger.info("要与预期结果进行比较的实际结果是：{}".format(acture_result))
                flag = compare_sql_result(acture_result, expected_value, operator)
        elif len(split_path) == 2:
            hang = int(split_path[1])
            lie_count = len(acture_result[hang - 1])
            logger.info("当前SQL查询结果，每条数据的总列数是：{}".format(lie_count))
            logger.info("取SQL查询结果的第{}行数据，当做实际结果，与预期结果进行比较".format(hang))
            # 判断行号是否有效
            if hang <= hang_count:
                # 获取进行比较的实际结果
                acture_result = acture_result[hang - 1]
                # 进行比较，此时的实际结果是极有可能不是特指某个字段的值，所以，数据类型是tuple，具体是几个字段，要看总列数
                logger.info("预期结果是：{}".format(expected_value))
                logger.info("要与预期结果进行比较的实际结果是：{}".format(acture_result))
                flag = compare_sql_result(acture_result, expected_value, operator)
            else:
                logger.error("当前输入的行号是：{} ，大于等于总行数：{} ，行号无效，请检查后重新输入！".format(hang, hang_count))
        elif len(split_path) == 3:
            hang = int(split_path[1])
            lie = int(split_path[2])
            lie_count = len(acture_result[hang - 1])
            logger.info("当前SQL查询结果，每条数据的总列数是：{}".format(lie_count))
            logger.info("取SQL查询结果的第{}行第{}列的数据，进行使用".format(hang, lie))
            # 判断行号是否有效
            if hang <= hang_count:
                # 判断列号是否有效
                if lie <= lie_count:
                    # 获取进行比较的实际结果
                    acture_result = acture_result[hang - 1][lie - 1]
                    # 进行比较，此时的实际结果是具体某个字段的值，数据类型是str
                    logger.info("预期结果是：{}".format(expected_value))
                    logger.info("要与预期结果进行比较的实际结果是：{}".format(acture_result))
                    flag = compare_sql_result(acture_result, expected_value, operator)
                else:
                    logger.error("当前输入的列号是：{} ，大于等于总列数：{} ，列号无效，请检查后重新输入！".format(lie, lie_count))
            else:
                logger.error("当前输入的行号是：{} ，大于等于总行数：{} ，行号无效，请检查后重新输入！".format(hang, hang_count))
        else:
            logger.info("SQL查询结果的path错误！直接判断为 FAIL ")
            flag = False
        return flag
    except Exception as e:
        logger.error("SQL-比较实际结果和预期结果失败！报错信息是：{}".format(e))
