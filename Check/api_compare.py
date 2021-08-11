# coding:utf-8
# @Author: wang_cong
import jsonpath
from Check.compare_api_result import compare_api_result
from Check.get_effective_result import get_effective_result
from Utils.operation_log import initLogger

logger = initLogger(__file__)


def api_compare(acture_result, not_compare, operator, expected_value, extract_path):
    """
    比较预期结果和实际结果，返回比较失败或者成功
    :param acture_result: 实际结果
    :param not_compare: 不进行比较的字段列表
    :param operator: 操作器
    :param expected_value: 预期结果
    :param extract_path: 实际结果的提取路径
    :return: 返回接口比较失败或者成功
    """
    try:
        # 假设结果比较的值flag，默认是False
        flag = False
        # 从实际接口返回值中，通过提取路径，得到准备需要进行接口校验的数据
        compare_actual_res = jsonpath.jsonpath(acture_result, extract_path)
        # 注意：jsonpath的方式寻找匹配值，若没有找到，返回的是False，找到了，就返回匹配搭配的数据
        if not compare_actual_res:
            flag = False
        else:
            # 对待比较结果，进行判断
            if compare_actual_res == "None" or compare_actual_res == "":
                if not_compare is not None:
                    logger.error("待比较的结果为空时，not_compare字段也必须为空！因此，直接判断为 Fail ")
                else:
                    # 对操作器的类型，进行判断
                    if operator in ["is None", "=="]:
                        # 根据操作器的类型，对预期结果的值进行判断
                        if operator == "is None":
                            if expected_value is None or expected_value == "":
                                flag = True
                            else:
                                flag = False
                        elif operator == "==":
                            if expected_value is None or expected_value == "":
                                flag = True
                            else:
                                flag = False
                    else:
                        logger.error("待比较的结果为空时，操作器只能是is None 或者 ==")
            else:
                # 遍历得到的list里面的值，开始进行分析
                for i in range(len(compare_actual_res)):
                    actual_data = compare_actual_res[i]
                    # 判断这个待比较的数据，是否为空或者None
                    if actual_data is None or actual_data == "" or actual_data == []:
                        # 继续判断not_compare字段的值
                        if not_compare is not None:
                            logger.error("待比较的结果为空时，not_compare字段也必须为空！因此，直接判断为 Fail ")
                        else:
                            # 需要对操作器的类型，进行判断
                            if operator in ["is None", "=="]:
                                if operator == "is None":
                                    if expected_value is None or expected_value == "":
                                        flag = True
                                    else:
                                        flag = False
                                elif operator == "==":
                                    if expected_value is None or expected_value == "":
                                        flag = True
                                    else:
                                        flag = False
                            else:
                                logger.error("待比较的结果为空时，操作器只能是is None 或者 ==")
                    else:
                        # 继续判断not_compare字段的值
                        if not_compare is None:
                            # 直接进行比较
                            flag = compare_api_result(actual_data, expected_value, operator)
                        else:
                            # 从待比较的实际结果中，去除不进行比较的字段信息，得到干净的待比较实际结果
                            actual_data = get_effective_result(not_compare, extract_path, acture_result)
                            if actual_data:
                                # 直接进行比较
                                flag = compare_api_result(actual_data, expected_value, operator)
                            else:
                                logger.error("获取有效的实际结果错误！")
        return flag
    except Exception as e:
        logger.error("接口-比较实际结果和预期结果失败！报错信息是：{}".format(e))
