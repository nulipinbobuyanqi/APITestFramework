# coding:utf-8
# @Author: wang_cong
# 第八步：获取当前日期，作为接口版本号
import os
import time
from Utils.get_project_config import get_project_config_info
from Utils.operation_json import get_json_data
from Utils.operation_yml import get_yaml_data, save_ruamel_data

new = time.strftime("%Y-%m-%d", time.localtime())
# new = "2021-08-04"

# 第一步：获取项目配置信息的存放根路径
project_yaml_path = "."
project_yaml_file_name = "project_path"
gen_path = get_yaml_data(project_yaml_path, project_yaml_file_name)["project_path"]
project_path = gen_path + "/ProjectManage/"
project_config_path = project_path + "01.ProjectConfig"
if not os.path.exists(project_config_path):
    os.makedirs(project_config_path)
# 第二步：获取项目配置信息
project, protocol, swagger_url = get_project_config_info(project_path)
# 第七步：创建所有的用例数据yml文件的存放根目录
all_cases_gen_path = project_path + "06.UnitTest/01.UnitCases" + "/" + project
if not os.path.exists(all_cases_gen_path):
    os.makedirs(all_cases_gen_path)
#
cases_path = all_cases_gen_path + "/" + new
if not os.path.exists(cases_path):
    os.mkdir(cases_path)

# 获取请求头文件内容
request_headers = get_json_data(".", "request_headers")


def write_case_header(source_path, headers):
    """

    :param source_path:
    :param case_base_path:
    :param headers:
    :return:
    """
    if os.path.exists(source_path):
        # root 所指的是当前正在遍历的这个文件夹的本身的地址
        # dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
        # files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
        for root, dirs, files in os.walk(source_path):
            for file in files:
                src_file = os.path.join(root, file).replace("\\", "/")
                # 切片
                if src_file.split(".")[-1] == "yml":
                    # 获取路径
                    yaml_path = "/".join(src_file.split("/")[:-1])
                    # 获取文件名
                    yaml_file_name = src_file.split("/")[-1].split(".")[0]
                    yaml_dict = get_yaml_data(yaml_path, yaml_file_name)
                    yaml_dict["case_common_info"]['interface_headers'] = headers
                    save_ruamel_data(yaml_path, yaml_file_name, yaml_dict)


write_case_header(cases_path, request_headers)
