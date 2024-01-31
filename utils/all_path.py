# -- coding: utf-8 --
# 通过获取当前环境的地址，避免切换环境后path不对的问题
import os


project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 举例
screenshots_path = os.path.join(project_path, "outputs\\screenshots\\")
log_save_path = os.path.join(project_path, "outputs\\logs\\")
operating_elements_yaml_path = os.path.join(project_path, "common\\") + "operating_elements.yaml"
img_code_path = os.path.join(project_path, "case_datas\\") + "code_image.png"


if __name__ == '__main__':
    print(operating_elements_yaml_path)