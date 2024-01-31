import ddddocr


def get_img_code(img_file):
    ocr = ddddocr.DdddOcr()
    with open(f"{img_file}", "rb") as f:
        image = f.read()
    res = ocr.classification(image)
    return res


if __name__ == '__main__':
    print(get_img_code(r'D:\Python_Projects\RockProjects\Operating_UI_test\case_datas\code_image.png'))