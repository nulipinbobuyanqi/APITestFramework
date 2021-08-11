# coding:utf-8
# @Author: wang_cong
import re
import jsonpath
from Utils.operation_log import initLogger

logger = initLogger(__file__)


def remove_not_compare(father_data, not_compare):
    """
    返回去除不进行比较字段的有效的实际结果
    :param father_data: 待去除的数据，其上级jsonpath的数据
    :param not_compare: 不进行比较的字段列表
    :return: 返回去除不进行比较字段的有效的实际结果
    """
    try:
        if isinstance(father_data, list) or isinstance(father_data, dict):
            # 遍历每个不进行比较的jsonpath
            for every_remove_path in not_compare:
                # 判断这个jsonpath的末尾是否含有[]符号，含有的话，说明就是从list里面去除，不含的话，说明是否dict里面去除
                if every_remove_path.endswith("]"):
                    logger.debug("说明就是从list里面去除")
                    # 判断要被删除的数据，其上一个层级的数据类型
                    split_data = every_remove_path.split("[")
                    pattern = re.compile(r'\]')
                    index_list = []
                    for da in split_data:
                        if pattern.search(da):
                            index_value = da.split("]")[0]
                            index_list.append(index_value)
                        else:
                            hh = jsonpath.jsonpath(father_data, da)
                            if hh:
                                continue
                    logger.debug("要被删除的数据，其index的范围是：{}".format(index_list))
                    if len(index_list) == 1:
                        for acture_data in hh:
                            for every_index_range in index_list:
                                if every_index_range == "*":
                                    logger.debug("这是要清空整个list的值")
                                    # 从实际结果中，去除不对比的数据
                                    acture_data.clear()
                                    logger.debug("从实际结果中，去除不对比的数据，成功！")
                                    logger.debug("实际结果={} ".format(father_data))
                                else:
                                    logger.debug("这是要去除部分list的值")
                                    # 获取要去除的index的范围值
                                    # index_range = every_not_compare.split("[")[-1].split("]")[0]
                                    logger.debug("即将要删除的index的范围是：{} ".format(every_index_range))
                                    if ":" in every_index_range:
                                        start_data = every_index_range.split(":")[0]
                                        end_data = every_index_range.split(":")[-1]
                                        if start_data != "":
                                            start = int(start_data)
                                            if end_data != "":
                                                end = int(end_data)
                                                # 从实际结果中，去除不对比的数据
                                                del acture_data[start:end]
                                                logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                logger.debug("实际结果={} ".format(father_data))
                                            else:
                                                # 从实际结果中，去除不对比的数据
                                                del acture_data[start:]
                                                logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                logger.debug("实际结果={} ".format(father_data))
                                        else:
                                            if end_data != "":
                                                end = int(end_data)
                                                # 从实际结果中，去除不对比的数据
                                                del acture_data[:end]
                                                logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                logger.debug("实际结果={} ".format(acture_data))
                                            else:
                                                # 从实际结果中，去除不对比的数据
                                                del acture_data[:]
                                                logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                logger.debug("实际结果={} ".format(acture_data))
                                    else:
                                        logger.debug("这是要去除list里面的某个值")
                                        for index in every_index_range:
                                            int_index = int(index)
                                            if int_index < len(acture_data):
                                                logger.debug("即将要删除的index的值是：{} ".format(int_index))
                                                # 从实际结果中，去除不对比的数据
                                                acture_data.pop(int_index)
                                                logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                logger.debug("实际结果={} ".format(acture_data))
                                            else:
                                                logger.error("要被删除的数据，其index值={}，超过列表的范围！请检查！".format(int_index))
                    else:
                        logger.debug("ddd")
                        # 找到最后一个index的值，然后获取这个index的值，将其作为接下来要删除数据的基础数据
                        # last_index = index_list[-1]
                        # 先找到基准值
                        base_data = every_remove_path.split("[")[0]
                        # logger.debug(base_data)
                        start_jsonpath = every_remove_path.split("[")[1:-1]
                        for f in start_jsonpath:
                            start_jsonpath = "[" + f
                        start_jsonpath = base_data + start_jsonpath
                        # 结尾的index范围
                        end_index = index_list[-1]
                        # 在实际结果中，通过这个jsonpath找到基准值
                        base_value = jsonpath.jsonpath(father_data, start_jsonpath)
                        # # 接下来，一切都是在这个基准值下，进行的删除
                        if base_value:
                            logger.debug("在实际结果中，找到了对应要删除的数据")
                            for to_delete_data in base_value:
                                if end_index == "*":
                                    logger.debug("这是要清空整个list的值")
                                    # 从实际结果中，去除不对比的数据
                                    to_delete_data.clear()
                                    logger.debug("从实际结果中，去除不对比的数据，成功！")
                                    logger.debug("实际结果={} ".format(father_data))
                                else:
                                    logger.debug("这是要去除部分list的值")
                                    # 获取要去除的index的范围值
                                    # index_range = every_not_compare.split("[")[-1].split("]")[0]
                                    logger.debug("即将要删除的index的范围是：{} ".format(end_index))
                                    if ":" in end_index:
                                        start_data = end_index.split(":")[0]
                                        end_data = end_index.split(":")[-1]
                                        if start_data != "":
                                            start = int(start_data)
                                            if end_data != "":
                                                end = int(end_data)
                                                # 从实际结果中，去除不对比的数据
                                                del to_delete_data[start:end]
                                                logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                logger.debug("实际结果={} ".format(father_data))
                                            else:
                                                # 从实际结果中，去除不对比的数据
                                                del to_delete_data[start:]
                                                logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                logger.debug("实际结果={} ".format(father_data))
                                        else:
                                            if end_data != "":
                                                end = int(end_data)
                                                # 从实际结果中，去除不对比的数据
                                                del to_delete_data[:end]
                                                logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                logger.debug("实际结果={} ".format(father_data))
                                            else:
                                                # 从实际结果中，去除不对比的数据
                                                del to_delete_data[:]
                                                logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                logger.debug("实际结果={} ".format(father_data))
                                    else:
                                        logger.debug("这是要去除list里面的某个值")
                                        for index in end_index:
                                            int_index = int(index)
                                            if int_index < len(to_delete_data):
                                                logger.debug("即将要删除的index的值是：{} ".format(int_index))
                                                # 从实际结果中，去除不对比的数据
                                                to_delete_data.pop(int_index)
                                                logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                logger.debug("实际结果={} ".format(to_delete_data))
                                            else:
                                                logger.error("要被删除的数据，其index值={}，超过列表的范围！请检查！".format(int_index))
                        else:
                            logger.error("在实际结果中，没有找到要删除的数据")
                else:
                    logger.debug("说明就是从dict里面去除")
                    if "." in every_remove_path:
                        remove_father_path = ".".join(every_remove_path.split(".")[:-1])
                        logger.debug("要被删除的数据，其上级数据的jsonpath={} ".format(remove_father_path))
                        # 判断要被删除的数据，其上级是否是根部
                        if remove_father_path == "$":
                            logger.debug("上级是根部")
                            first_path = "."
                            # 从实际结果中，找到上级数据
                            superior_data = jsonpath.jsonpath(father_data, first_path)
                            if superior_data:
                                # 获取要被删除的数据，其对应的key值
                                remove_key = every_remove_path.split(".")[-1]
                                logger.debug("要被删除的数据，其对应的key值是：{}".format(remove_key))
                                if remove_key != "":
                                    for superior in superior_data:
                                        if remove_key in list(superior.keys()):
                                            # 从得到的结果中，去除要被删除的数据
                                            superior.pop(remove_key)
                                            logger.debug("从实际结果中，删除不对比数据成功")
                                        else:
                                            logger.error("要被删除的数据，其key={} 不在数据里，请检查！".format(remove_key))
                                else:
                                    logger.error("当前要被删除的数据，其jsonpath的值={} ，格式错误，请检查！".format(every_remove_path))

                            else:
                                logger.error("通过上级的jsonpath={} ，在要被删除的数据中，没有找到要匹配的数据".format(every_remove_path))
                        else:
                            logger.debug("上级不是根部")
                            # 判断是否以[]符号结尾，是的话，就是从list里面去除数据，否则，就是从dict里面去除数据
                            if remove_father_path.endswith("]"):
                                logger.debug("list")
                                # 判断要被删除的数据，其上一个层级的数据类型
                                split_data = every_remove_path.split("[")
                                pattern = re.compile(r'\]')
                                index_list = []
                                for da in split_data:
                                    if pattern.search(da):
                                        index_value = da.split("]")[0]
                                        index_list.append(index_value)
                                    else:
                                        hh = jsonpath.jsonpath(father_data, da)
                                        if hh:
                                            continue
                                logger.debug("要被删除的数据，其index的范围是：{}".format(index_list))
                                if len(index_list) == 1:
                                    logger.debug("说明整个jsonpath只有一个[]符号")
                                    for acture_data in hh:
                                        for every_index_range in index_list:
                                            logger.debug("即将要被剔除的数据，其index范围是：{}".format(every_index_range))
                                            if every_index_range == "*":
                                                logger.debug("这是要从整个list里面，进行剔除")
                                                # 找到要去除list里面的每个key
                                                remove_key = every_remove_path.split(".")[-1]
                                                logger.debug(remove_key)
                                                # 遍历实际结果，一个个去除这个key
                                                for every_actual_data in acture_data:
                                                    every_actual_data.pop(remove_key)
                                                logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                logger.debug("实际结果={} ".format(father_data))
                                            else:
                                                logger.debug("这是要从部分list里面，进行剔除")
                                                # 获取要去除的index的范围值
                                                # index_range = every_not_compare.split("[")[-1].split("]")[0]
                                                # logger.debug("即将要删除的index的范围是：{} ".format(every_index_range))
                                                if ":" in every_index_range:
                                                    start_data = every_index_range.split(":")[0]
                                                    end_data = every_index_range.split(":")[-1]
                                                    if start_data != "":
                                                        start = int(start_data)
                                                        if end_data != "":
                                                            end = int(end_data)
                                                            # 找到要去除list里面的每个key
                                                            remove_key = every_remove_path.split(".")[-1]
                                                            logger.debug(remove_key)
                                                            # 遍历实际结果，一个个去除这个key
                                                            for every_actual_data in acture_data[start:end]:
                                                                every_actual_data.pop(remove_key)
                                                            logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                            logger.debug("实际结果={} ".format(father_data))
                                                        else:
                                                            # 从实际结果中，去除不对比的数据
                                                            # 找到要去除list里面的每个key
                                                            remove_key = every_remove_path.split(".")[-1]
                                                            logger.debug(remove_key)
                                                            # 遍历实际结果，一个个去除这个key
                                                            for every_actual_data in acture_data[start:]:
                                                                every_actual_data.pop(remove_key)
                                                            logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                            logger.debug("实际结果={} ".format(father_data))
                                                    else:
                                                        if end_data != "":
                                                            end = int(end_data)
                                                            # 从实际结果中，去除不对比的数据
                                                            # 找到要去除list里面的每个key
                                                            remove_key = every_remove_path.split(".")[-1]
                                                            logger.debug(remove_key)
                                                            # 遍历实际结果，一个个去除这个key
                                                            for every_actual_data in acture_data[:end]:
                                                                every_actual_data.pop(remove_key)
                                                            logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                            logger.debug("实际结果={} ".format(acture_data))
                                                        else:
                                                            # 从实际结果中，去除不对比的数据
                                                            # 找到要去除list里面的每个key
                                                            remove_key = every_remove_path.split(".")[-1]
                                                            logger.debug(remove_key)
                                                            # 遍历实际结果，一个个去除这个key
                                                            for every_actual_data in acture_data[:]:
                                                                every_actual_data.pop(remove_key)
                                                            logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                            logger.debug("实际结果={} ".format(acture_data))
                                                else:
                                                    logger.debug("这是要从list里面的具体某个值，进行剔除")
                                                    for index in every_index_range:
                                                        int_index = int(index)
                                                        if int_index < len(acture_data):
                                                            logger.debug("即将要删除的index的值是：{} ".format(int_index))
                                                            # 从实际结果中，去除不对比的数据
                                                            # 找到要去除list里面的每个key
                                                            remove_key = every_remove_path.split(".")[-1]
                                                            logger.debug(remove_key)
                                                            # 遍历实际结果，一个个去除这个key
                                                            acture_data[int_index].pop(remove_key)
                                                            logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                            logger.debug("实际结果={} ".format(acture_data))
                                                        else:
                                                            logger.error("要被删除的数据，其index值={}，超过列表的范围！请检查！".format(int_index))
                                else:
                                    logger.debug("说明整个jsonpath不止有一个[]符号，我们只需要关注最后一个[]符号")
                                    # 找到最后一个index的值，然后获取这个index的值，将其作为接下来要删除数据的基础数据
                                    # last_index = index_list[-1]
                                    # 先找到基准值
                                    base_data = every_remove_path.split("[")[0]
                                    logger.debug(base_data)
                                    start_jsonpath = every_remove_path.split("[")[1:-1]
                                    for f in start_jsonpath:
                                        start_jsonpath = "[" + f
                                    start_jsonpath = base_data + start_jsonpath
                                    logger.debug("要被去除的数据，其上级jsonpath={}".format(start_jsonpath))
                                    # 结尾的index范围
                                    end_index = index_list[-1]
                                    logger.debug("要被去除的数据，其index范围是：{}".format(end_index))
                                    # 在实际结果中，通过这个jsonpath找到基准值
                                    base_value = jsonpath.jsonpath(father_data, start_jsonpath)
                                    logger.debug("要被去除的数据，其值是：{}".format(base_value))
                                    # # 接下来，一切都是在这个基准值下，进行的删除
                                    if base_value:
                                        logger.debug("在实际结果中，找到了对应要删除的数据")
                                        for to_delete_data in base_value:
                                            logger.debug("要被去除的数据，其值是：{}".format(to_delete_data))
                                            if end_index == "*":
                                                logger.debug("这是要清空整个list的值")
                                                # 从实际结果中，去除不对比的数据
                                                # 找到要去除list里面的每个key
                                                remove_key = every_remove_path.split(".")[-1]
                                                logger.debug(remove_key)
                                                # 遍历实际结果，一个个去除这个key
                                                for every_actual_data in to_delete_data:
                                                    every_actual_data.pop(remove_key)
                                                logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                logger.debug("实际结果={} ".format(father_data))
                                            else:
                                                logger.debug("这是要从部分list里面，进行剔除")
                                                # 获取要去除的index的范围值
                                                logger.debug("即将要删除的index的范围是：{} ".format(end_index))
                                                if ":" in end_index:
                                                    start_data = end_index.split(":")[0]
                                                    end_data = end_index.split(":")[-1]
                                                    if start_data != "":
                                                        start = int(start_data)
                                                        if end_data != "":
                                                            end = int(end_data)
                                                            # 从实际结果中，去除不对比的数据
                                                            # 找到要去除list里面的每个key
                                                            remove_key = every_remove_path.split(".")[-1]
                                                            # 遍历实际结果，一个个去除这个key
                                                            for every_actual_data in to_delete_data[start:end]:
                                                                every_actual_data.pop(remove_key)
                                                            logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                            logger.debug("实际结果={} ".format(father_data))

                                                        else:
                                                            # 从实际结果中，去除不对比的数据
                                                            # 找到要去除list里面的每个key
                                                            remove_key = every_remove_path.split(".")[-1]
                                                            # 遍历实际结果，一个个去除这个key
                                                            for every_actual_data in to_delete_data[start:]:
                                                                every_actual_data.pop(remove_key)
                                                            logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                            logger.debug("实际结果={} ".format(father_data))
                                                    else:
                                                        if end_data != "":
                                                            end = int(end_data)
                                                            # 从实际结果中，去除不对比的数据
                                                            # 找到要去除list里面的每个key
                                                            remove_key = every_remove_path.split(".")[-1]
                                                            # 遍历实际结果，一个个去除这个key
                                                            for every_actual_data in to_delete_data[:end]:
                                                                every_actual_data.pop(remove_key)
                                                            logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                            logger.debug("实际结果={} ".format(father_data))

                                                        else:
                                                            # 从实际结果中，去除不对比的数据
                                                            # 找到要去除list里面的每个key
                                                            remove_key = every_remove_path.split(".")[-1]
                                                            # 遍历实际结果，一个个去除这个key
                                                            for every_actual_data in to_delete_data[:]:
                                                                every_actual_data.pop(remove_key)
                                                            logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                            logger.debug("实际结果={} ".format(father_data))

                                                else:
                                                    logger.debug("这是要从list里面的具体某个值，进行剔除")
                                                    for index in end_index:
                                                        int_index = int(index)
                                                        logger.debug("即将要删除的index的值是：{} ".format(int_index))
                                                        if int_index < len(to_delete_data):
                                                            logger.debug("即将要删除的index的值是：{} ".format(int_index))
                                                            # 从实际结果中，去除不对比的数据
                                                            # 找到要去除list里面的每个key
                                                            remove_key = every_remove_path.split(".")[-1]
                                                            logger.debug(remove_key)
                                                            # 遍历实际结果，一个个去除这个key
                                                            to_delete_data[int_index].pop(remove_key)
                                                            logger.debug("从实际结果中，去除不对比的数据，成功！")
                                                            logger.debug("实际结果={} ".format(acture_data))
                                                        else:
                                                            logger.error("要被删除的数据，其index值={}，超过列表的范围！请检查！".format(int_index))
                                    else:
                                        logger.error("在实际结果中，没有找到要删除的数据")
                            else:
                                logger.debug("dict")
                                # 从实际结果中，找到上级数据
                                superior_data = jsonpath.jsonpath(father_data, remove_father_path)
                                if superior_data:
                                    # 获取要被删除的数据，其对应的key值
                                    remove_key = every_remove_path.split(".")[-1]
                                    logger.debug("要被删除的数据，其对应的key值是：{}".format(remove_key))
                                    if remove_key != "":
                                        for superior in superior_data:
                                            if remove_key in list(superior.keys()):
                                                # 从得到的结果中，去除要被删除的数据
                                                superior.pop(remove_key)
                                                logger.debug("从实际结果中，删除不对比数据成功")
                                            else:
                                                logger.error("要被删除的数据，其key={} 不在数据里，请检查！".format(remove_key))
                                    else:
                                        logger.error("当前要被删除的数据，其jsonpath的值={} ，格式错误，请检查！".format(every_remove_path))
                                else:
                                    logger.error("通过上级的jsonpath={} ，在要被删除的数据中，没有找到要匹配的数据".format(every_remove_path))
                    else:
                        # 说明直接从根部去除所有的数据
                        father_data.clear()
            logger.debug("干净的实际结果是：{}".format(father_data))
            return father_data
        else:
            logger.error("提取出来的返回值，其jsonpath的上一个层级的数据类型，是：{} 。既不是list，也不是dict，无法进行剔除！".format(type(father_data)))
    except Exception as e:
        logger.error("从实际结果中，去除不需要进行比较的字段失败！报错信息是：{}".format(e))
