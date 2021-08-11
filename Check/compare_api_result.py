# coding:utf-8
# @Author: wang_cong
from Utils.operation_log import initLogger

logger = initLogger(__file__)


def compare_api_result(acture_data, expected_value, operator):
    """
    比较接口的实际结果和预期结果，返回比较成功或失败
    :param acture_data: 从实际结果中，提取出来的待比较的结果
    :param expected_value: 预期结果
    :param operator: 操作器
    :return: 返回比较成功或失败
    """
    try:
        # 假设比较结果的值是flag，默认是False
        flag = False
        # 注意：能执行下列代码的前提是：待比较的实际结果一定非空，不是None ，预期结果也一定非空，不是None
        if acture_data is None or acture_data == "":
            logger.error("待比较的实际结果为空，无法进行比较！")
        if expected_value is None or expected_value == "":
            logger.error("预期结果为空，无法进行比较！")
        # 对预期结果和实际结果的数据类型，进行分类比较
        if isinstance(acture_data, int):
            if isinstance(expected_value, int):
                if operator in ["==", "!=", "<", "<=", ">"]:
                    if operator == "==":
                        if acture_data == expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            logger.debug("预期结果等于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果不等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            flag = False
                    elif operator == "!=":
                        if acture_data != expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            logger.debug("预期结果不等于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            flag = False
                    elif operator == "<":
                        if acture_data > expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            logger.debug("预期结果小于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果大于等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            flag = False
                    elif operator == "<=":
                        if acture_data >= expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            logger.debug("预期结果小于等于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果大于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            flag = False
                    elif operator == ">":
                        if acture_data < expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            logger.debug("预期结果大于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果小于等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            flag = False
                else:
                    logger.error("当数据类型是int时，操作器的数据类型必须是==, !=, <, <=, > 里面的任意一种, 而当前的操作器的值是：{}".format(operator))
            else:
                logger.error("当实际结果是int类型时，预期结果不是int类型，而是：{} 类型，无法进行比较！".format(type(expected_value)))
        elif isinstance(acture_data, str):
            if isinstance(expected_value, str):
                if operator in ["==", "!=", "in", "not in"]:
                    if operator == "==":
                        if acture_data == expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            logger.debug("预期结果等于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果不等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            flag = False
                    elif operator == "!=":
                        if acture_data != expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            logger.debug("预期结果不等于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            flag = False
                    elif operator == "in":
                        if acture_data in expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            logger.debug("预期结果在待比较的接口返回值里，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果不在等于待比较的接口返回值里，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            flag = False
                    elif operator == "not in":
                        if acture_data not in expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            logger.debug("预结果不在待比较的接口返回值里，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果在待比较的接口返回值里，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            flag = False
                else:
                    logger.error("当数据类型是str时，操作器的数据类型必须是==, !=, in, not in 里面的任意一种, 而当前的操作器的值是：{}".format(operator))
            else:
                logger.error("当实际结果是str类型时，预期结果不是str类型，而是：{} 类型，无法进行比较！".format(type(expected_value)))
        elif isinstance(acture_data, bool):
            if isinstance(expected_value, bool):
                if operator in ["==", "!="]:
                    if operator == "==":
                        if acture_data == expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            logger.debug("预期结果等于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果不等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            flag = False
                    elif operator == "!=":
                        if acture_data != expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            logger.debug("预期结果不等于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            flag = False
                else:
                    logger.error("当数据类型是bool时，操作器的数据类型必须是==, != 里面的任意一种, 而当前的操作器的值是：{}".format(operator))
            else:
                logger.error("当实际结果是bool类型时，预期结果不是bool类型，而是：{} 类型，无法进行比较！".format(type(expected_value)))
        elif isinstance(acture_data, list):
            if isinstance(expected_value, list):
                if operator in ["==", "!="]:
                    if operator == "==":
                        if acture_data == expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            logger.debug("预期结果等于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果不等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            flag = False
                    elif operator == "!=":
                        if acture_data != expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            logger.debug("预期结果不等于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            flag = False
                else:
                    logger.error("当数据类型是list时，操作器的数据类型必须是==, != 里面的任意一种, 而当前的操作器的值是：{}".format(operator))
            else:
                logger.error("当实际结果是list类型时，预期结果不是list类型，而是：{} 类型，无法进行比较！".format(type(expected_value)))
        elif isinstance(acture_data, dict):
            if isinstance(expected_value, dict):
                if operator in ["==", "!="]:
                    if operator == "==":
                        if acture_data == expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            logger.debug("预期结果等于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果不等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            flag = False
                    elif operator == "!=":
                        if acture_data != expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            logger.debug("预期结果不等于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_data))
                            flag = False
                else:
                    logger.error("当数据类型是dict时，操作器的数据类型必须是==, != 里面的任意一种, 而当前的操作器的值是：{}".format(operator))
            else:
                logger.error("当实际结果是dict类型时，预期结果不是dict类型，而是：{} 类型，无法进行比较！".format(type(expected_value)))
        else:
            logger.error("当前实际结果的数据类型是：{} ，本套代码暂不支持对这种类型的数据，进行比较！".format(type(acture_data)))
        logger.info("预期结果与实际结果的比较结果是：{} ".format(flag))
        return flag
    except Exception as e:
        logger.error("比较预期结果和实际结果失败！报错信息是：{}".format(e))
