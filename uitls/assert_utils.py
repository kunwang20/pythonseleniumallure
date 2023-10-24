from uitls.log_uitls import logger


def assert_compare(expect, compare, actual):
    """

    :param expect: 预期结果
    :param compare: 断言方式
    :param actual: 实际结果
    :return:
    """
    logger.info(f'预期结果：{expect} {compare} {actual}')
    try:
        if compare == "==":
            assert expect == actual
        elif compare == "!=":
            assert expect != actual
        elif compare == ">":
            assert expect > actual
        elif compare == "<":
            assert expect < actual
        elif compare == "in":
            assert expect in actual
        else:
            try:
                raise NameError(f"{compare}断言方式错误，请检查")
            except Exception as e:
                logger.error(e)
                raise
        logger.info(f"断言成功")
    except AssertionError as e:
        logger.error(f"断言失败：{e}")
        raise
