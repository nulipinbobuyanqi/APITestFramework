# coding:utf-8
# @Author: wang_cong
import jsonpath
from Check.remove_not_compare import remove_not_compare
from Utils.operation_log import initLogger

logger = initLogger(__file__)


def get_effective_result(not_compare, extract_path, acture_result):
    """
    从实际结果中，去除不需要进行比较的字段后，返回有效的待比较的实际结果
    :param not_compare: 不进行比较的字段列表信息
    :param extract_path: 实际结果的提取路径
    :param acture_result: 实际结果
    :return: 返回有效的实际结果
    """
    # 注意：能成功调用这个方法的前提是：not_compare和actual_data一定都非空
    try:
        # 获取实际结果的提取路径的上级jsonpath
        if "." in extract_path:
            father_path = ".".join(extract_path.split(".")[:-1])
            if father_path == "$":
                father_path = "."
            else:
                father_path = father_path
            # 获取上级jsonpath的内容
            father_path_data = jsonpath.jsonpath(acture_result, father_path)
            # 判断上级jsonpath的内容，
            if not father_path_data:
                logger.error("通过上级jsonpath={} ，在实际结果中，找不到对应内容！".format(father_path_data))
            else:
                # 判断是否为None或者空
                if father_path_data == "None" or father_path_data == "" or father_path_data is None:
                    logger.error("提取路径的上个层级的值，是 None 或者 '' ")
                else:
                    # 遍历得到的list里面的值
                    for i in range(len(father_path_data)):
                        father_data = father_path_data[i]
                        # 判断这个提取路径的上个层级的值，是否为空或者None
                        if father_data is None or father_data == "":
                            logger.error("第{}个上级数据的值，为None 或者 '' ".format(i + 1))
                        else:
                            # 根据上级数据的数据类型，从实际结果中，去除不进行对比的字段列表，得到有效的实际结果
                            effective_result = remove_not_compare(father_data, not_compare)
                            return effective_result
        else:
            logger.error("当前实际结果的提取路径是：{} 不正确，请检查！".format(extract_path))
    except Exception as e:
        logger.error("获取有效的实际结果失败！报错信息是：{}".format(e))
