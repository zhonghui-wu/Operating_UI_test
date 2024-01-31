import yaml


def get_yaml_data(yaml_path):
    with open(yaml_path, encoding="utf-8") as f:
        return yaml.safe_load(f.read())


if __name__ == '__main__':
    print(get_yaml_data(r'D:\Python_Projects\RockProjects\Operating_UI_test\common\test.yaml'))