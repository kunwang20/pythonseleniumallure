import os

import pytest

if __name__ == '__main__':
    #  1.执行测试用例
    pytest.main()
    #  2.生成报告
    os.system("allure generate ./report -o ./allure-report")
    #  3.打开报告
    os.system("allure serve ./report ./allure-report")
