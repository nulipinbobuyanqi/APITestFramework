# coding:utf-8
# @Author: wang_cong
from Check.compare_api_result import compare_api_result
from Utils.operation_log import initLogger

logger = initLogger(__file__)


def compare_sql_result(acture_result, expected_value, operator):
    """
    比较SQL的实际结果和预期结果，返回比较成功或失败
    :param acture_result: 从实际结果中，提取出来的待比较的结果
    :param expected_value: 预期结果
    :param operator: 操作器
    :return: 返回比较成功或失败
    """
    try:
        # 假设比较结果的值是flag，默认是False
        flag = False
        # 注意：能执行下列代码的前提是：待比较的实际结果一定非空，不是None ，预期结果也一定非空，不是None
        # 注意：传过来的SQL查询结果，一定不是空的
        # 注意：传过来的SQL查询结果，其数据类型一定是tuple
        # 注意：传过来的SQL预期结果，其数据类型一定是tuple,但具体的每个预期结果，其数据类型一定是dict
        # 注意：传过来的SQL预期结果，默认其key的顺序与查询结果的顺序一致，在此基础上，做的判断
        # 对预期结果和实际结果的数据类型，进行分类比较
        if isinstance(expected_value, tuple):
            if isinstance(acture_result, tuple):
                # 先判断SQL预期结果，其长度
                if len(expected_value) == 1:
                    logger.info("表示仅对一条查询结果进行比较")
                    # 遍历每个预期结果
                    for i in range(len(expected_value)):
                        every_expected_result = expected_value[i]
                        logger.info("当前正在对第{}个预期结果：{} 进行比较".format(i + 1, every_expected_result))
                        # 判断其数据类型，并对其进行比较
                        if isinstance(every_expected_result, dict):
                            # 判断其所有key组成的列表长度是否与SQL查询出来的实际结果一致
                            key_list = list(every_expected_result.keys())
                            if len(key_list) == len(acture_result):
                                # 获取要与实际结果进行比较的预期结果
                                expected_value = []
                                for key in key_list:
                                    value = every_expected_result[key]
                                    expected_value.append(value)
                                # 进行比较
                                acture_result = list(acture_result)
                                # 调用比较方法
                                flag = compare_api_result(acture_result, expected_value, operator)
                            else:
                                logger.error("第{}个预期结果，其所有字段的长度与实际结果不相等，无法进行比较！".format(i + 1))
                else:
                    logger.info("表示需要对多条查询结果进行比较")
                    # 先判断预期结果和实际结果的长度，是否一致
                    if len(acture_result) == len(expected_value):
                        # 遍历每个预期结果
                        for i in range(len(expected_value)):
                            every_expected_result = expected_value[i]
                            logger.info("当前正在对第{}个预期结果：{} 进行比较".format(i + 1, every_expected_result))
                            every_acture_result = acture_result[i]
                            logger.info("当前正在对第{}个实际结果：{} 进行比较".format(i + 1, every_acture_result))
                            # 判断其数据类型，并对其进行比较
                            if isinstance(every_expected_result, dict):
                                # 判断其所有key组成的列表长度是否与SQL查询出来的实际结果一致
                                key_list = list(every_expected_result.keys())
                                if len(key_list) == len(every_acture_result):
                                    # 获取要与实际结果进行比较的预期结果
                                    expected_data = []
                                    for key in key_list:
                                        value = every_expected_result[key]
                                        expected_data.append(value)
                                    # 进行比较
                                    acture_data = list(every_acture_result)
                                    # 调用比较方法
                                    flag = compare_api_result(acture_data, expected_data, operator)
                                else:
                                    logger.error("第{}个预期结果，其所有字段的长度是：{} ，与实际结果的长度：{} ，不相等，无法进行比较！".format(i + 1, len(every_expected_result), len(every_acture_result)))
                    else:
                        logger.info("预期结果的数量是：{} ， 实际结果的数量是：{} ，不相等，无法进行比较！".format(len(expected_value), len(acture_result)))
            elif isinstance(acture_result, str):
                # 先判断SQL预期结果，其长度
                if len(expected_value) == 1:
                    logger.info("表示仅对一条查询结果进行比较")
                    # 遍历每个预期结果
                    for i in range(len(expected_value)):
                        every_expected_result = expected_value[i]
                        logger.info("当前正在对第{}个预期结果：{} 进行比较".format(i + 1, every_expected_result))
                        # 判断其数据类型，并对其进行比较
                        if isinstance(every_expected_result, dict):
                            # 判断其所有key组成的列表长度是否与SQL查询出来的实际结果一致
                            key_list = list(every_expected_result.keys())
                            # 获取要与实际结果进行比较的预期结果
                            for key in key_list:
                                expected_value = every_expected_result[key]
                                # 调用比较方法
                                flag = compare_api_result(acture_result, expected_value, operator)
            elif isinstance(acture_result, int):
                # 先判断SQL预期结果，其长度
                if len(expected_value) == 1:
                    logger.info("表示仅对一条查询结果进行比较")
                    # 遍历每个预期结果
                    for i in range(len(expected_value)):
                        every_expected_result = expected_value[i]
                        logger.info("当前正在对第{}个预期结果：{} 进行比较".format(i + 1, every_expected_result))
                        # 判断其数据类型，并对其进行比较
                        if isinstance(every_expected_result, dict):
                            # 判断其所有key组成的列表长度是否与SQL查询出来的实际结果一致
                            key_list = list(every_expected_result.keys())
                            # 获取要与实际结果进行比较的预期结果
                            for key in key_list:
                                expected_value = every_expected_result[key]
                                # 调用比较方法
                                flag = compare_api_result(acture_result, expected_value, operator)
            else:
                logger.error("当预期结果是tuple类型时，实际结果不是tuple类型，而是：{} 类型，无法进行比较！".format(type(acture_result)))
        elif isinstance(acture_result, str):
            if isinstance(expected_value, str):
                logger.info("dddddddddddddd")
                flag = compare_api_result(acture_result, expected_value, operator)
                # if operator in ["==", "!=", "in", "not in"]:
                #     if operator == "==":
                #         if acture_result == expected_value:
                #             logger.debug("预期结果是：{}".format(expected_value))
                #             logger.debug("待比较的接口返回值是：{}".format(acture_result))
                #             logger.debug("预期结果等于待比较的接口返回值，PASS")
                #             flag = True
                #         else:
                #             logger.debug("预期结果不等于待比较的接口返回值，FAIL")
                #             logger.debug("预期结果是：{}".format(expected_value))
                #             logger.debug("待比较的接口返回值是：{}".format(acture_result))
                #             flag = False
                #     elif operator == "!=":
                #         if acture_result != expected_value:
                #             logger.debug("预期结果是：{}".format(expected_value))
                #             logger.debug("待比较的接口返回值是：{}".format(acture_result))
                #             logger.debug("预期结果不等于待比较的接口返回值，PASS")
                #             flag = True
                #         else:
                #             logger.debug("预期结果等于待比较的接口返回值，FAIL")
                #             logger.debug("预期结果是：{}".format(expected_value))
                #             logger.debug("待比较的接口返回值是：{}".format(acture_result))
                #             flag = False
                #     elif operator == "in":
                #         if acture_result in expected_value:
                #             logger.debug("预期结果是：{}".format(expected_value))
                #             logger.debug("待比较的接口返回值是：{}".format(acture_result))
                #             logger.debug("预期结果在待比较的接口返回值里，PASS")
                #             flag = True
                #         else:
                #             logger.debug("预期结果不在等于待比较的接口返回值里，FAIL")
                #             logger.debug("预期结果是：{}".format(expected_value))
                #             logger.debug("待比较的接口返回值是：{}".format(acture_result))
                #             flag = False
                #     elif operator == "not in":
                #         if acture_result not in expected_value:
                #             logger.debug("预期结果是：{}".format(expected_value))
                #             logger.debug("待比较的接口返回值是：{}".format(acture_result))
                #             logger.debug("预结果不在待比较的接口返回值里，PASS")
                #             flag = True
                #         else:
                #             logger.debug("预期结果在待比较的接口返回值里，FAIL")
                #             logger.debug("预期结果是：{}".format(expected_value))
                #             logger.debug("待比较的接口返回值是：{}".format(acture_result))
                #             flag = False
                # else:
                #     logger.error("当数据类型是str时，操作器的数据类型必须是==, !=, in, not in 里面的任意一种, 而当前的操作器的值是：{}".format(operator))
            else:
                logger.error("当实际结果是str类型时，预期结果不是str类型，而是：{} 类型，无法进行比较！".format(type(expected_value)))
        elif isinstance(acture_result, int):
            if isinstance(expected_value, int):
                if operator in ["==", "!=", "<", "<=", ">"]:
                    if operator == "==":
                        if acture_result == expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                            logger.debug("预期结果等于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果不等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                            flag = False
                    elif operator == "!=":
                        if acture_result != expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                            logger.debug("预期结果不等于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                            flag = False
                    elif operator == "<":
                        if acture_result > expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                            logger.debug("预期结果小于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果大于等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                            flag = False
                    elif operator == "<=":
                        if acture_result >= expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                            logger.debug("预期结果小于等于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果大于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                            flag = False
                    elif operator == ">":
                        if acture_result < expected_value:
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                            logger.debug("预期结果大于待比较的接口返回值，PASS")
                            flag = True
                        else:
                            logger.debug("预期结果小于等于待比较的接口返回值，FAIL")
                            logger.debug("预期结果是：{}".format(expected_value))
                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                            flag = False
                else:
                    logger.error("当数据类型是int时，操作器的数据类型必须是==, !=, <, <=, > 里面的任意一种, 而当前的操作器的值是：{}".format(operator))
            elif isinstance(expected_value, tuple):
                for i in range(len(expected_value)):
                    value = expected_value[i]
                    if isinstance(value, dict):
                        key_list = list(value.keys())
                        if len(key_list) == 1:
                            expected_value = value[key_list[0]]
                            if isinstance(expected_value, int):
                                # 根据操作器的类型，进行判断
                                if operator in ["==", "!=", "<", "<=", ">"]:
                                    if operator == "==":
                                        if acture_result == expected_value:
                                            logger.debug("预期结果是：{}".format(expected_value))
                                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                                            logger.debug("预期结果等于待比较的接口返回值，PASS")
                                            flag = True
                                        else:
                                            logger.debug("预期结果不等于待比较的接口返回值，FAIL")
                                            logger.debug("预期结果是：{}".format(expected_value))
                                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                                            flag = False
                                    elif operator == "!=":
                                        if acture_result != expected_value:
                                            logger.debug("预期结果是：{}".format(expected_value))
                                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                                            logger.debug("预期结果不等于待比较的接口返回值，PASS")
                                            flag = True
                                        else:
                                            logger.debug("预期结果等于待比较的接口返回值，FAIL")
                                            logger.debug("预期结果是：{}".format(expected_value))
                                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                                            flag = False
                                    elif operator == "<":
                                        if acture_result > expected_value:
                                            logger.debug("预期结果是：{}".format(expected_value))
                                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                                            logger.debug("预期结果小于待比较的接口返回值，PASS")
                                            flag = True
                                        else:
                                            logger.debug("预期结果大于等于待比较的接口返回值，FAIL")
                                            logger.debug("预期结果是：{}".format(expected_value))
                                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                                            flag = False
                                    elif operator == "<=":
                                        if acture_result >= expected_value:
                                            logger.debug("预期结果是：{}".format(expected_value))
                                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                                            logger.debug("预期结果小于等于待比较的接口返回值，PASS")
                                            flag = True
                                        else:
                                            logger.debug("预期结果大于待比较的接口返回值，FAIL")
                                            logger.debug("预期结果是：{}".format(expected_value))
                                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                                            flag = False
                                    elif operator == ">":
                                        if acture_result < expected_value:
                                            logger.debug("预期结果是：{}".format(expected_value))
                                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                                            logger.debug("预期结果大于待比较的接口返回值，PASS")
                                            flag = True
                                        else:
                                            logger.debug("预期结果小于等于待比较的接口返回值，FAIL")
                                            logger.debug("预期结果是：{}".format(expected_value))
                                            logger.debug("待比较的接口返回值是：{}".format(acture_result))
                                            flag = False
                                else:
                                    logger.error("当数据类型是int时，操作器的数据类型必须是==, !=, <, <=, > 里面的任意一种, 而当前的操作器的值是：{}".format(operator))
                            else:
                                logger.error("当实际结果是int类型时，预期结果不是int类型，而是：{} 类型，无法进行比较！".format(type(expected_value)))
                        else:
                            logger.error("第{}个预期结果，其值的key的长度是：{} ，本系统暂不支持！".format(i + 1, len(key_list)))
                    else:
                        logger.error("第{}个预期结果，其值的数据类型不是dict，而是：{} ，无法进行比较".format(i + 1, type(value)))
            else:
                logger.error("当实际结果是int类型时，预期结果既不是int类型，也不是tuple类型，而是：{} 类型，无法进行比较！".format(type(expected_value)))
        else:
            logger.error("当前实际结果的数据类型是：{} ，本套代码暂不支持对这种类型的数据，进行比较！".format(type(acture_result)))
        return flag
    except Exception as e:
        logger.error("比较预期结果和实际结果失败！报错信息是：{}".format(e))